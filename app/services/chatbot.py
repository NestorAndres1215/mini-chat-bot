import random

from app.services.analisis import (
    total_gastos,
    gasto_promedio,
    gasto_por_mes,
    gasto_mayor_categoria,
    gasto_menor_categoria,
    porcentaje_por_categoria,
    ranking_gastos,
    insight_financiero,
    comparacion_mensual,
    categoria_mas_frecuente,
    dia_mas_caro
)


def responder(mensaje: str):
    mensaje = mensaje.lower()

    # =========================
    # 👋 CONVERSACIÓN HUMANA
    # =========================
    if any(p in mensaje for p in ["hola", "buenas", "hey", "que tal"]):
        return random.choice([
            "👋 ¡Hola! ¿En qué te ayudo hoy con tus gastos?",
            "😊 Hola! Estoy listo para analizar tus finanzas contigo",
            "💰 ¡Hey! Vamos a ver cómo van tus gastos hoy"
        ])

    if any(p in mensaje for p in ["como estas", "cómo estás", "que tal estas", "qué tal estás"]):
        return random.choice([
            "😊 Estoy bien, listo para ayudarte con tus gastos",
            "💡 Todo en orden! ¿Revisamos tus finanzas?",
            "📊 Funcionando perfecto, listo para analizar tus datos"
        ])

    if any(p in mensaje for p in ["bien", "todo bien"]):
        return "😄 ¡Qué bueno! ¿Quieres ver tus gastos o un análisis?"

    if any(p in mensaje for p in ["gracias", "te lo agradezco"]):
        return random.choice([
            "😊 ¡De nada! Estoy aquí para ayudarte",
            "💡 Con gusto 👍",
            "🚀 Siempre listo para tus finanzas"
        ])

    if any(p in mensaje for p in ["ok", "dale", "listo"]):
        return "👍 Perfecto, dime qué quieres analizar"

    # =========================
    # 🧠 INSIGHT COMPLETO
    # =========================
    if any(p in mensaje for p in ["analisis", "análisis", "insight", "resumen"]):
        return insight_financiero()

    # =========================
    # 📊 PORCENTAJES
    # =========================
    if any(p in mensaje for p in ["porcentaje", "%", "distribucion", "distribución"]):
        data = porcentaje_por_categoria()
        if data is None:
            return "📭 Aún no tienes datos registrados"

        texto = "📊 Así se distribuyen tus gastos:\n"
        for k, v in data.items():
            texto += f"👉 {k}: {v:.2f}%\n"

        texto += "\n💡 Tip: intenta reducir la categoría más alta"
        return texto

    # =========================
    # 📈 RANKING
    # =========================
    if any(p in mensaje for p in ["ranking", "top", "orden", "lista"]):
        data = ranking_gastos()
        if data is None:
            return "📭 No hay datos aún"

        texto = "📈 Ranking de gastos:\n"
        for k, v in data.items():
            texto += f"🥇 {k}: S/{v:.2f}\n"

        return texto

    # =========================
    # 🔝 MAYOR GASTO
    # =========================
    if any(p in mensaje for p in ["mas", "más", "mayor", "alto"]):
        r = gasto_mayor_categoria()
        if not r:
            return "📭 No hay datos"

        cat, monto = r
        return (
            f"🔝 Tu mayor gasto es en **{cat}**\n"
            f"💸 Total: S/{monto:.2f}\n"
            f"⚠️ Es la categoría que más impacta tu dinero"
        )

    # =========================
    # 🔻 MENOR GASTO
    # =========================
    if any(p in mensaje for p in ["menos", "menor", "bajo"]):
        r = gasto_menor_categoria()
        if not r:
            return "📭 No hay datos"

        cat, monto = r
        return f"🔻 Tu menor gasto es en **{cat}** con S/{monto:.2f}"

    # =========================
    # 📊 PROMEDIO
    # =========================
    if "promedio" in mensaje:
        p = gasto_promedio()
        return f"📊 Tu gasto promedio es S/{p:.2f}" if p else "📭 Sin datos"

    # =========================
    # 📅 MES
    # =========================
    if any(p in mensaje for p in ["mes", "mensual"]):
        data = gasto_por_mes()
        if data is None:
            return "📭 No hay datos"

        texto = "📅 Gastos por mes:\n"
        for k, v in data.items():
            texto += f"📆 {k}: S/{v:.2f}\n"

        return texto

    # =========================
    # 💸 TOTAL
    # =========================
    if any(p in mensaje for p in ["total", "cuanto gaste", "gasté", "gaste"]):
        t = total_gastos()
        return f"💸 Has gastado en total: S/{t:.2f}" if t else "📭 Sin datos"

    # =========================
    # 📊 COMPARACIÓN
    # =========================
    if "comparacion" in mensaje or "comparación" in mensaje:
        c = comparacion_mensual()
        if not c:
            return "📭 No hay suficientes datos aún"

        return (
            f"📊 Mes actual: S/{c['actual']:.2f}\n"
            f"📉 Mes anterior: S/{c['anterior']:.2f}\n"
            f"📈 Cambio: {c['variacion']:.2f}%"
        )

    # =========================
    # 📊 FRECUENCIA
    # =========================
    if "frecuente" in mensaje:
        r = categoria_mas_frecuente()
        if not r:
            return "📭 Sin datos"

        return f"📊 La categoría que más usas es {r[0]} ({r[1]} veces)"

    # =========================
    # 📅 DÍA MÁS CARO
    # =========================
    if "dia caro" in mensaje or "día caro" in mensaje:
        r = dia_mas_caro()
        if not r:
            return "📭 Sin datos"

        return f"📅 El día que más gastaste fue {r[0]} con S/{r[1]:.2f}"

    # =========================
    # ❌ NO ENTENDIDO
    # =========================
    return random.choice([
        "😅 No te entendí bien, ¿puedes reformularlo?",
        "🤔 No estoy seguro de eso, prueba preguntar de otra forma",
        "💬 Puedes preguntarme por tus gastos, análisis o porcentajes"
    ])