CREATE DATABASE IF NOT EXISTS db_feedback;
USE db_feedback;


CREATE TABLE IF NOT EXISTS tb_comentarios
(
cod_comentario INT AUTO_INCREMENT PRIMARY KEY,
nome CHAR(50) NOT NULL,
comentario TEXT NOT NULL,
data_hora DATETIME NOT NULL,
curtidas INT default 0
);


CREATE TABLE IF NOT EXISTS tb_usuarios
(
login VARCHAR(50) NOT NULL PRIMARY KEY,
nome VARCHAR(50) NOT NULL,
senha VARCHAR(150) NOT NULL
);

SELECT cod_comentario, nome, comentario, data_hora, curtidas FROM tb_comentarios;
SELECT login, nome, senha FROM tb_usuarios;