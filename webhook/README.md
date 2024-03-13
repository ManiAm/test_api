# test_webhook

`Smee.io` acts as a proxy that forwards webhook requests from GitHub to your local machine, allowing you to inspect them in real-time.

Go to https://smee.io/ and click on the "Start a new channel" button.

A new channel will be created with a unique URL. Keep this URL handy as it will be used to receive webhook payloads from GitHub and forward them to your local environment.

My URL is: https://smee.io/Ob9Pel4XzHtmFwx

The Smee client is a Node.js application that forwards the webhooks received by your Smee channel to your local machine. Install it using npm. Note that the `-g` flag tells npm to install the package globally on your system. Installing a package globally means that it will be placed in a system-wide directory, making it accessible from any location on your filesystem.

    sudo npm install -g smee-client

Run the Smee client with your Smee channel URL to start forwarding events. Replace the URL with the URL you got when you created the new channel.

    smee --url <URL>

Output:

    Forwarding https://smee.io/Ob9Pel4XzHtmFwx to http://127.0.0.1:3000/
    Connected https://smee.io/Ob9Pel4XzHtmFwx

This will start forwarding webhook events from Smee.io to http://127.0.0.1:3000.

You can override port or path with:

    smee --url <URL> --path /webhook --port 5000

Go to the GitHub repository you want to test webhooks for.

Navigate to Settings > Webhooks > Add webhook.

In the "Payload URL" field, enter the URL of your Smee.io channel.

Content type could be `application/json` or `application/x-www-form-urlencoded`. In the former, data is sent as a JSON (JavaScript Object Notation) string. JSON is a lightweight data-interchange format that is easy for humans to read and write and easy for machines to parse and generate. It supports a range of data types, including objects, arrays, numbers, and strings. In the former content type, data is sent in key-value pairs, similar to query strings in URLs. This format is essentially the same as the data format used in the query string of a URL: keys and values are paired up with = and separated from other pairs by &. JSON supports a more complex and hierarchical data structure, allowing for nesting of objects and arrays. In contrast, URL-encoded format is flat, representing only one level of key-value pairs, which makes it less suitable for complex data structures.

Select the events you want to receive or just choose "Send me everything.".

Click on "Add webhook".

Once you do that, github sends a ping payload to test it out.

You can check the content in the smee website.
