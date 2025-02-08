
// Function to hide the form
function cancelForm() {
    document.getElementById('password_form_container').classList.add('hidden');
    
}

// Function to show the form when the Create button is clicked
function showForm() {
    document.getElementById('password_form_container').classList.remove('hidden');
}

document.addEventListener("htmx:afterRequest", function(event) {
    if (event.detail.successful) {
        document.querySelector("form").reset();
    }
});
