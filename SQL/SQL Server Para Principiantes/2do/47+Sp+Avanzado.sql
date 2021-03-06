USE [Escuela]
GO
/****** Object:  StoredProcedure [dbo].[spInsertarAlumno]    Script Date: 4/11/2020 5:54:16 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

--spInsertarAlumno 'CarmenR', 'Pineda', 22, 'Femenino', 'Barrio el Guanacaste', '1515-5595'
--SELECT * from Alumno


ALTER Procedure [dbo].[spInsertarAlumno] 
	@Nombre VARCHAR(100),
	@Apellido VARCHAR(100),
	@Edad int,
	@Sexo VARCHAR(20),
	@Direccion VARCHAR(200),
	@Telefono VARCHAR(20)
AS
BEGIN

	DECLARE @Existe BIT = (SELECT COUNT(*) FROM Alumno WHERE Nombre =@Nombre AND Apellido =  @Apellido)
	IF(@Existe =1)
	BEGIN
		DECLARE @AlumnoID INT = (Select TOP 1 AlumnoID from Alumno Where Nombre =@Nombre AND Apellido =  @Apellido)
		UPDATE Alumno Set Edad = @Edad, Sexo = @Sexo, Direccion = @Direccion, Telefono = @Telefono Where
				AlumnoID = @AlumnoID
	END
	ELSE
	BEGIN
		INSERT INTO Alumno (Nombre, Apellido, Edad, Sexo, Direccion, Telefono)
		VALUES (@Nombre,@Apellido,@Edad,@Sexo,@Direccion,@Telefono)
	END
END