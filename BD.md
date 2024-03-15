 create database panne;
 use panne;
 
INSERT INTO home_roles (rol) VALUES ('Administrador');
INSERT INTO home_roles (rol) VALUES ('Vendedor');


INSERT INTO home_usuario (email, contraseña, idRol_id) VALUES ('admin@example.com', 'admin123', 1);
INSERT INTO home_usuario (email, contraseña, idRol_id) VALUES ('usuario1@example.com', 'usuario123', 2);



GRANT SELECT, INSERT, UPDATE, DELETE ON home_venta TO Administrador;
GRANT SELECT, INSERT, UPDATE, DELETE ON home_stock TO Administrador;
GRANT SELECT, INSERT, UPDATE, DELETE ON home_pqrs TO Administrador;
GRANT SELECT, INSERT, UPDATE, DELETE ON home_ventaproducto TO Administrador;


-- Asignar permisos al Vendedor
GRANT SELECT, INSERT, UPDATE, DELETE ON home_venta TO Vendedor;
