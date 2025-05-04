import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
from plyer import notification

# Función para actualizar las notificaciones de las tareas
def check_deadlines(tareas):
    for tarea in tareas:
        fecha_entrega = datetime.strptime(tarea['fecha_entrega'], '%d/%m/%y')
        if fecha_entrega - datetime.now() <= timedelta(days=2) and not tarea['hecha']:
            notification.notify(
                title="Tarea cercana",
                message=f"La tarea '{tarea['nombre']}' se vence en menos de 2 días.",
                timeout=10
            )

# Función para cambiar el estado de las tareas
def marcar_como_hecha(tarea):
    tarea['hecha'] = True
    tarea['label_status'].config(text="Entregada", bg="green")

# Función para agregar una tarea
def agregar_tarea(tarea_nombre, tarea_fecha, tareas, frame):
    # Validar que los campos no estén vacíos
    if tarea_nombre == "" or tarea_fecha == "":
        messagebox.showerror("Error", "Por favor, complete todos los campos.")
        return

    try:
        # Verificar el formato de fecha
        fecha_entrega = datetime.strptime(tarea_fecha, '%d/%m/%y')
    except ValueError:
        messagebox.showerror("Error", "Formato de fecha incorrecto. Use dd/mm/yy.")
        return

    # Crear nueva tarea y agregarla a la lista
    nueva_tarea = {'nombre': tarea_nombre, 'fecha_entrega': tarea_fecha, 'hecha': False, 'label_status': None}
    tareas.append(nueva_tarea)

    # Actualizar la interfaz con la nueva tarea
    actualizar_tareas(tareas, frame)

    # Revisar si se deben enviar notificaciones
    check_deadlines(tareas)

# Función para actualizar la lista de tareas en la interfaz
def actualizar_tareas(tareas, frame):
    # Limpiar el frame antes de redibujar
    for widget in frame.winfo_children():
        widget.destroy()

    # Mostrar las tareas
    for i, tarea in enumerate(tareas, 1):
        fecha_entrega = datetime.strptime(tarea['fecha_entrega'], '%d/%m/%y')
        if fecha_entrega.date() < datetime.now().date():
            color = "red"
            status = "No entregada"
        elif fecha_entrega.date() == datetime.now().date():
            color = "orange"
            status = "Se entrega hoy"
        elif fecha_entrega - datetime.now() <= timedelta(days=2):
            color = "yellow"
            status = "Fecha de entrega cercana"
        else:
            color = "green"
            status = "A tiempo"

        tarea['label_status'] = tk.Label(frame, text=status, bg=color, width=20)
        tarea['label_status'].grid(row=i, column=1, padx=10, pady=5)

        tarea_label = tk.Label(frame, text=f"{tarea['nombre']} Entrega: {tarea['fecha_entrega']}", font=("Arial", 12))
        tarea_label.grid(row=i, column=0, padx=10, pady=5)

        button_hecha = tk.Button(frame, text="Marcar como hecha", command=lambda t=tarea: marcar_como_hecha(t))
        button_hecha.grid(row=i, column=2, padx=10, pady=5)

# Crear la interfaz principal
def crear_app():
    root = tk.Tk()
    root.title("Gestor de Tareas")

    # Crear frame principal para tareas
    frame = tk.Frame(root)
    frame.grid(row=1, column=0, padx=10, pady=10)

    # Obtener la fecha actual
    fecha_actual = datetime.now()
    mes_actual = fecha_actual.strftime("%B")
    fecha_actual_str = fecha_actual.strftime("%d/%m/%y")

    # Mostrar la fecha actual
    label_mes = tk.Label(root, text=f"Mes: {mes_actual}", font=("Arial", 12))
    label_mes.grid(row=0, column=0, padx=10, pady=10)
    
    label_fecha = tk.Label(root, text=f"Fecha actual: {fecha_actual_str}", font=("Arial", 12))
    label_fecha.grid(row=0, column=1, padx=10, pady=10)

    # Lista de tareas
    tareas = [
        {'nombre': 'Hacer cuadro sinóptico', 'fecha_entrega': '03/05/25', 'hecha': False, 'label_status': None},
        {'nombre': 'Hacer resumen', 'fecha_entrega': '05/05/25', 'hecha': False, 'label_status': None},
        {'nombre': 'Exposición de Xp', 'fecha_entrega': '07/05/25', 'hecha': False, 'label_status': None},
        {'nombre': 'Entrega de apuntes', 'fecha_entrega': '30/05/25', 'hecha': False, 'label_status': None}
    ]
    
    # Mostrar tareas iniciales
    actualizar_tareas(tareas, frame)

    # Revisar notificaciones para tareas existentes
    check_deadlines(tareas)

    # Entradas para agregar tarea
    tarea_nombre_entry = tk.Entry(root, width=30)
    tarea_nombre_entry.grid(row=2, column=0, padx=10, pady=5)

    tarea_fecha_entry = tk.Entry(root, width=10)
    tarea_fecha_entry.grid(row=2, column=1, padx=10, pady=5)

    # Botón para agregar tarea
    agregar_button = tk.Button(root, text="Agregar tarea", command=lambda: agregar_tarea(tarea_nombre_entry.get(), tarea_fecha_entry.get(), tareas, frame))
    agregar_button.grid(row=2, column=2, padx=10, pady=5)

    root.mainloop()

# Ejecutar la aplicación
if __name__ == "__main__":
    crear_app()
