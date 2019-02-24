CREATE DATABASE ria_iniciales;

USE ria_iniciales;

create table clientes(
id_cliente       int(4)      not null primary key auto_increment,
nombre_cliente   varchar(30) not null,
apellido_paterno varchar(20) not null,
apellido_materno varchar(20) not null,
telefono         varchar(10) not null);

create table productos(
id_producto  int(4)      not null primary key auto_increment,
nombre       varchar(30) not null,
marca        varchar(20) not null,
modelo       varchar(20) not null,
cantidad     int(5)      not null);

insert into clientes(nombre_cliente, apellido_paterno, apellido_materno, telefono) values
('pedro', 'hernandez', 'luqueno', '7757253463'),
('abigail', 'nery', 'montes', '7757253858'),
('israel', 'merida', 'lopez', '7757658958');

insert into productos( nombre, marca, modelo, cantidad) values
('gancito', 'gamesa', 'gancito', 6),
('fanta', 'coca-cola', 'fanta', 8),
('papas', 'sabritas', 'sabritas', 5);

CREATE USER 'ria'@'localhost' IDENTIFIED BY 'ria.2019';
GRANT ALL PRIVILEGES ON ria_iniciales.* TO 'ria'@'localhost';
FLUSH PRIVILEGES;
