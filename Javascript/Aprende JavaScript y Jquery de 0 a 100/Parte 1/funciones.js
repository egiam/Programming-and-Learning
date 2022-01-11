

function Funcion() {
    return 'Return de la primera funcion'
}

function Mostrar() {
    console.log('Dentro de la funcion');
}

Funcion()
Mostrar();


// Parametros en funciones

var n1 = prompt('Dime algo',':c')
var n2 = prompt('Dime otro algo',':c')

function Parametro() {
    
    var palabrasUnidas = n1 + ' ' + n2;

    return palabrasUnidas
}

var res = Parametro(n1,n2)

console.log(res);


// Parametro opcional

function UnirPal(n1,n2,n3 = false) {
    
    if(n3 == false){
        console.log(n1 + ' ' + n2);
    }else{
        document.write(n1+' +n2');
    }
}

UnirPal(n1,n2,true);


// Funciones dentro de funciones

function FF(n1,n2) {
    console.log(n1+' '+n2);
}

function FF1(n1,n2) {
    document.write(n1+' '+n2);
}

function FF2(n1,n2,n3 = false) {
    if(n3 == false){
        FF(n1,n2);
    }else{
        FF1(n1,n2);
    }
}

FF2(n1,n2,true)


// Anonimas

function anon(n1,n2,mult) {
    var suma = n1+n2;
    mult(suma);
    return suma;
}

anon(5,7,function(d){
    console.log('La suma es '+d);
    console.log('La multiplicacion es '+d*2);
})


// Arrow o flecha

function anon(n1,n2,fun) {
    var suma = n1+n2;
    mult(suma);
    return suma;
}

anon(5,7,d => {
    console.log('La suma es '+d);
    console.log('La multiplicacion es '+d*2);
})




