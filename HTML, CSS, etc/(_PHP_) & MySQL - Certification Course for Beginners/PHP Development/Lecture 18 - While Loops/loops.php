<!DOCTYPE html>
<html>
<body>

	<?php 
	
		//WHILE LOOP - mientras que cumpla la condicion, se va a ejecutar.
		$x = 1;
		  
		while($x < 10) {
		   echo "The number is: $x <br>";
		   $x++;
		} 
		echo "<hr />";
		
		//DO WHILE LOOP - hacer mientras - se ejecuta al menos una vez y luego ve si cumple la condicion.
		$x = 6;		
		do {
		echo "The number is: $x <br>";
		$x++;
		} while ($x <= 5);
		
	?>   

</body>
</html>