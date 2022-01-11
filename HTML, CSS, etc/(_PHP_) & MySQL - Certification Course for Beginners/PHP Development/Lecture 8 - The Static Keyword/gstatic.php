<!DOCTYPE html>
<html>
<body>

<?php
function test1() {
	// static: para q las variables mantengan su valor inicial, estas luego se muestran en donde llaman a la funcion. tipo un return
     static $x = 10;
     echo $x;
     $x++;
}

test1();
echo "<br>";
test1();
echo "<br>";
test1();
echo "<br>";
test1();
?>  

</body>
</html>