
DECLARE @Numero1 INT = 1, @Numero2 INT=5, @Numero3 INT = 2

SELECT @Numero1 + @numero2 + @numero3


DECLARE @TotalPagoAlumno MONEY =  0;

SELECT @TOtalPagoAlumno

SET @TotalPagoAlumno = (SELECT Sum(Precio) from Inscripcion I 
Inner Join Clase C on I.ClaseID = C.ClaseID )

SELECT @TOtalPagoAlumno