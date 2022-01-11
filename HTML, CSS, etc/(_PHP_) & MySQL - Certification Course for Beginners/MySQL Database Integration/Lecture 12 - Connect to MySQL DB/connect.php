<?php
$servername = "localhost"; //The host
$username = "root"; //User
$password = "test2"; //Contraseña
$dbname = "mywebsite"; //nombre de la base de datos

// Create connection - PDO or mysqli
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection - verificar si hay errores con la coneccion
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

echo "Connected successfully";
?>