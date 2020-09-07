# Flask Socket.IO example

Python web application showing how Socket.IO "enables realtime, bi-directional communication between web clients and servers." (official description)

This example is for development and debugging.

## Install

Requires:
- Python 3
- Flask and Flask-SocketIO modules (can be installed with `pip install Flask flask-socketio`)
- web browser that supports JavaScript

The web app itself doesn't need to be installed.

## Use

1. Run `python3 main.py` in the directory containing this web app.
2. While the app is running, open `http://127.0.0.1:5000/` in a web browser.
3. After a few seconds, you should see messages on the web page like this:
```
Client 040731b94d414a4da58ae2796f868668 got 1
Client 040731b94d414a4da58ae2796f868668 got 3
Client 040731b94d414a4da58ae2796f868668 got 5
```
Basically the server sends numbers to the browser client in real time (no reloading!)
The browser client also sends numbers back to the server.
Check the terminal window to see what the server received.

4. When you open `http://127.0.0.1:5000/` in another browser window, you should see a different client ID.
5. Type `Ctrl-C` in the terminal window to close the server. The browser windows will no longer receive the messages.

## Author, License

"flask_socketio_example" by Alan Tseng is licensed under CC0 1.0 Universal

2020
