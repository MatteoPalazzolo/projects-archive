(function () {
let boxSpinners = [];
    
window.addEventListener("load", () => {
    boxSpinners = document.querySelectorAll(".GUI .box-spinner");
    boxSpinners.forEach(b => {load(b)});
});

function load(b) {
    let cards = b.querySelectorAll(".card");
    cards.forEach(card => {
        card.addEventListener("click", () => {
            cards.forEach(elm => {elm.classList.remove("selected");});
            card.classList.add("selected");
        });
    });
    
}

})();