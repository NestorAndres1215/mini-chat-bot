def sin_datos():
    return "Aún no tienes gastos registrados 📭"

def no_entendido():
    return ("No entendí tu consulta 😅.\n"
            "Puedes preguntar:\n"
            "- total de gastos\n"
            "- gastos por categoría")

def respuesta_total(total):
    return f"Tu gasto total es S/{total:.2f} 💸"

def respuesta_categoria(cat):
    return f"Gastas más en {cat} 📊"