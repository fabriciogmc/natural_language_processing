/* Basic front-end processor */

// First we get all html components
// references

let submit_button = document.getElementById("submit_button");
let text_input = document.getElementById("text_input");
let chat = document.getElementById("chat");



let interaction_text = []

function update_chat(){
    chat.value = "";
    interaction_text.forEach(v => {
        chat.value += v +"\n";
    });
}

// Now we define the action to be performed once the button
// is clicked (hander function)
function button_function(){
    let query_input = text_input.value
    interaction_text.push("<user>: " + query_input);
    text_input.value = ""

    axios.get("http://127.0.0.1:5000/bot_service?user_input="+query_input)
        .then(res => {
            let chat_response = res.data.response;
            interaction_text.push("<chatbot>:"+ chat_response);
            update_chat();
        })
        .catch(error => {
            console.error("Error:", error);
        });
    
}

// Here we link the button click event to hander function
submit_button.onclick =  button_function;