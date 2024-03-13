from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():

    # Check the content type of the incoming request
    content_type = request.headers.get('Content-Type')

    if content_type != 'application/json':
        return "Unsupported Media Type", 415

    payload = request.get_json()

    print_repository_info(payload)
    print_sender_info(payload)

    event_type = request.headers.get('X-GitHub-Event')
    print(f"Event: {event_type}")

    if event_type == "push":
        print_push_info()

    # Respond to indicate successful receipt
    return jsonify(success=True)


def print_repository_info(payload):

    repository = payload.get('repository', {})

    repo_name = repository.get('name')
    full_name = repository.get('full_name')
    repo_url = repository.get('html_url')
    description = repository.get('description')
    visibility = repository.get('visibility')

    owner_dict = repository.get('owner', {})
    owner_name = owner_dict.get('login')

    print(f"Repository: {repo_name}")
    print(f"Full Name: {full_name}")
    print(f"URL: {repo_url}")
    print(f"Description: {description}")
    print(f"Owner: {owner_name}")
    print(f"Visibility: {visibility}")


def print_sender_info(payload):

    sender = payload.get('sender', {})
    sender_login = sender.get('login')
    print(f"Sender: {sender_login}")


def print_push_info(payload):

    head_commit = payload.get('head_commit', {})
    msg = head_commit.get('message')
    print(f"Head commit: {msg}")


if __name__ == '__main__':

    app.run(port=3000, debug=True)
