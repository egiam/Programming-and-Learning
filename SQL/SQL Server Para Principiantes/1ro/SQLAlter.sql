-- Alter Table
-- Alter column (Para alterar una Columna ya existente)
-- Add (Para agregar una Columna nueva)


-- Alter Procedure
Alter procedure PrimerStoredP
	@CrearCatalogo bit

	as
		--Agregar columna
		if @CrearCatalogo = 1
			begin
				alter table CatGenero add DescripccionG varchar(10);
			end
	go

exec PrimerStoredP 1 --(0 o 1)


--  Alter Function
alter function pagos
(
	@SDiario money,
	@DTrabajados int
)
returns money
as
	begin
		declare @MontoPagar money;
		set @MontoPagar = (@SDiario * @DTrabajados) + (35 * @DTrabajados);
		return @MontoPagar
	end

select dbo.pago(150.20, 8) as pago

