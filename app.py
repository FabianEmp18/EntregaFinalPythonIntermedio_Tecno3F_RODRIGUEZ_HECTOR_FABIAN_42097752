import tkinter as tk
from tkinter import messagebox, ttk
import database

def mostrar_clientes():
    clientes = database.ver_clientes()
    lista_clientes.delete(*lista_clientes.get_children())
    for cliente in clientes:
        lista_clientes.insert("", "end", values=cliente)

def mostrar_productos():
    productos = database.ver_productos()
    lista_productos.delete(*lista_productos.get_children())
    for producto in productos:
        lista_productos.insert("", "end", values=producto)

def mostrar_pedidos():
    pedidos = database.ver_pedidos()
    lista_pedidos.delete(*lista_pedidos.get_children())
    for pedido in pedidos:
        lista_pedidos.insert("", "end", values=pedido)

def mostrar_eliminados():
    eliminados = database.ver_eliminados()
    lista_eliminados.delete(*lista_eliminados.get_children())
    for eliminado in eliminados:
        lista_eliminados.insert("", "end", values=eliminado)

def agregar_cliente_gui():
    nombre = entry_cliente_nombre.get()
    apellido = entry_cliente_apellido.get()
    email = entry_cliente_email.get()
    telefono = entry_cliente_telefono.get()
    direccion = entry_cliente_direccion.get()
    database.agregar_cliente(nombre, apellido, email, telefono, direccion)
    mostrar_clientes()

def eliminar_cliente_gui():
    seleccion = lista_clientes.selection()
    if seleccion:
        cliente_id = lista_clientes.item(seleccion)["values"][0]
        database.eliminar_cliente(cliente_id)
        mostrar_clientes()
        mostrar_eliminados()  # Actualiza la lista de eliminados
    else:
        messagebox.showwarning("Advertencia", "Seleccione un cliente para eliminar.")

def agregar_producto_gui():
    nombre = entry_producto_nombre.get()
    descripcion = entry_producto_descripcion.get()
    precio = entry_producto_precio.get()
    stock = entry_producto_stock.get()
    vencimiento = entry_producto_vencimiento.get()  # Capturar el vencimiento
    database.agregar_producto(nombre, descripcion, precio, stock, vencimiento)
    mostrar_productos()

def eliminar_producto_gui():
    seleccion = lista_productos.selection()
    if seleccion:
        producto_id = lista_productos.item(seleccion)["values"][0]
        database.eliminar_producto(producto_id)
        mostrar_productos()
        mostrar_eliminados()  
    else:
        messagebox.showwarning("Advertencia", "Seleccione un producto para eliminar.")

def agregar_pedido_gui():
    cliente_id = entry_pedido_cliente_id.get()
    producto_id = entry_pedido_producto_id.get()
    cantidad = entry_pedido_cantidad.get()
    fecha = entry_pedido_fecha.get()
    hora = entry_pedido_hora.get()  # Capturar la hora
    database.agregar_pedido(cliente_id, producto_id, cantidad, fecha, hora)
    mostrar_pedidos()

def eliminar_pedido_gui():
    seleccion = lista_pedidos.selection()
    if seleccion:
        pedido_id = lista_pedidos.item(seleccion)["values"][0]
        database.eliminar_pedido(pedido_id)
        mostrar_pedidos()
        mostrar_eliminados()  
    else:
        messagebox.showwarning("Advertencia", "Seleccione un pedido para eliminar.")

def maximizar_ventana():
    ventana.state('zoomed')  

ventana = tk.Tk()
ventana.title("Gestión de Clientes, Productos y Pedidos")

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview.Heading", font=("Helvetica", 10, "bold"), background="lightblue")
style.configure("Treeview", font=("Helvetica", 10), rowheight=25)
style.map("Treeview", background=[("selected", "blue")], foreground=[("selected", "white")])

tab_control = ttk.Notebook(ventana)

tab_clientes = ttk.Frame(tab_control)
tab_control.add(tab_clientes, text='Clientes')

frame_cliente_form = tk.Frame(tab_clientes, bg="lightgrey", pady=10, padx=10)
frame_cliente_form.pack(pady=10, fill="x")

tk.Label(frame_cliente_form, text="Nombre", bg="lightgrey").grid(row=0, column=0, padx=10, pady=5, sticky="e")
tk.Label(frame_cliente_form, text="Apellido", bg="lightgrey").grid(row=1, column=0, padx=10, pady=5, sticky="e")
tk.Label(frame_cliente_form, text="Email", bg="lightgrey").grid(row=2, column=0, padx=10, pady=5, sticky="e")
tk.Label(frame_cliente_form, text="Teléfono", bg="lightgrey").grid(row=3, column=0, padx=10, pady=5, sticky="e")
tk.Label(frame_cliente_form, text="Dirección", bg="lightgrey").grid(row=4, column=0, padx=10, pady=5, sticky="e")

entry_cliente_nombre = tk.Entry(frame_cliente_form)
entry_cliente_nombre.grid(row=0, column=1, padx=10, pady=5)
entry_cliente_apellido = tk.Entry(frame_cliente_form)
entry_cliente_apellido.grid(row=1, column=1, padx=10, pady=5)
entry_cliente_email = tk.Entry(frame_cliente_form)
entry_cliente_email.grid(row=2, column=1, padx=10, pady=5)
entry_cliente_telefono = tk.Entry(frame_cliente_form)
entry_cliente_telefono.grid(row=3, column=1, padx=10, pady=5)
entry_cliente_direccion = tk.Entry(frame_cliente_form)
entry_cliente_direccion.grid(row=4, column=1, padx=10, pady=5)

btn_agregar_cliente = tk.Button(frame_cliente_form, text="Agregar Cliente", command=agregar_cliente_gui, bg="green", fg="white")
btn_agregar_cliente.grid(row=5, column=0, pady=10, padx=10)
btn_eliminar_cliente = tk.Button(frame_cliente_form, text="Eliminar Cliente", command=eliminar_cliente_gui, bg="red", fg="white")
btn_eliminar_cliente.grid(row=5, column=1, pady=10, padx=10)

frame_cliente_lista = tk.Frame(tab_clientes)
frame_cliente_lista.pack(pady=10, fill="both", expand=True)

cols_cliente = ("ID", "Nombre", "Apellido", "Email", "Teléfono", "Dirección")
lista_clientes = ttk.Treeview(frame_cliente_lista, columns=cols_cliente, show="headings")

for col in cols_cliente:
    lista_clientes.heading(col, text=col)

lista_clientes.pack(fill="both", expand=True)

tab_productos = ttk.Frame(tab_control)
tab_control.add(tab_productos, text='Productos')

frame_producto_form = tk.Frame(tab_productos, bg="lightgrey", pady=10, padx=10)
frame_producto_form.pack(pady=10, fill="x")

tk.Label(frame_producto_form, text="Nombre", bg="lightgrey").grid(row=0, column=0, padx=10, pady=5, sticky="e")
tk.Label(frame_producto_form, text="Descripción", bg="lightgrey").grid(row=1, column=0, padx=10, pady=5, sticky="e")
tk.Label(frame_producto_form, text="Precio", bg="lightgrey").grid(row=2, column=0, padx=10, pady=5, sticky="e")
tk.Label(frame_producto_form, text="Stock", bg="lightgrey").grid(row=3, column=0, padx=10, pady=5, sticky="e")
tk.Label(frame_producto_form, text="Vencimiento", bg="lightgrey").grid(row=4, column=0, padx=10, pady=5, sticky="e")

entry_producto_nombre = tk.Entry(frame_producto_form)
entry_producto_nombre.grid(row=0, column=1, padx=10, pady=5)
entry_producto_descripcion = tk.Entry(frame_producto_form)
entry_producto_descripcion.grid(row=1, column=1, padx=10, pady=5)
entry_producto_precio = tk.Entry(frame_producto_form)
entry_producto_precio.grid(row=2, column=1, padx=10, pady=5)
entry_producto_stock = tk.Entry(frame_producto_form)
entry_producto_stock.grid(row=3, column=1, padx=10, pady=5)
entry_producto_vencimiento = tk.Entry(frame_producto_form)  
entry_producto_vencimiento.grid(row=4, column=1, padx=10, pady=5)

btn_agregar_producto = tk.Button(frame_producto_form, text="Agregar Producto", command=agregar_producto_gui, bg="green", fg="white")
btn_agregar_producto.grid(row=5, column=0, pady=10, padx=10)
btn_eliminar_producto = tk.Button(frame_producto_form, text="Eliminar Producto", command=eliminar_producto_gui, bg="red", fg="white")
btn_eliminar_producto.grid(row=5, column=1, pady=10, padx=10)

frame_producto_lista = tk.Frame(tab_productos)
frame_producto_lista.pack(pady=10, fill="both", expand=True)

cols_producto = ("ID", "Nombre", "Descripción", "Precio", "Stock", "Vencimiento")
lista_productos = ttk.Treeview(frame_producto_lista, columns=cols_producto, show="headings")

for col in cols_producto:
    lista_productos.heading(col, text=col)

lista_productos.pack(fill="both", expand=True)

tab_pedidos = ttk.Frame(tab_control)
tab_control.add(tab_pedidos, text='Pedidos')

frame_pedido_form = tk.Frame(tab_pedidos, bg="lightgrey", pady=10, padx=10)
frame_pedido_form.pack(pady=10, fill="x")

tk.Label(frame_pedido_form, text="ID Cliente", bg="lightgrey").grid(row=0, column=0, padx=10, pady=5, sticky="e")
tk.Label(frame_pedido_form, text="ID Producto", bg="lightgrey").grid(row=1, column=0, padx=10, pady=5, sticky="e")
tk.Label(frame_pedido_form, text="Cantidad", bg="lightgrey").grid(row=2, column=0, padx=10, pady=5, sticky="e")
tk.Label(frame_pedido_form, text="Fecha", bg="lightgrey").grid(row=3, column=0, padx=10, pady=5, sticky="e")
tk.Label(frame_pedido_form, text="Hora", bg="lightgrey").grid(row=4, column=0, padx=10, pady=5, sticky="e")

entry_pedido_cliente_id = tk.Entry(frame_pedido_form)
entry_pedido_cliente_id.grid(row=0, column=1, padx=10, pady=5)
entry_pedido_producto_id = tk.Entry(frame_pedido_form)
entry_pedido_producto_id.grid(row=1, column=1, padx=10, pady=5)
entry_pedido_cantidad = tk.Entry(frame_pedido_form)
entry_pedido_cantidad.grid(row=2, column=1, padx=10, pady=5)
entry_pedido_fecha = tk.Entry(frame_pedido_form)
entry_pedido_fecha.grid(row=3, column=1, padx=10, pady=5)
entry_pedido_hora = tk.Entry(frame_pedido_form)  # Nuevo campo para hora
entry_pedido_hora.grid(row=4, column=1, padx=10, pady=5)

btn_agregar_pedido = tk.Button(frame_pedido_form, text="Agregar Pedido", command=agregar_pedido_gui, bg="green", fg="white")
btn_agregar_pedido.grid(row=5, column=0, pady=10, padx=10)
btn_eliminar_pedido = tk.Button(frame_pedido_form, text="Eliminar Pedido", command=eliminar_pedido_gui, bg="red", fg="white")
btn_eliminar_pedido.grid(row=5, column=1, pady=10, padx=10)

frame_pedido_lista = tk.Frame(tab_pedidos)
frame_pedido_lista.pack(pady=10, fill="both", expand=True)

cols_pedido = ("ID", "ID Cliente", "ID Producto", "Cantidad", "Fecha", "Hora")
lista_pedidos = ttk.Treeview(frame_pedido_lista, columns=cols_pedido, show="headings")

for col in cols_pedido:
    lista_pedidos.heading(col, text=col)

lista_pedidos.pack(fill="both", expand=True)

tab_eliminados = ttk.Frame(tab_control)
tab_control.add(tab_eliminados, text='Eliminados')

frame_eliminados_lista = tk.Frame(tab_eliminados)
frame_eliminados_lista.pack(pady=10, fill="both", expand=True)

cols_eliminados = ("ID", "Tipo", "Elemento ID", "Detalle")
lista_eliminados = ttk.Treeview(frame_eliminados_lista, columns=cols_eliminados, show="headings")

for col in cols_eliminados:
    lista_eliminados.heading(col, text=col)

lista_eliminados.pack(fill="both", expand=True)

tab_control.pack(expand=1, fill='both')

# Función para centrar la ventana en la pantalla
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'+{x}+{y}')
    window.deiconify()  

# Maximizar la ventana
maximizar_ventana()

# Centrar la ventana en la pantalla
center_window(ventana)

mostrar_clientes()
mostrar_productos()
mostrar_pedidos()
mostrar_eliminados()

ventana.mainloop()
