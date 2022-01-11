

DECLARE @TotalClases INT = 4;
DECLARE @Descuento DECIMAL(10,10) = 0.15;
DECLARE @Precio MONEY = 100;

IF(@TotalClases > 5)
BEGIN
	SET @Precio = @precio - (@precio * @Descuento) --15
END

SELECT @Precio



IF(2+2 =5)
BEGIN
	SELECT 'Es Cierto'
END