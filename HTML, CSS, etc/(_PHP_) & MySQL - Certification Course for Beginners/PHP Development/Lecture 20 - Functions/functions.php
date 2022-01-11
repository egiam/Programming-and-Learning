<!DOCTYPE html>
<html>
<body>

<?php
//BASIC FUNCTION
function displaytxt() {
     echo "My First Function";
}

displaytxt();
// Para llamar a la funcion

echo "<hr />";

//FUNCTION ARGUMENTS
function myCar($car) {
	// entre parentecis de la funcion, el argumento (lo que se pone cuando se llama a la funcion.)
    echo "$car<br>";
}

// Entre parentecis de la llamada, se pone el valor del argumento antes dictado.
myCar("Volvo");
myCar("BMW");
myCar("Honda");

?>



</body>
</html>