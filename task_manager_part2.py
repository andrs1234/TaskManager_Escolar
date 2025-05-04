# version 2: Agregar tareas y validaciones
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

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
