SELECT CASE WHEN 1+1 =2 THEN 'Es verdadero' ELSE 'No es Verdadero' END


DECLARE @Fecha DATE = '2020-09-05'
SELECT 
CASE WHEN MONTH(@Fecha) = 4 THEN 'Abríl'  
WHEN  MONTH(@Fecha) = 5 THEN 'Mayo'
WHEN MONTH(@Fecha) = 6 THEN 'Junio'
WHEN MONTH(@Fecha) = 7 THEN 'Julio'
WHEN MONTH(@fecha) = 8 THEN 'Agosto'
END
