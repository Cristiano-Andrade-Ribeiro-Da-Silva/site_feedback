CREATE DATABASE IF NOT EXISTS db_feedback;
USE db_feedback;

CREATE TABLE IF NOT EXISTS tb_comentarios
(
cod_comentario INT AUTO_INCREMENT PRIMARY KEY,
usuario CHAR(50) NOT NULL,
comentario TEXT NOT NULL,
data_comentario DATETIME NOT NULL
);

SELECT usuario, comentario, data_comentario FROM tb_comentarios;