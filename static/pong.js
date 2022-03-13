const client_id = Date.now()

const ws = new WebSocket( `ws://` + base_url + `/ws/pong/${client_id}`);
const wsField = new WebSocket(`ws://` + base_url + `/ws/field/`);

const pads = ["pad1", "pad2", "pad3", "pad4"];
const ball = document.getElementById("ball");


document.addEventListener('keydown', (event) => {
  const keyName = event.key;
  ws.send(keyName)
});

ws.onmessage = function(event) {
    handleEvent(event);
};


wsField.onmessage = function(event) {
    handleEvent(event);
};


function renderMsg(msg){
    // Function for rendering messages from backend
    let messages = document.getElementById('messages')
    let message = document.createElement('li')
    let content = document.createTextNode(msg)
    message.appendChild(content)
    messages.appendChild(message)
}


function handleEvent(event){
    // Function for handling event from websocket
    let msg = event.data;

    try {
        let field = JSON.parse( msg );

        if (field.hasOwnProperty("info")){
            renderMsg(field.info);
        } else {
            for (const padName of pads) {
                let pad = document.getElementById(padName);
                // set position
                pad.style.top = field[padName].top + "px";
                pad.style.left = field[padName].left + "px";

                // set visibility
                if (field[padName].active === true) {
                pad.style.visibility = "visible";
                } else {
                    pad.style.visibility = "hidden";
                }
            }
            // ball
            ball.style.top = field.ball.top + "px";
            ball.style.left = field.ball.left + "px";
        }

    } catch (e) {
        renderMsg("Error: " + e);
    }
}