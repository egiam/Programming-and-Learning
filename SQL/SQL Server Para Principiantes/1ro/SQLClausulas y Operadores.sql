-- Clausulas y Operadores

-- Order by
select * from DimGeography
order by StateProvinceName desc
-- Ordenar de manera ascendente, si le agregas desc al final se ordena en manera descendente

select * from DimGeography
order by 4 asc



select top 10 * from DimGeography
order by 1 desc


-- DISTINCT
select distinct StateProveinceName from DimGeography

select distinct StateProveinceName, PostalCode from DimGeography


-- WHERE
select * from DimGeography
where PostalCode = '95010'



-- OPERADORES
-- AND = Todas las condiciones deben cumplirse
-- OR = Una sola condicion debe cumplirse
-- IN = Multiples valores en una clausula

select * from empleados
where postalcode in ('85225','85233','85201')

-- BETWEEN = entre esos valores
select * from empleados
where geographykey between 100 and 200

