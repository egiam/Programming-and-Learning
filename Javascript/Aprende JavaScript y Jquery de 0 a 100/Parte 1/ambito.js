

var global = 'Variable Global';

function MostrarC(){
    // El ambito, la variable vive dentro del bloque de la funcion, afuera de la funcion es inexistente
    var variable_fun = 'Vriable dentro de la funcion';
    console.log(global);
    console.log(variable_fun);

}

MostrarC();

// console.log(variable_fun);


