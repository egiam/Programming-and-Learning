<!DOCTYPE HTML>
<html> 
<body>

<!-- First Name: <?php echo $_GET["fname"]; ?><br>
Email: <?php echo $_GET["email"]; ?>  --> <!-- get method is insecure -->

First Name: <?php echo $_POST["fname"]; ?><br>
Email: <?php echo $_POST["email"]; ?>

</body>
</html>