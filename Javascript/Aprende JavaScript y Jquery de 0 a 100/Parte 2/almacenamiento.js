

if(typeof(Storage)){
    console.log('Disponible');
}else {
    console.log('No disponible');
}

// Insertar item
localStorage.setItem('clave','texto o valor de esta clave');
localStorage.setItem('edad',37);

// recojer item
var valor = localStorage.getItem(key: 'clave');
console.log(valor);

// objeo JSON
var persona = {
    edad:37,
    nombre:'Manuel',
}

localStorage.setItem('persona', JSON.stringify(persona));

var per = JSON.parse(localStorage.getItem(key:'persona'));

console.log(per.nombre);


