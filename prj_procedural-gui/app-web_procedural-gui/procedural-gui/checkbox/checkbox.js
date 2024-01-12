(function() {
let checkboxes = [];

window.addEventListener("load", () => {
    checkboxes = document.querySelectorAll(".GUI .checkbox input[type=checkbox]");
    checkboxes.forEach(e => {
        e.addEventListener("input", () => {console.log(e.checked)});
    });
});
})();