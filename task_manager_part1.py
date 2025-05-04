# Parte 1: Interfaz y tareas iniciales
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

# Crear la interfaz principal
def crear_app():
    root = tk.Tk()
    root.title("Gestor de Tareas")

    # Obtener la fecha actual
    fecha_actual = datetime.now()
    mes_actual = fecha_actual.strftime("%B")
    fecha_actual_str = fecha_actual.strftime("%d/%m/%y")
    
    # Mostrar la fecha actual
    label_mes = tk.Label(root, text=f"Mes: {mes_actual}", font=("Arial", 12))
    label_mes.grid(row=0, column=0, padx=10, pady=10)
    
    label_fecha = tk.Label(root, text=f"Fecha actual: {fecha_actual_str}", font=("Arial", 12))
    label_fecha.grid(row=0, column=1, padx=10, pady=10)

    tareas = [
        {'nombre': 'Hacer cuadro sinóptico', 'fecha_entrega': '03/04/25', 'hecha': False, 'label_status': None},
        {'nombre': 'Hacer resumen', 'fecha_entrega': '05/04/25', 'hecha': False, 'label_status': None},
        {'nombre': 'Exposición de Xp', 'fecha_entrega': '07/04/25', 'hecha': False, 'label_status': None},
        {'nombre': 'Entrega de apuntes', 'fecha_entrega': '30/04/25', 'hecha': False, 'label_status': None}
    ]

    frame = tk.Frame(root)
    frame.grid(row=1, column=0, padx=10, pady=10)
    
    # Mostrar tareas iniciales
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

    root.mainloop()

if __name__ == "__main__":
    crear_app()
