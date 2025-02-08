function togglePassword(id) {
    let passElement = document.getElementById(`password-${id}`);
    if (passElement.classList.contains("blur-sm")) {
        passElement.classList.remove("blur-sm");
        passElement.classList.add("font-mono");
        event.target.innerText = "Hide";
    } else {
        passElement.classList.add("blur-sm");
        passElement.classList.remove("font-mono");
        event.target.innerText = "Show";
    }
}

function copyPassword(id) {
    let passElement = document.getElementById(`password-${id}`);
    let password = passElement.innerText;

    navigator.clipboard.writeText(password).then(() => {
        alert("Password copied to clipboard!");
    }).catch(err => {
        console.error("Failed to copy: ", err);
    });
}

