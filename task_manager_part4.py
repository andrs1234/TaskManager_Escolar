# Version 4: Notificación de fechas cercanas
import tkinter as tk
from plyer import notification
from datetime import datetime, timedelta

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
