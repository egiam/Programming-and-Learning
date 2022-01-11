<!DOCTYPE html>
<html>
<body>

<?php
// Una lista dentro de otra lista
$grades = array
   (
   array("John",50,60),
   array("Bob",40,25),
   array("Sam",35,48),
   array("Ted",55,26)
   );
   
   // el primer numero es el que marca cual lista es, el segundo marca que atributo de esa lista es.
echo $grades[0][0].": Test 1: ".$grades[0][1].", Test 2: ".$grades[0][2].".<br>";
echo $grades[1][0].": Test 1: ".$grades[1][1].", Test 2: ".$grades[1][2].".<br>";
echo $grades[2][0].": Test 1: ".$grades[2][1].", Test 2: ".$grades[2][2].".<br>";
echo $grades[3][0].": Test 1: ".$grades[3][1].", Test 2: ".$grades[3][2].".<br>";
?>

</body>
</html>