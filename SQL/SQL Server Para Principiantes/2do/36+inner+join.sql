select * from Alumno

select * from clase

select * from Maestro

select * from Inscripcion


SELECT I.InscripcionID, I.fecha, I.Hora, C.Nombre [Nombre Clase], A.Nombre [Nombre Alumno], 
A.Direccion, M.Nombre [Nombre Maestro]
from Inscripcion I 
 INNER JOIN Clase C ON I.ClaseID = C.ClaseID
 INNER JOIN Alumno A ON I.AlumnoID = A.AlumnoID
 INNER JOIN Maestro M On I.MaestroID = M.MaestroID