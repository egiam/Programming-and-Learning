

var boton = document.querySelector(selectors, '#boton');
var div = document.querySelector(selectors, '#div');

boton.addEventListener('click', listener, function(){
    console.log('As pulsado el boton');
    div.innerHTML = 'Has pulsado el boton';
})

function Pulsar(){
    div.innerHTML = 'Has pulsado el boton';
}

function Alerta(){
    alert('Has pulsado el div')
}

// Eventos
// onclick
// oncontextmenu
// onmouseenter
// onmousedown
// ondblclick
// onmouseleave
// onmouseover
// onmouseup




