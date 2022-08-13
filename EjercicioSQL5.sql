use pelupatitas

CREATE TABLE Dueno (
    DNI INT PRIMARY KEY NOT NULL,
    Nombre VARCHAR(25) NOT NULL,
    Apellido VARCHAR(50) NOT NULL,
    Telefono VARCHAR(9)
    Direccion VARCHAR(50) NOT NULL,   
);

# Punto 1

CREATE TABLE Perro (
    Id_Perro INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    Nombre VARCHAR(25) NOT NULL,
    Fecha_nac DATE NOT NULL,
    Sexo ENUM('H', 'M') NOT NULL,
    DNI_dueno INT NOT NULL,
    FOREIGN KEY (DNI_dueno) REFERENCES dueno(DNI)
);
 
 CREATE TABLE Historial (
    Id_Historial INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    Fecha DATE NOT NULL,
    Perro INT NOT NULL,
    FOREIGN KEY (perro) REFERENCES perro(id_perro),
    Descripcion VARCHAR(100) NOT NULL,
    Monto FLOAT UNSIGNED NOT NULL
);

# Punto 2

INSERT INTO dueno VALUES ('40501304', 'Marisa', 'Murua', '156898514', 'La Marca 301');
INSERT INTO dueno VALUES ('35604904', 'Jose', 'Rosales', '4879888' , '9  de Julio 195');
INSERT INTO dueno VALUES ('14124887', 'Gonzalo', 'Martin','45666877', 'Tres Arroyos 49');
 
/* perro */
INSERT INTO perro VALUES (1256,'Diana', '2021-02-15', 'M','40501304');
INSERT INTO perro VALUES (1685,'Capi', '2020-05-12', 'H','35604904');
INSERT INTO perro VALUES (1722,'Buch', '2016-09-21', 'H','40501304');


/* historial */
INSERT INTO historial VALUES (1, '2022-01-15', 1256, 'Corte Completo', 1800);
INSERT INTO historial VALUES (2, '2021-07-19', 1722, 'Baño y Corte', 3000);
INSERT INTO historial VALUES (3, '2016-06-03', 1685, 'Corte Completo', 1800);


# Punto 5 Realice una consulta multitabla que arroje el nombre de todos los perros cuyos dueños se llaman Pedro*/

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
    d.nombre LIKE '%Pedro%'