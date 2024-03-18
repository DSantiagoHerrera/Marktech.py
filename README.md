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
 
 
 
 -- Inserciones para la tabla Producto
INSERT INTO home_producto (codigo, nombre, precio, stock) VALUES
('PAN001', 'Pan de maíz', 1500, 50),
('PAN002', 'Pan de yuca', 2000, 40),
('PAN003', 'Bollo de queso', 1800, 30),
('PAN004', 'Almojábana', 1200, 60),
('PAN005', 'Rosca de arequipe', 2500, 20),
('PAN006', 'Pandebono', 1700, 35),
('PAN007', 'Palito de queso', 1600, 45),
('PAN008', 'Pastel de pollo', 3000, 25),
('PAN009', 'Galletas de avena', 2000, 55),
('PAN010', 'Buñuelos', 2200, 30),
('PAN011', 'Muffin de chocolate', 2800, 40),
('PAN012', 'Empanada de carne', 1800, 50),
('PAN013', 'Ponqué de naranja', 3500, 15),
('PAN014', 'Pan integral', 1800, 35),
('PAN015', 'Torta de zanahoria', 4000, 20),
('PAN016', 'Torta de chocolate', 4500, 25),
('PAN017', 'Croissant', 2000, 30),
('PAN018', 'Pan de banano', 2300, 40),
('PAN019', 'Rosquillas', 1600, 50),
('PAN020', 'Pastel de tres leches', 3800, 20);

-- Inserciones para la tabla Stock
INSERT INTO home_stock (producto_codigo, cantidad, fecha) VALUES
('PAN001', 50, NOW()),
('PAN002', 40, NOW()),
('PAN003', 30, NOW()),
('PAN004', 60, NOW()),
('PAN005', 20, NOW()),
('PAN006', 35, NOW()),
('PAN007', 45, NOW()),
('PAN008', 25, NOW()),
('PAN009', 55, NOW()),
('PAN010', 30, NOW()),
('PAN011', 40, NOW()),
('PAN012', 50, NOW()),
('PAN013', 15, NOW()),
('PAN014', 35, NOW()),
('PAN015', 20, NOW()),
('PAN016', 25, NOW()),
('PAN017', 30, NOW()),
('PAN018', 40, NOW()),
('PAN019', 50, NOW()),
('PAN020', 20, NOW());

-- Inserciones para la tabla Pqrs
INSERT INTO home_pqrs (nombre, correo, telefono, tipoPqrs, mensaje, fecha, estado) VALUES
('Juan Pérez', 'juan@example.com', 3101234567, 'Sugerencia', 'Me gustaría que ofrecieran más variedad de panes integrales.', NOW(), 'Pendiente'),
('María Gómez', 'maria@example.com', 3157654321, 'Reclamo', 'El pan que compré estaba un poco duro.', NOW(), 'Pendiente'),
('Carlos Rodríguez', 'carlos@example.com', 3009876543, 'Consulta', '¿Tienen servicio a domicilio?', NOW(), 'Pendiente'),
('Laura Martínez', 'laura@example.com', 3206543210, 'Felicitación', 'Excelente atención al cliente.', NOW(), 'Pendiente'),
('Andrés Herrera', 'andres@example.com', 3012345678, 'Reclamo', 'El pedido llegó incompleto.', NOW(), 'Pendiente'),
('Ana Ramírez', 'ana@example.com', 3188765432, 'Solicitud', 'Quisiera saber si hacen panes sin gluten.', NOW(), 'Pendiente'),
('Luisa Sánchez', 'luisa@example.com', 3056789012, 'Sugerencia', 'Sería genial que incluyeran más opciones vegetarianas.', NOW(), 'Pendiente'),
('Jorge González', 'jorge@example.com', 3001234567, 'Reclamo', 'El pan tenía un sabor extraño.', NOW(), 'Pendiente'),
('Camila Díaz', 'camila@example.com', 3176543210, 'Consulta', '¿Hacen reservas para eventos?', NOW(), 'Pendiente'),
('Felipe Muñoz', 'felipe@example.com', 3109876543, 'Felicitación', 'Me encantó el nuevo pan de banano.', NOW(), 'Pendiente');

-- Inserciones para la tabla Venta
INSERT INTO home_venta (total_venta, fecha) VALUES
(35000, NOW()),
(28000, NOW()),
(42000, NOW()),
(51000, NOW()),
(38000, NOW()),
(45000, NOW()),
(33000, NOW()),
(29000, NOW()),
(50000, NOW()),
(36000, NOW()),
(48000, NOW()),
(39000, NOW()),
(41000, NOW()),
(27000, NOW()),
(44000, NOW()),
(37000, NOW()),
(32000, NOW()),
(43000, NOW()),
(40000, NOW()),
(47000, NOW());

-- Inserciones para la tabla DetalleVenta
INSERT INTO home_detalleventa (cantidad, producto_id, venta_id) VALUES
(2, 1, 1),
(3, 4, 2),
(1, 7, 3),
(4, 9, 4),
(2, 13, 5),
(3, 16, 6),
(1, 19, 7),
(4, 2, 8),
(2, 5, 9),
(3, 8, 10),
(1, 11, 11),
(4, 14, 12),
(2, 17, 13),
(3, 20, 14),
(1, 3, 15),
(4, 6, 16),
(2, 12, 17),
(3, 15, 18),
(1, 18, 19),
(4, 1, 20);

-- Inserciones para la tabla VentaProducto
INSERT INTO home_ventaproducto (venta_id, producto_id, cantidad) VALUES
(1, 'PAN001', 2),
(2, 'PAN004', 3),
(3, 'PAN007', 1),
(4, 'PAN009', 4),
(5, 'PAN013', 2),
(6, 'PAN016', 3),
(7, 'PAN019', 1),
(8, 'PAN002', 4),
(9, 'PAN005', 2),
(10, 'PAN008', 3),
(11, 'PAN011', 1),
(12, 'PAN014', 4),
(13, 'PAN017', 2),
(14, 'PAN020', 3),
(15, 'PAN003', 1),
(16, 'PAN006', 4),
(17, 'PAN012', 2),
(18, 'PAN015', 3),
(19, 'PAN018', 1),
(20, 'PAN001', 4);
