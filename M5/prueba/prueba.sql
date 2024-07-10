
/* Prueba - Fundamentos de bases de datos relacionales 

1. Crea el modelo (revisa bien cuál es el tipo de relación antes de crearlo), respeta las claves primarias, foráneas y tipos de datos. 
(1 punto)  */

create database prueba_sql ;
\c prueba_sql
create table peliculas(id serial primary key, nombre varchar(255), anno integer);
create table tags(id serial primary key, tag varchar(32));
create table peliculas_tag(peliculas_id integer references peliculas(id), tags_id integer references tags(id));

/* 2. Inserta 5 películas y 5 tags, la primera película tiene que tener 3 tags asociados, la segunda película debe tener dos tags asociados. 
(1 punto)  */

insert into peliculas (nombre, anno) values ('The Lord of the Rings : The Fellowship of the Ring', 2001);
insert into peliculas (nombre, anno) values ('The Matrix', 1999);
insert into peliculas (nombre, anno) values ('The Terminator', 1984);
insert into peliculas (nombre, anno) values ('Das Boot', 1981 );
insert into peliculas (nombre, anno) values ('Me, Myself & Irene', 2000);

insert into tags (tag) values ('Sci-Fi');
insert into tags (tag) values ('Fantasy');
insert into tags (tag) values ('Action');
insert into tags (tag) values ('Adventure');
insert into tags (tag) values ('Comedy');

insert into peliculas_tag values (1, 2);
insert into peliculas_tag values (1, 3);
insert into peliculas_tag values (1, 3);
insert into peliculas_tag values (2, 1);
insert into peliculas_tag values (2, 3);

/* 3. Cuenta la cantidad de tags que tiene cada película. Si una película no tiene tags debe mostrar 0. 
(1 punto)  */
select p.nombre, count(pt.peliculas_id) as tags_cantidad
from peliculas as p 
left join peliculas_tag as pt 
    on p.id = pt.peliculas_id
group by p.nombre
order by tags_cantidad desc;

/* Dado el siguiente modelo: 
4. Crea las tablas respetando los nombres, tipos, claves primarias y foráneas y tipos de datos. (1 punto) */
create table preguntas(id serial primary key, pregunta varchar(255), respuesta_correcta varchar);
create table usuarios(id serial primary key, nombre varchar(255), edad integer);
create table respuestas(id serial primary key, respuesta varchar(255), usuario_id integer references usuarios(id), pregunta_id integer references preguntas(id));

/* 5. Agrega 5 registros a la tabla preguntas, de los cuales: (1 punto) 
a. 1. La primera pregunta debe ser contestada correctamente por dos usuarios distintos 
b. 2. La pregunta 2 debe ser contestada correctamente por un usuario. c. 3. Los otros dos registros deben ser respuestas incorrectas. 
Hint: Contestada correctamente significa que la respuesta indicada en la tabla respuestas es exactamente igual al texto indicado en la tabla de preguntas. 
 */

insert into usuarios (nombre, edad) values ('Valentina', 23);
insert into usuarios (nombre, edad) values ('Pedro', 19);
insert into usuarios (nombre, edad) values ('Andrea', 20);

insert into preguntas (pregunta, respuesta_correcta) values ('¿Cuál es la capital de Escocia?', 'Edimburgo');
insert into preguntas (pregunta, respuesta_correcta) values ('¿Cuál es la capital de Canada?', 'Ottawa');
insert into preguntas (pregunta, respuesta_correcta) values ('¿Cuál es la capital de Italia?', 'Roma');
insert into preguntas (pregunta, respuesta_correcta) values ('¿Cuál es la capital de China?', 'Pekin');
insert into preguntas (pregunta, respuesta_correcta) values ('¿Cuál es la capital de Brasil?', 'Brasilia');

insert into respuestas (respuesta, usuario_id, pregunta_id) values ('Edimburgo', 1, 1);
insert into respuestas (respuesta, usuario_id, pregunta_id) values ('Edimburgo', 3, 1);
insert into respuestas (respuesta, usuario_id, pregunta_id) values ('Ottawa', 3, 2);
insert into respuestas (respuesta, usuario_id, pregunta_id) values ('Milan', 2, 3);
insert into respuestas (respuesta, usuario_id, pregunta_id) values ('Hong Kong', 1, 4);
insert into respuestas (respuesta, usuario_id, pregunta_id) values ('Sao Paulo', 1, 5);

/* 6. Cuenta la cantidad de respuestas correctas totales por usuario (independiente de la pregunta). (1 punto) 
 */

select u.nombre, count(p.respuesta_correcta) as correctas
from preguntas as p
left join respuestas as r
    on p.id = r.pregunta_id 
left join usuarios as u
    on r.usuario_id = u.id 
where p.respuesta_correcta = r.respuesta
group by u.nombre ;

/* 7. Por cada pregunta, en la tabla preguntas, cuenta cuántos usuarios tuvieron la respuesta correcta. (1 punto) 
 */

select p.pregunta, count(u.nombre) as correctas
from preguntas as p
left join respuestas as r
    on p.id = r.pregunta_id 
left join usuarios as u
    on r.usuario_id = u.id 
where p.respuesta_correcta = r.respuesta
group by p.pregunta ;


/* 8. Implementa borrado en cascada de las respuestas al borrar un usuario y borrar el primer usuario para probar la implementación. (1 punto) 
 */

alter table respuestas
drop constraint respuestas_usuario_id_fkey,
add constraint respuestas_usuario_id_fkey 
    foreign key (usuario_id) 
    references usuarios(id) 
    on delete cascade;

\d respuestas

select *
from respuestas
left join usuarios
    on respuestas.usuario_id = usuarios.id;

delete from usuarios where nombre = 'Valentina';

select *
from respuestas
left join usuarios
    on respuestas.usuario_id = usuarios.id;

/* 9. Crea una restricción que impida insertar usuarios menores de 18 años en la base de datos. (1 punto) 
 */

alter table usuarios
add check (edad>=18); 

\d usuarios

/* 10. Altera la tabla existente de usuarios agregando el campo email con la restricción de único. (1 punto) 
 */

alter table usuarios
add email varchar(255) unique;

\d usuarios