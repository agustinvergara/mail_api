DROP DATABASE IF EXISTS mail_db;

CREATE DATABASE mail_db;

USE mail_db;

CREATE TABLE Cliente(
    cliente_id INTEGER NOT NULL UNIQUE AUTO_INCREMENT,
    nombre VARCHAR(28),
    apellido VARCHAR(28),
    mail VARCHAR(50) UNIQUE NOT NULL,
    cell CHAR(18),
    mensaje VARCHAR(300),
    PRIMARY KEY (cliente_id)
);

CREATE USER 'dbadmin'@'localhost' IDENTIFIED BY 'Agus0702.';
GRANT ALL PRIVILEGES ON mail_db.* TO 'dbadmin'@'localhost';
FLUSH PRIVILEGES;