(function () {
let sliders = [];

window.addEventListener("load", () => {
    sliders = document.querySelectorAll(".GUI .slider");
    sliders.forEach(div => {load(div);});
});

function load(div) {
    let slider = div.querySelector("input[type=range]");
    let num = div.querySelector("input[type=text]");
    num.value = slider.defaultValue;

    slider.addEventListener("input", () => {num.value = slider.value;});
    num.addEventListener("keypress", e => {if (e.key == "Enter") set();});
    num.addEventListener("focusout", e => {set()});
    function set() {
        slider.value = set_value(num.value, slider);
        num.value = set_value(num.value, slider);
    }
}

function set_value(value, slider) {
    if (isNaN(Number(value))) return Number(slider.min);
    return clamp(Number(value), Number(slider.min), Number(slider.max));
}

})();