SELECT AlumnoID, Nombre, Apellido, Edad, Sexo, Direccion ,
(select COUNT(*) from inscripcion I WHERE I.AlumnoID  = A.AlumnoID) TotalClases,

( 
	select ISNULL(Sum(Precio), 0 ) from inscripcion I INNER JOIN Clase C On I.ClaseID = C.ClaseID
	WHERE I.AlumnoID = A.AlumnoID

) SumaTotal
FROM Alumno A





