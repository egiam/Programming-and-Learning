SELECT AlumnoID, Nombre, Apellido, Edad, Sexo, Direccion ,
(select COUNT(*) from inscripcion I WHERE I.AlumnoID  = A.AlumnoID)

FROM Alumno A


SELECT AlumnoID, Nombre, Apellido, Edad, Sexo, Direccion ,
(select SUM(*) from inscripcion I WHERE I.AlumnoID  = A.AlumnoID)

FROM Alumno A

select * from inscricion

