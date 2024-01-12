(function () {
let dropdowns = [];

window.addEventListener("load", () => {
    dropdowns = document.querySelectorAll(".GUI .dropdown");
    dropdowns.forEach(drop => {load(drop);});
});

function load(drop) {
    let header = drop.querySelector(".header");
    header.onclick = () => {togle_class(drop,"open");}
}

})();