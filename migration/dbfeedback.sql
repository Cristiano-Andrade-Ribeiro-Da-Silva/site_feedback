CREATE DATABASE IF NOT EXISTS db_feedback;
USE db_feedback;
CREATE TABLE IF NOT EXISTS tb_comentarios
(
usuario CHAR(50) NOT NULL,
cod_comentario INT AUTO_INCREMENT PRIMARY KEY,
comentario TEXT NOT NULL,
data_hora DATETIME NOT NULL
);