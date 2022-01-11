<!DOCTYPE html>
<html>
<body>

<?php 

	// STRING - Caracter
	$x = "Hello world!";
	$y = 'Hello world!';
	echo $x;
	echo "<br>";
	echo $y;
	echo "<hr />";

	// INTEGER - Entero
	$num = 6000;
	var_dump($num); // Para averiguar que tipo de variable es
	echo "<hr />";
	
	// FLOAT - Decimal
	$num2 = 20.565;
	var_dump($num2); // Para averiguar que tipo de variable es
	echo "<hr />";

	// ARRAY - Lista
	$sports = array("Soccer","Tennis","Baseball","Football");
	var_dump($sports); // Para averiguar que tipo de variable es
	echo "<hr />";

	// NULL - No valor asignado
	$color = "Blue";
	$color = null;
	var_dump($color); // Para averiguar que tipo de variable es
	
	// BOOLEAN - True o False
	$x = true;
	$y = false;
	var_dump($x); // Para averiguar que tipo de variable es
	var_dump($y); // Para averiguar que tipo de variable es

?>

</body>
</html>