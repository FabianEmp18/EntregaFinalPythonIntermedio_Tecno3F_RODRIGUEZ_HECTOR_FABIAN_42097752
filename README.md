RODRÍGUEZ HÉCTOR FABIÁN - 42097752

Estructura de la Base de Datos
El proyecto utiliza una base de datos SQLite con las siguientes tablas y campos:

clientes

id: Identificador único del cliente.
nombre: Nombre del cliente.
apellido: Apellido del cliente.
email: Correo electrónico del cliente.
telefono: Número de teléfono del cliente.
direccion: Dirección del cliente.
productos

id: Identificador único del producto.
nombre: Nombre del producto.
descripcion: Descripción del producto.
precio: Precio del producto.
stock: Cantidad en stock del producto.
vencimiento: Fecha de vencimiento del producto.
pedidos

id: Identificador único del pedido.
cliente_id: Referencia al cliente que realizó el pedido.
producto_id: Referencia al producto pedido.
cantidad: Cantidad de productos solicitados.
fecha: Fecha en que se realizó el pedido.
hora: Hora en que se realizó el pedido.
eliminados

id: Identificador único del elemento eliminado.
tipo: Tipo de elemento eliminado (cliente, producto, pedido).
elemento_id: ID del elemento eliminado.
detalle: Detalle adicional sobre la eliminación.
Funcionalidades
Gestión de Clientes: Agregar, eliminar y visualizar clientes.
Gestión de Productos: Agregar, eliminar y visualizar productos.
Gestión de Pedidos: Registrar, eliminar y visualizar pedidos.
Registro de Eliminados: Mantener un registro de elementos eliminados con detalles sobre la acción.
Requisitos y Ejecución
Clonar el Repositorio

bash
Copiar código
git clone https://github.com/FabianEmp18/EntregaFinalPythonIntermedio_Tecno3F_RODRIGUEZ_HECTOR_FABIAN_42097752.git
cd EntregaFinalPythonIntermedio_Tecno3F_RODRIGUEZ_HECTOR_FABIAN_42097752
Instalar Dependencias

Este proyecto no requiere bibliotecas externas adicionales más allá de las estándar de Python (Tkinter, SQLite3) y DB Browser SQLite para manejar la base de datos
.
Ejecutar la Aplicación
python main.py

Uso de la Aplicación
La interfaz principal muestra pestañas para Clientes, Productos, Pedidos y Elementos Eliminados.
Cada pestaña permite agregar nuevos registros, eliminar registros existentes y visualizar la información actualizada en tablas.