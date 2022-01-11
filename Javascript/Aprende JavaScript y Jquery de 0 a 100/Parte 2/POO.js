

function Persona(edad,altura,peso){
    this.edad = edad;
    this.altura = altura;
    this.peso = peso;

    this.caminar = ()=>{
        console.log('Esta persona esta caminando');
    }

    this.sentarse = ()=>{
        console.log('Se sento we :v');
    }
}

var Manuel = new Persona(37,2.00,97);
var Lucia = new Persona(33,1.77,150);

console.log(Manuel.caminar());
console.log(Lucia.sentarse());




