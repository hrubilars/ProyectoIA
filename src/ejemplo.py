#El nombre de la estudiante
#La calificación del curso
#El titulo de la segunda tarea
#Si la primera tarea está completada
estudiante = {
    "nombre": "Ana",
    "edad": 24,
    "curso": {
        "nombre": "Python",
        "calificacion": 92
    },
    "tareas": [
        {
            "titulo": "Variables",
            "completada": True
        },
        {
            "titulo": "Consumo de APIs",
            "completada": False
        }
    ]
}
print("Nombre de la estudiante:", estudiante["nombre"])
print("Calificación del curso:", estudiante["curso"]["calificacion"])
print("Título de la segunda tarea:", estudiante["tareas"][1]["titulo"])
print("¿La primera tarea está completada?", estudiante["tareas"][0]["completada"])  
