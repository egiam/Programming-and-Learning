<!DOCTYPE html>
<html>
<body>

<?php

//WORD COUNT - Cuenta la cantidad de palabras en el string(caracter)
echo str_word_count("Hello world!");
echo "<hr />";

//REVERSE WORDS - Escribe al reves el string '!dlrow olleH'
echo strrev("Hello world!"); // outputs !dlrow olleH
echo "<hr />";

//SEARCH FOR TEXT INSIDE A STRING - Busca una palabra o parte de text en especifico, que se encuentre dentro del texto entero.
echo strpos("Hello world!", "world"); // outputs 6
echo "<hr />";

//REPLACE TEXT INSIDE A STRING
echo str_replace("world", "John", "Hello world!"); // outputs Hello John!
echo "<hr />";

?>  
  
</body>
</html>