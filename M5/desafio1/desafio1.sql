-- Requerimientos
-- Dentro del video debes ir ejecutando las siguientes acciones y explicar lo que estás
-- haciendo:
-- 1. Comienza a grabar
ok
-- 2. Entra al terminal
ssh jcataldo@192.168.1.253

-- 3. Ingresa al cliente de postgreSQL desde el terminal
psql -U postgres

-- 4. Crea una base de datos llamada desafio-tuNombre-tuApellido-3digitos (2 Puntos)
create database desafio-juan-cataldo-257;
create database desafio_juan_cataldo_257;

-- 5. Ingresa a la base de datos creada. (1 Punto)
\c desafio_juan_cataldo_257

-- 6. Crea una tabla llamada clientes, con una columna llamada email de tipo
-- varchar(50), una columna llamada nombre de tipo varchar sin limitación, una
-- columna llamada teléfono de tipo varchar(16), un campo llamado empresa de
-- tipo varchar(50) y una columna de tipo smallint, para indicar la prioridad del
-- cliente. Ahí se debe ingresar un valor entre 1 y 10, donde 10 es más prioritario.
-- (2 Puntos)
-- Hint: No hay que limitar el valor de la columna de prioridad, como tipo de dato se
-- recomienda ocupar smallint.
create table clientes(email varchar(50), nombre varchar, teléfono varchar(16), empresa varchar(50), prioridad smallint);
\d clientes;

-- 7. Ingresa 5 clientes distintos con distintas prioridades, el resto de los valores los
-- puedes inventar. (1 Punto)
insert into clientes values ('cliente1@mail.com', 'Cliente Uno', '56911111111', 'CTC', 8);
insert into clientes values ('cliente2@mail.com', 'Cliente Dos', '56922222222', 'BELLSOUTH', 6);
insert into clientes values ('cliente3@mail.com', 'Cliente Tres', '56933333333', 'SMARTCOM', 3);
insert into clientes values ('cliente4@mail.com', 'Cliente Cuatro', '56944444444', 'EMOS', 10);
insert into clientes values ('cliente5@mail.com', 'Cliente Cinco', '56955555555', 'METROPOLIS INTERCOM', 2);

-- 8. Selecciona los tres clientes de mayor prioridad. (2 Puntos)
select * from clientes order by prioridad desc limit 3;

-- 9. Selecciona, de la tabla clientes, una prioridad o una empresa, de forma que el
-- resultado devuelva 2 registros. (2 Puntos)
select * from clientes where prioridad = 10 or empresa = 'BELLSOUTH';

-- 10. Sal de postgreSQL
\q