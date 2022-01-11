<!DOCTYPE html>
<html>

<body>

<?php
// Variables empiezan con el signo $, seguido del nombre de la variable y su valor.
$var1 = "Hello world!";
$x = 15;
$y = 20.5;

// echo para mostrar la operacion, parecido a print.
echo $var1;
echo "<br>";
echo $x;
echo "<br>";
echo $y;
echo "<hr />";

// se puede poner $(nombre de variable) para que se muestre el valor de la misma
$sport= "Football";
echo "I like $sport!";
echo "<hr />";

// entre (.) para que una variable se muestre
$sport= "Football";
echo "I like " . $sport . "!";
echo "<hr />";

$x = 5;
$y = 6;
echo $x + $y;

?>

</body>
</html>