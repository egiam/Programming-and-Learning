SELECT * from Alumno

EXEC spInsertarAlumno 'Carlos', 'Agurcia', 22, 'Masculino', 'Barrio el benque SPS', '2541-59595'


ALTER Procedure spInsertarAlumno 
	@Nombre VARCHAR(100),
	@Apellido VARCHAR(100),
	@Edad int,
	@Sexo VARCHAR(20),
	@Direccion VARCHAR(200),
	@Telefono VARCHAR(20)
AS
BEGIN
	INSERT INTO Alumno (Nombre, Apellido, Edad, Sexo, Direccion, Telefono)
	VALUES (@Nombre,@Apellido,@Edad,@Sexo,@Direccion,@Telefono)
END