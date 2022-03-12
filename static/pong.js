const client_id = Date.now()

const ws = new WebSocket(`ws://localhost:8000/ws/pong/${client_id}`);
// const wsField = new WebSocket(`ws://localhost:8000/ws/field/${client_id}`);


function sendMessage(event) {
    let input = document.getElementById("messageText")
    ws.send(input.value)
    input.value = ''
    event.preventDefault()
}

document.addEventListener('keydown', (event) => {
  const keyName = event.key;
  console.log(keyName);
  ws.send(keyName)
});

ws.onmessage = function(event) {
    // var messages = document.getElementById('messages')
    // var message = document.createElement('li')
    // var content = document.createTextNode(event.data)
    // message.appendChild(content)
    // messages.appendChild(message)
    let msg = event.data;
    console.log(msg);

    try {
        let field = JSON.parse( msg );
        let pad1 = document.getElementById("pad1");

        if (field.hasOwnProperty("info")){
            renderMsg(field.info);
        } else {
            pad1.style.top = field.pad1.top + "px";
        }

    } catch (e) {
        renderMsg(e);
    }

};


function renderMsg(msg){
    let messages = document.getElementById('messages')
    let message = document.createElement('li')
    let content = document.createTextNode(msg)
    message.appendChild(content)
    messages.appendChild(message)
}