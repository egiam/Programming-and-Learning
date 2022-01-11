select ClienteID from cliente
Union 
select ClienteID from viaje


select * from viaje

insert into viaje values (getdate(), 100000, 2,6,250)

delete from viaje where clienteid = 100000