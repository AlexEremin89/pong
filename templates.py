html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <h2>Your ID: <span id="ws-id"></span></h2>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script type="text/javascript" src="static/chat.js"></script>
    </body>
</html>
"""

pong = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
        <style type="text/css">
            #field {
                border: 1px solid black;
                width: 400px;
                height: 400px;
            }

            .pad {
                border: 0px solid black;
                background: black;
                position: absolute;
            }

            .vertical-pad {
                left: 399px;
                top: 158px;
                width: 10px;
                height: 60px;
            }
        </style>
    </head>
    <body>
        <div id="field">
            <div id="pad1" class="pad vertical-pad"></div>
        </div>
        <ul id='messages'>
        </ul>
        <script type="text/javascript" src="static/pong.js"></script>
    </body>
</html>
"""