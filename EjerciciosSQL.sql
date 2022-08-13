CREATE DATABASE PELUPATITAS;

USE PELUPATITAS;

CREATE TABLE Dueno (
    DNI INT PRIMARY KEY NOT NULL,
    Nombre VARCHAR(25) NOT NULL,
    Apellido VARCHAR(50) NOT NULL,
    Telefono VARCHAR(15),
    Direccion VARCHAR(50) NOT NULL   
);

# Punto 1

CREATE TABLE Perro (
    Id_Perro INT PRIMARY KEY NOT NULL,
    Nombre VARCHAR(25) NOT NULL,
    Fecha_nac DATE NOT NULL,
    Sexo ENUM('H', 'M') NOT NULL,
    DNI_dueno INT NOT NULL,
    CONSTRAINT DNI_Dueno_fk
    FOREIGN KEY (DNI_dueno) REFERENCES Dueno(DNI)
);
 
 CREATE TABLE Historial (
    Id_Historial INT PRIMARY KEY NOT NULL,
    Fecha DATE NOT NULL,
    Perro INT NOT NULL,
    CONSTRAINT  Perro_fk
    FOREIGN KEY (Perro) REFERENCES perro(Id_Perro),
    Descripcion VARCHAR(100) NOT NULL,
    Monto FLOAT UNSIGNED NOT NULL
);

# ----------- Punto 2

# Inserto datos de dueños

INSERT INTO dueno VALUES ('40501304', 'Marisa', 'Murua', '156898514', 'La Marca 301');
INSERT INTO dueno VALUES ('35604904', 'Pedro', 'Rosales', '4879888', '9  de Julio 195');
INSERT INTO dueno VALUES ('14124887', 'Gonzalo', 'Martin','45666877', 'Tres Arroyos 49');
INSERT INTO dueno VALUES ('10256988', 'Roberto', 'Ayala','11258898', 'El faro 321');
INSERT INTO dueno VALUES ('32852655', 'Natalia', 'Ocampos','154877889', 'La paloma 725');
INSERT INTO dueno VALUES ('22987555', 'Jose', 'Martin','351855588', 'Leartes 552');
INSERT INTO dueno VALUES ('79503962', 'Luisa', 'Del Valle','null', 'Jacinto Rios 150');

# Inserto datos de perros

INSERT INTO perro VALUES (132,'Diana', '2021-02-15', 'H','40501304');
INSERT INTO perro VALUES (12,'Capi', '2016-05-12', 'M','35604904');
INSERT INTO perro VALUES (32,'Buch', '2016-09-21', 'M','14124887');
INSERT INTO perro VALUES (340,'Nara', '2022-01-21', 'H','10256988');
INSERT INTO perro VALUES (85,'Pola', '2018-06-18', 'H','32852655');
INSERT INTO perro VALUES (05,'Canela', '2015-12-15', 'H','22987555');



# Inserto datos del historial

INSERT INTO historial VALUES (1, '2022-07-18', 132, 'Corte Completo', 1800);
INSERT INTO historial VALUES (2, '2021-07-19', 85, 'Baño y Corte', 3000);
INSERT INTO historial VALUES (3, '2018-08-18', 32, 'Corte Completo', 800);
INSERT INTO historial VALUES (4, '2022-04-03', 340, 'Corte básico', 1200);


# ----------- Punto 3 Borre un animal que ya no va a ser atendido. Para ello consulte antes en el historial, algún animal que ya no sea atendido desde hace mucho tiempo.

SELECT * FROM historial
ORDER BY Fecha;
DELETE FROM historial
WHERE Perro=32;
DELETE FROM perro
WHERE ID_Perro=32;

# ----------- Punto 4 Actualice la fecha de nacimiento de algún animal (perro) que usted considere.

UPDATE PERRO 
set Fecha_nac='2020-03-25' 
where Nombre='Diana';
SELECT * FROM PERRO;


# ----------- Punto 5 Realice una consulta multitabla que arroje el nombre de todos los perros cuyos dueños se llaman Pedro

SELECT 
p.Nombre AS Perro,
p.Fecha_nac AS FechaNacimiento,
p.Sexo,
d.DNI AS DniDueno,
CONCAT(d.Apellido, ', ', d.Nombre) AS Dueno
FROM
perro p
INNER JOIN
dueno d ON d.DNI = p.DNI_dueno
WHERE
d.nombre LIKE '%Pedro%';

# ----------- Punto 6 Obtener todos los perros que asistieron a la peluquería en 2022

SELECT Fecha, perro 
FROM historial 
WHERE Fecha >= '2022-01-01';


# ----------- Punto 7 Obtener los ingresos percibidos en Julio del 2022

SELECT Monto
FROM historial
WHERE Fecha between '2022-07-01' and '2022-07-31';


# ----------- Punto 8 Insertar un nuevo registro en la tabla historial de un perro cuyo ID Perro es igual a 10.

INSERT INTO perro VALUES (10,'Roco', '2020-04-22', 'M','79503962');
INSERT INTO historial VALUES (11, '2020-04-22', 10, 'Corte completo', 3000);


# ----------- Punto 9  Escriba una consulta que permita actualizar la dirección de un dueño. Su nueva dirección es Libertad 123

UPDATE dueno 
SET 
Direccion = 'Libertad 123'
WHERE
DNI = 35604904;

SELECT * 
FROM dueno 
WHERE DNI = 35604904;

# ----------- Punto 10 Vaciar la tabla historial y resetear el contador del campo ID.

TRUNCATE historial;


# ----------- Punto 11 Obtener todos los dueños que tengan perros de menos de 5 años de edad que no hayan visitado la peluquería en el año 2022.


SELECT 
p.Nombre AS Perro,
(YEAR(CURDATE()) - YEAR(p.Fecha_nac)) AS EdadPerro,
CONCAT(d.Apellido, ' ', d.Nombre) AS Dueno,
h.Fecha as FechaDeVisita
FROM
historial h
INNER JOIN
perro p ON p.Id_Perro = h.perro
INNER JOIN
dueno d ON d.DNI = p.DNI_dueno
WHERE
h.Fecha NOT BETWEEN '20220101' AND '20221231'
AND (YEAR(CURDATE()) - YEAR(p.Fecha_nac)) < 5;


# ----------- Punto 12 Obtener todos los perros de sexo “Macho” nacidos entre 2020 y 2022.

SELECT * 
FROM perro
WHERE Sexo ='M'
AND Fecha_nac BETWEEN '2020-01-01' AND '2022-12-31';
