-- COMMIT = aceptar y dar por terminado
-- ROLLBACK = volver atras


begin tran
	update empleados
	set MartialStatus = 'S'
	where LastName = 'Castro' and FirstName = 'Alberto'

	if @@ROWCOUNT > 1
	begin
		rollback
		select 'Error'
	end
	else
	begin
		commit
		select 'Cambiado'
	end

select * from empleados
where LastName = 'Castro' and FirstName = 'Alberto'

