$(document).ready(function() 
{
    let cards = document.querySelectorAll('button');
    for (let i = 0; i < cards.length; i++) {
        cards[i].addEventListener('click', e => {
            console.log(e.target);
            let element = e.target.parentNode.parentNode.parentNode.parentNode.parentNode.parentNode;

            $(element.querySelector('.contact main button')).toggleClass('active');
            $(element.querySelector('.contact main .title')).toggleClass('active');
            $(element.querySelector('.contact nav')).toggleClass('active');
        });
    }

});