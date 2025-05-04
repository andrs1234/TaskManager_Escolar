# Parte 3: Función para actualizar y marcar tareas
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Función para marcar tarea como entregada
def marcar_como_hecha(tarea):
    tarea['hecha'] = True
    tarea['label_status'].config(text="Entregada", bg="green")

# Función para actualizar tareas
def actualizar_tareas(tareas, frame):
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
