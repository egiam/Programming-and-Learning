-- Create database xxx

-- Create table xxx

-- Create procedure
Create procedure PrimerStoredPro
@CrearCatalogo BIT

AS
	
	--Crear tabla para catalogo de genero
	if @CrearCatalogo = 1
		Begin
			Create table CatGenero(CveGenero varchar(1));
		end

GO

	-- Ejecutar el stored procedure
Exec PrimerStoredPro


-- Create function
Create function pago
(
	@SDiario Money,
	@DTrabajados int
)
Returns money
as
	begin
		declare @montoPagar money;
		set @montoPagar = @SDiario * @DTrabajados;
		return @montoPagar
	end


	-- Ejecutar la funciom
select dbo.pago(150.20, 9) as pago


-- Create index
Create index IniceNacionalidad on Empleados (Nacionalidad);

