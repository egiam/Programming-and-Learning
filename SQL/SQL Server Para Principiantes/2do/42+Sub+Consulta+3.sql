CREATE VIEW vAlumnosMatriculados

AS


SELECT AlumnoID, Nombre, Apellido, Edad, Sexo, Direccion ,
(select COUNT(*) from inscripcion I WHERE I.AlumnoID  = A.AlumnoID) TotalClases,

( 
	select ISNULL(SUM(Precio), 0 ) from inscripcion I INNER JOIN Clase C On I.ClaseID = C.ClaseID
	WHERE I.AlumnoID = A.AlumnoID

) SumaTotal,

(
	SELECT ISNULL( AVG(Precio),0) from Inscripcion I inner join Clase C on I.ClaseID = C.ClaseID
WHERE I.ALumnoID = A.AlumnoID
) PromedioPorClase

FROM Alumno A


select * from vAlumnosMatriculados


--AlumnoID de Ana = 3
--ClaseID = 7
--MaestroID = 3
SELECT * from Inscripcion
SELECT * from Clase
SELECT * from maestro


INSERT INTO Inscripcion (Fecha, ClaseID, AlumnoID, MaestroID, Hora)
VALUES (GETDATE(),7, 3,3 , '1400' )