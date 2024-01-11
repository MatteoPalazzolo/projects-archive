let img_alessio = null;
let swap = true;

$(document).ready(function() {
    img_alessio = $('#img_alessio');
});

function swap_image() {
    swap = !swap;
    let path = swap ? "./images/Alessio1.jpg" : "./images/Alessio2.jpeg";
    img_alessio.attr("src", path);
}