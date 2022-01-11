<!DOCTYPE html>
<html>
<body>

<?php

//DEFAULT ARGUMENT VALUE - el igual del argumento indica el arumento que va a tener por default, por en caso de que no se ponga ningun valor al argumento.
function myAge($minage = 30) {
     echo "My age is : $minage <br>";
}

myAge();
myAge(50);
myAge(60);
myAge(18);

echo "<hr />";


//RETURNING VALUES - return para regresar la variable que quieras, en este caso los resultados de la operacion.
function add($x, $y) {
     $z = $x + $y;
     return $z;
}

echo "1 + 2 = " . add(1,2) . "<br>";
echo "3 + 4 = " . add(3,4) . "<br>";
echo "5 + 5 = " . add(5,5);

?>

</body>
</html>