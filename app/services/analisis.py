import pandas as pd
from app.db import engine


# =========================
# 📥 OBTENER DATOS
# =========================
def obtener_datos():
    query = "SELECT * FROM gastos"
    df = pd.read_sql(query, engine)
    return df


# =========================
# 💸 TOTAL GASTOS
# =========================
def total_gastos():
    df = obtener_datos()
    if df.empty:
        return None
    return df["monto"].sum()


# =========================
# 📊 PROMEDIO GENERAL
# =========================
def gasto_promedio():
    df = obtener_datos()
    if df.empty:
        return None
    return df["monto"].mean()


# =========================
# 📉 PROMEDIO DIARIO
# =========================
def promedio_diario():
    df = obtener_datos()
    if df.empty:
        return None

    df["fecha"] = pd.to_datetime(df["fecha"])
    dias = df["fecha"].nunique()

    return df["monto"].sum() / dias if dias > 0 else None


# =========================
# 📅 GASTO POR MES
# =========================
def gasto_por_mes():
    df = obtener_datos()
    if df.empty:
        return None

    df["fecha"] = pd.to_datetime(df["fecha"])
    df["mes"] = df["fecha"].dt.to_period("M")

    gastos = df.groupby("mes")["monto"].sum().sort_index()
    return gastos.to_dict()


# =========================
# 🔝 MAYOR CATEGORÍA
# =========================
def gasto_mayor_categoria():
    df = obtener_datos()
    if df.empty:
        return None

    gastos = df.groupby("categoria")["monto"].sum()
    return gastos.idxmax(), gastos.max()


# =========================
# 🔻 MENOR CATEGORÍA
# =========================
def gasto_menor_categoria():
    df = obtener_datos()
    if df.empty:
        return None

    gastos = df.groupby("categoria")["monto"].sum()
    return gastos.idxmin(), gastos.min()


# =========================
# 📊 % POR CATEGORÍA
# =========================
def porcentaje_por_categoria():
    df = obtener_datos()
    if df.empty:
        return None

    total = df["monto"].sum()
    gastos = df.groupby("categoria")["monto"].sum()

    porcentaje = (gastos / total) * 100
    return porcentaje.sort_values(ascending=False).to_dict()


# =========================
# 📈 RANKING DE GASTOS
# =========================
def ranking_gastos():
    df = obtener_datos()
    if df.empty:
        return None

    gastos = df.groupby("categoria")["monto"].sum()
    return gastos.sort_values(ascending=False).to_dict()


# =========================
# 📊 CATEGORÍA MÁS FRECUENTE
# =========================
def categoria_mas_frecuente():
    df = obtener_datos()
    if df.empty:
        return None

    conteo = df["categoria"].value_counts()
    return conteo.idxmax(), conteo.max()


# =========================
# 📅 DÍA MÁS CARO
# =========================
def dia_mas_caro():
    df = obtener_datos()
    if df.empty:
        return None

    df["fecha"] = pd.to_datetime(df["fecha"])
    por_dia = df.groupby(df["fecha"].dt.date)["monto"].sum()

    return por_dia.idxmax(), por_dia.max()


# =========================
# 📆 COMPARACIÓN MENSUAL
# =========================
def comparacion_mensual():
    df = obtener_datos()
    if df.empty:
        return None

    df["fecha"] = pd.to_datetime(df["fecha"])
    df["mes"] = df["fecha"].dt.to_period("M")

    gastos = df.groupby("mes")["monto"].sum().sort_index()

    if len(gastos) < 2:
        return None

    actual = gastos.iloc[-1]
    anterior = gastos.iloc[-2]

    variacion = ((actual - anterior) / anterior) * 100 if anterior != 0 else 0

    return {
        "actual": actual,
        "anterior": anterior,
        "variacion": variacion
    }


# =========================
# 🚨 ALERTA DE GASTO
# =========================
def alerta_gasto_alto(limite):
    df = obtener_datos()
    if df.empty:
        return None

    total = df["monto"].sum()

    if total > limite:
        return f"⚠️ Gastaste S/{total:.2f}, superas tu límite de S/{limite:.2f}"

    return f"✅ Bien, estás dentro del límite: S/{total:.2f}"


# =========================
# 🧠 INSIGHT FINANCIERO AVANZADO
# =========================
def insight_financiero():
    df = obtener_datos()
    if df.empty:
        return "No hay datos 📭"

    total = df["monto"].sum()
    cat, monto = gasto_mayor_categoria()
    porcentaje = (monto / total) * 100

    texto = f"""
💡 RESUMEN FINANCIERO:

💸 Total gastado: S/{total:.2f}
🔝 Mayor gasto: {cat}
📊 Representa: {porcentaje:.2f}%
"""

    comp = comparacion_mensual()
    if comp:
        texto += f"""
📆 Mes actual: S/{comp['actual']:.2f}
📆 Mes anterior: S/{comp['anterior']:.2f}
📊 Variación: {comp['variacion']:.2f}%
"""

        if comp["variacion"] > 0:
            texto += "⚠️ Estás gastando más que el mes anterior\n"
        else:
            texto += "📉 Estás gastando menos que el mes anterior\n"

    return texto