const titleInput = document.getElementById("input-title");
const messageInput = document.getElementById("input-text");
const saveBtn = document.getElementById("save-btn");

saveBtn.addEventListener("click", function () {
    const title = titleInput.value;
    const message = messageInput.value;

    fetch("/create", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            title: title,
            message: message
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);

        if (data.result === "success") {
            alert("저장 성공!");

            titleInput.value = "";
            messageInput.value = "";
        } else {
            alert("저장 실패: " + data.message);
        }
    });
});