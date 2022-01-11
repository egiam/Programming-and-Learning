<!DOCTYPE html>
<html>
<body>

<?php
$car = "volvo";

// switch = opciones, si es cierto caso, ese caso se va a ejecutar.
switch ($car) {
     case "volvo":
         echo "You drive a Volvo!";
         break;
     case "bmw":
         echo "You drive a BMW!";
         break;
     case "honda":
         echo "You drive a Honda!";
         break;
     default:
         echo "You don't drive";
}
?>
  
</body>
</html>