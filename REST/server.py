from flask import Flask, request, jsonify
from flask import make_response

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def handle_get():

    # note that content_type is not relevant here,
    # as it deals with the URL part of the request.
    content_type = request.content_type

    name = request.args.get('name', 'Guest')
    return_type = request.args.get('type', 'txt')

    # make sure to use qoutes around the URL when using &

    # test with: curl "http://localhost:5000/users?name=John&type=txt"
    if return_type == "txt":
        return f'Hello, {name}'

    # test with: curl "http://localhost:5000/users?name=John&type=html"
    if return_type == "html":
        return f'<h1>Hello {name}</h1>'

    # test with: curl "http://localhost:5000/users?name=John&type=json"
    if return_type == "json":
        return jsonify(message=f"Hello, {name}!")

    return make_response('Bad request', 400)


@app.route('/users/<string:username>/pics', methods=['GET'])
@app.route('/users/<string:username>/pics/<int:pic_id>', methods=['GET'])
def get_user_pics(username, pic_id=None):

    users = {
        'john': {
            'pics': {
                123: {
                    'title': 'picture name 1',
                    'geo': 'SJC'
                }
            }
        }
    }

    user = users.get(username, None)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    # Return all pics for the user
    # test with: curl "http://localhost:5000/users/john/pics"
    if pic_id is None:
        return jsonify(user['pics'])

    # Find and return the specific pic
    # test with: curl "http://localhost:5000/users/john/pics/123"
    pics_dict = user.get("pics", {})
    pic = pics_dict.get(pic_id, None)
    if not pic:
        return jsonify({'error': 'pic not found'}), 404

    return jsonify(pic)


@app.route('/post', methods=['POST'])
def handle_post():

    content_type = request.content_type

    # test with:
    # curl -X POST -H "Content-Type: application/json" -d '{"key":"value"}' http://localhost:5000/post
    if content_type == 'application/json':

        # By default, request.get_json() will only parse the request body
        # as JSON if the Content-Type header of the request is set to application/json.
        # This is to ensure that the method attempts to parse JSON only when the
        # request explicitly indicates it's sending JSON data.
        data = request.get_json()
        if not data:
            return jsonify(error="Please provide data as JSON"), 400

        # Echo back the received data
        return jsonify(received=data)

    if content_type == 'application/x-www-form-urlencoded':

        # You might want to parse the request body as JSON regardless of the
        # Content-Type header. In such cases, you can use the force flag set to True.
        # We might be dealing with a legacy system or a bug that send JSON data
        # without the correct content-type.

        # test with:
        # curl -X POST -d '{"key":"value"}' http://localhost:5000/post
        # note that when no content type is specified, curl uses 'application/x-www-form-urlencoded' by default
        try:
            data = request.get_json(force=True)
            if data:
                # Echo back the received data
                return jsonify(received=data)
        except Exception:
            pass

        # test with:
        # curl -X POST -d "username=johndoe&password=secret" http://localhost:5000/post
        data = request.form

        username = data.get('username', 'Guest')
        password = data.get('password', '')

        print(f"username: {username}, password: {password}")

        # to return just a successful status code without any message
        return make_response('', 200)

    if content_type.startswith('multipart/form-data'):

        # test with:
        # curl -X POST -F "username=johndoe" -F "avatar=@avatar.jpg" http://localhost:5000/post

        # Accessing any standard fields in the form that contain text data, such as
        # input fields of type text, radio buttons, checkboxes (when their values are submitted),
        # hidden fields, and similar. Even though the form may include file inputs, any
        # non-file inputs should be accessed via request.form.
        data_txt = request.form

        # The request.files attribute is a dictionary-like object where the keys are the
        # names of the file input fields, and the values are Werkzeug FileStorage objects,
        # which contain the uploaded files.
        data_file = request.files

        # to return just a successful status code without any message
        return make_response('', 200)


if __name__ == '__main__':

    app.run(debug=True, port=5000)
