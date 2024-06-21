import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('gestion.db')
cursor = conn.cursor()

# Crear tabla de clientes
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    email TEXT NOT NULL,
    telefono TEXT NOT NULL,
    direccion TEXT NOT NULL
)
''')

# Crear tabla de productos
cursor.execute('''
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    precio REAL,
    stock INTEGER,
    vencimiento TEXT
)
''')

# Crear tabla de pedidos
cursor.execute('''
CREATE TABLE IF NOT EXISTS pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER,
    producto_id INTEGER,
    cantidad INTEGER,
    fecha TEXT,
    hora TEXT,
    FOREIGN KEY(cliente_id) REFERENCES clientes(id),
    FOREIGN KEY(producto_id) REFERENCES productos(id)
)
''')

# Crear tabla de eliminados
cursor.execute('''
CREATE TABLE IF NOT EXISTS eliminados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT,
    elemento_id INTEGER,
    detalle TEXT
)
''')

conn.commit()

def agregar_cliente(nombre, apellido, email, telefono, direccion):
    cursor.execute('''
    INSERT INTO clientes (nombre, apellido, email, telefono, direccion)
    VALUES (?, ?, ?, ?, ?)
    ''', (nombre, apellido, email, telefono, direccion))
    conn.commit()

def ver_clientes():
    cursor.execute('SELECT * FROM clientes')
    return cursor.fetchall()

def eliminar_cliente(cliente_id):
    cliente = buscar_cliente_por_id(cliente_id)
    if cliente:
        cursor.execute('DELETE FROM clientes WHERE id=?', (cliente_id,))
        conn.commit()
        registrar_eliminado('cliente', cliente_id, f'Cliente eliminado: {cliente[1]} {cliente[2]}')

def buscar_cliente_por_id(cliente_id):
    cursor.execute('SELECT * FROM clientes WHERE id=?', (cliente_id,))
    return cursor.fetchone()

def agregar_producto(nombre, descripcion, precio, stock, vencimiento):
    cursor.execute('''
    INSERT INTO productos (nombre, descripcion, precio, stock, vencimiento)
    VALUES (?, ?, ?, ?, ?)
    ''', (nombre, descripcion, precio, stock, vencimiento))
    conn.commit()

def ver_productos():
    cursor.execute('SELECT * FROM productos')
    return cursor.fetchall()

def eliminar_producto(producto_id):
    producto = buscar_producto_por_id(producto_id)
    if producto:
        cursor.execute('DELETE FROM productos WHERE id=?', (producto_id,))
        conn.commit()
        registrar_eliminado('producto', producto_id, f'Producto eliminado: {producto[1]}')

def buscar_producto_por_id(producto_id):
    cursor.execute('SELECT * FROM productos WHERE id=?', (producto_id,))
    return cursor.fetchone()

def agregar_pedido(cliente_id, producto_id, cantidad, fecha, hora):
    cursor.execute('''
    INSERT INTO pedidos (cliente_id, producto_id, cantidad, fecha, hora)
    VALUES (?, ?, ?, ?, ?)
    ''', (cliente_id, producto_id, cantidad, fecha, hora))
    conn.commit()

def ver_pedidos():
    cursor.execute('SELECT * FROM pedidos')
    return cursor.fetchall()

def eliminar_pedido(pedido_id):
    pedido = buscar_pedido_por_id(pedido_id)
    if pedido:
        cursor.execute('DELETE FROM pedidos WHERE id=?', (pedido_id,))
        conn.commit()
        registrar_eliminado('pedido', pedido_id, f'Pedido eliminado: {pedido[0]}')

def buscar_pedido_por_id(pedido_id):
    cursor.execute('SELECT * FROM pedidos WHERE id=?', (pedido_id,))
    return cursor.fetchone()

def registrar_eliminado(tipo, elemento_id, detalle):
    cursor.execute('''
    INSERT INTO eliminados (tipo, elemento_id, detalle)
    VALUES (?, ?, ?)
    ''', (tipo, elemento_id, detalle))
    conn.commit()

def ver_eliminados():
    cursor.execute('SELECT * FROM eliminados')
    return cursor.fetchall()

# Cerrar la conexión con la base de datos al salir
def cerrar_conexion():
    conn.close()

