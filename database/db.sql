drop database proyecto_db;

create database proyecto_db;

use proyecto_db;

create table productos(
 codigo int(9) primary key,
 descripcion varchar(300) not null,
 precio int not null,
 stock int not null,
 categoria varchar(50) not null
);

insert into productos(codigo,descripcion,precio,stock,categoria)
values('000000001','Gaseosa','5','2000','Bebidas'),
      ('000000002','Yogurt','7','3000','Embutido'),
      ('000000003','Desinfectante','10','1500','Limpieza'),
      ('000000004','Cubiertos','20','1000','Hogar'),
      ('000000005','Lejia','7','3000','Limpieza');
