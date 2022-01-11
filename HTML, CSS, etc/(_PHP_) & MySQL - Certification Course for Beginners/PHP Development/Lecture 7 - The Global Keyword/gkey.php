<!DOCTYPE html>
<html>
<body>

<?php
$x = 30;
$y = 20;


function test1() {
	// global para acceder a los valores puestos. 
     global $x, $y;
	 $y = $x + $y;
} 

test1(); // Execute Function
echo $y; // Output Value of Variable y

?>

</body>
</html>