

// and && 
// or ||
// not !

// Control IF

var edad = 11

if (edad>18){
    console.log("Mayor de edad");
}else{
    console.log("Menor de edad")
}



if (edad>18 && edad<30){
    console.log("Mayor de edad, entre 18 y 30");
}else{
    console.log("Menor de edad o muy mayor")
}


//  Control Switch

var texto = '';

switch(edad){
    case 17:
        texto = 'No eres mayor';
    break;
    case 18:
        texto = 'Eres mayor';
    break;
    
    default:
        texto = 'Tu edad es tante q no se puede medir en este plano intradimensional, viejo'
}

console.log(texto);


// For

// Inicializacion   var i = 0;
// Evaluacion       i <= 100;
// Iteracion        i++;

for(var i = 0; i <=100; i++){
    console.log(i);
}


// while

var dato = 5;

while(dato <= 7){
    console.log('El dato vale: ' + dato);

    dato ++;
}


// Do while

var dato1 = 5;

do{
    console.log('El dato vale: ' + dato);

    dato ++;
}while(dato <= 10);



