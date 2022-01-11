-- UPDATE
-- SET = asignar valores a ciertos campos
-- where


update empleados
set apellido = 'Juarez'
where idEmpleado = 8

begin tran -- Nos ayuda a guardarlo directamente en la tabla
	update empleados
	set apellido = 'Trejo'
	where idEmpleado = 6

rollback tran -- Regresar a su movimiento anterior al begin tran

commit tran -- Para grabar definitivamente el begin tran





