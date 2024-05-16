-- 1. Crear una base de datos llamada películas.(1 Punto)
create database peliculas;
\c peliculas
create table peliculas (id serial not null primary key, Pelicula varchar(60), Año_estreno integer, Director varchar(30));
create table reparto (id_pelicula integer references peliculas(id), actor varchar(30));

-- 2. Cargar ambos archivos a su tabla correspondiente. (1 Punto)
COPY peliculas(id, Pelicula, Año_estreno, Director) FROM '/exchange/desafio3/peliculas.csv' DELIMITER ',' CSV HEADER;
COPY reparto(id_pelicula, actor) FROM '/exchange/desafio3/reparto.csv' DELIMITER ',' CSV HEADER;

-- 3. Obtener el ID de la película “Titanic”. (1 Punto)
select id from peliculas where Pelicula = 'Titanic';

-- 4. Listar a todos los actores que aparecen en la película "Titanic". (1 Punto)
select actor from reparto where id = 2;

-- 5. Consultar en cuántas películas del top 100 participa Harrison Ford. (2 Puntos)
select id, pelicula, año_estreno, director, actor
from peliculas
inner join reparto on reparto.id_pelicula=peliculas.id
where reparto.actor = 'Harrison Ford';

-- 6. Indicar las películas estrenadas entre los años 1990 y 1999 ordenadas por título de
-- manera ascendente. (1 punto)
select * from peliculas where Año_estreno between 1990 and 1999 order by Pelicula asc;
-- 7. Hacer una consulta SQL que muestre los títulos con su longitud, la longitud debe ser
-- nombrado para la consulta como “longitud_titulo”. (1 punto)
select pelicula, length(pelicula) as longitud_titulo from peliculas;
-- 8. Consultar cual es la longitud más grande entre todos los títulos de las películas. (2 punto)
select max(longitud_titulo), pelicula
from (
    select pelicula, length(pelicula) as longitud_titulo from peliculas
    )
group by pelicula
order by max desc
limit 1;