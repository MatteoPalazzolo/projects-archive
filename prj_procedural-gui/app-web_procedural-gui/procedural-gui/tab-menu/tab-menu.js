(function () {
    
window.addEventListener("load", () => {
    const menu = document.querySelector(".GUI .tab-menu");
    const items = menu.querySelectorAll(".item");
    items.forEach(tab => {load(tab)});
    items[0].classList.add("selected");
    /*NEW*/
    const gui = document.querySelector(".GUI");
    const close = document.querySelector(".GUI .close-bkg");
    close.addEventListener("click", e => { togle_class(gui, "close"); });
});

function load(tab) {
    tab.addEventListener("click", () => {
        items.forEach(i => {i.classList.remove("selected");});
        tab.classList.add("selected");
        loadHTML(Array.from(items).indexOf(tab));
    });    
}

function loadHTML(index) {
    console.log(index);
}

})();