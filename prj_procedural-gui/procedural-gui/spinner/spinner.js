(function () {
let spinners = [];

window.addEventListener("load", () => {
    spinners = document.querySelectorAll(".GUI .spinner");
    spinners.forEach(spinner => {load(spinner);});
});

function load(spinner) {
    let value = "none";
    let header = spinner.querySelector(".header");
    header.onclick = () => {togle_class(spinner,"open");}

    let hover = false;
    spinner.addEventListener("mouseover", () => {hover = true;});
    spinner.addEventListener("mouseleave", () => {hover = false;});
    
    window.addEventListener("click", () => {
        if (!hover) spinner.classList.remove("open");
    });

    let current = header.querySelector("p");
    let items = spinner.querySelectorAll(".list > p");
    items.forEach(i => {
        i.addEventListener("click", () => {
            current.innerHTML = i.innerHTML;
            value = i.innerHTML;
            spinner.classList.remove("open");
        });
    });
}

})();