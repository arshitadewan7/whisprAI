function sendCommand() {
    let command = document.getElementById("commandInput").value;

    fetch("/run_assistant", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: `command=${command}`
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("response").innerHTML = `<p>${data.response}</p>`;
    })
    .catch(error => console.log('Error:', error));
}
