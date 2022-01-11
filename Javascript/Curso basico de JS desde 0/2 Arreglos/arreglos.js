
var amigos = [];

var cantidad = prompt("Ingresa la cantidad de amigos que tienes: ");

for (let c = 0; c < cantidad; c++) {
    amigos[c] = prompt("Nombre del amigo: ");
    
}

amigos.push("Jaimito");
//Para agregar al final del arreglo

amigos.pop();
//Para eliminar el ultimo del arreglo

var amigos2 = ["Luis","Fernando","Oscar"];

var amigos3 = amigos.concat(amigos2);
//Para juntar las dos listas.

amigos.join(" - ");
//Dividimos nuestro arreglo con ese formato.


document.writeln("Amigos: ");
document.writeln(amigos.join(" - "));
// for (let i = 0; i < amigos.length; i++) {
//     document.writeln(amigos[i]);
    
// }

var ordenados = amigos.sort();
//Ordena al arreglo alfabeticamente

document.writeln("Tienes " + amigos.length + " amigos");

