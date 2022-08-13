CREATE DATABASE PELUPATITAS

USE PELUPATITAS

CREATE TABLE Dueno (
    DNI INT PRIMARY KEY NOT NULL,
    Nombre VARCHAR(25) NOT NULL,
    Apellido VARCHAR(50) NOT NULL,
    Telefono VARCHAR(9),
    Direccion VARCHAR(50) NOT NULL   
);

# Punto 1

CREATE TABLE Perro (
    Id_Perro INT(15) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    Nombre VARCHAR(25) NOT NULL,
    Fecha_nac DATE NOT NULL,
    Sexo ENUM('H', 'M') NOT NULL,
    DNI_dueno INT NOT NULL,
    FOREIGN KEY (DNI_Dueno) REFERENCES Dueno(DNI)
);
 
 CREATE TABLE Historial (
    Id_Historial INT PRIMARY KEY NOT NULL,
    Fecha DATE NOT NULL,
    Perro INT NOT NULL,
    FOREIGN KEY (Perro) REFERENCES perro(Id_Perro),
    Descripcion VARCHAR(100) NOT NULL,
    Monto FLOAT UNSIGNED NOT NULL
);

# Punto 2

# Inserto datos de dueños

INSERT INTO dueno VALUES ('40501304', 'Marisa', 'Murua', '156898514', 'La Marca 301');
INSERT INTO dueno VALUES ('35604904', 'Pedro', 'Rosales', '4879888', '9  de Julio 195');
INSERT INTO dueno VALUES ('14124887', 'Gonzalo', 'Martin','45666877', 'Tres Arroyos 49');
INSERT INTO dueno VALUES ('10256988', 'Roberto', 'Ayala','11258898', 'El faro 321');
INSERT INTO dueno VALUES ('32852655', 'Natalia', 'Ocampos','154877889', 'La paloma 725');
INSERT INTO dueno VALUES ('22987555', 'Jose', 'Martin','351855588', 'Leartes 552');
INSERT INTO dueno VALUES ('25458632', 'Nora', 'Espinoza','4781125', 'Fraternidad 15');

# Inserto datos de perros

INSERT INTO perro VALUES (132,'Diana', '2021-02-15', 'H','40501304');
INSERT INTO perro VALUES (10,'Capi', '2016-05-12', 'M','35604904');
INSERT INTO perro VALUES (32,'Buch', '2016-09-21', 'M','14124887');
INSERT INTO perro VALUES (340,'Nara', '2022-01-21', 'H','10256988');
INSERT INTO perro VALUES (85,'Pola', '2018-06-18', 'H','32852655');
INSERT INTO perro VALUES (05,'Canela', '2015-12-15', 'H','22987555');
INSERT INTO perro VALUES (115,'Manu', '2021-03-15', 'm','25458632');

# Inserto datos del historial

INSERT INTO historial VALUES (1, '2022-07-18', 132, 'Corte Completo', 1800);
INSERT INTO historial VALUES (2, '2021-07-19', 85, 'Baño y Corte', 3000);
INSERT INTO historial VALUES (3, '2018-08-18', 32, 'Corte Completo', 800);
INSERT INTO historial VALUES (4, '2022-04-03', 340, 'Corte básico', 1200);


# ----------- Punto 10 Vaciar la tabla historial y resetear el contador del campo ID.

TRUNCATE historial;