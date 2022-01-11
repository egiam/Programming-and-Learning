

CREATE View vViajesRealizados
as
	SELECT V.ViajeID, V.Fecha, CONCAT(C.Nombre, ' ', C.Apellido) NombreCliente, 
	L.Nombre Lugar , L.Direccion, CONCAT( Ch.Nombre,' ' ,Ch.Apellido ) NombreChofer
	from Viaje V 
	inner Join Cliente C on V.ClienteID= C.ClienteID
	INNER JOIN Chofer ch ON V.ChoferID = Ch.ChoferID
	INNER JOIN Lugar L ON V.LugarID = L.LugarID


select COUNT(*) Viajes, NombreChofer from vViajesRealizados
GROUP BY NombreChofer