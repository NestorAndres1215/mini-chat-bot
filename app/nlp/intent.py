from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Datos de entrenamiento simples
texts = [
    "hola", "buenos dias",
    "total gastos", "cuanto gaste", "cuanto gasté",
    "en que gasto mas", "gastos por categoria",
    "adios", "hasta luego"
]

labels = [
    "saludo", "saludo",
    "total", "total", "total",
    "categoria", "categoria",
    "despedida", "despedida"
]

# Vectorizador
vectorizer = TfidfVectorizer()

# Transformar texto
X = vectorizer.fit_transform(texts)

# Modelo
model = MultinomialNB()
model.fit(X, labels)


def detectar_intencion(mensaje: str):
    X_test = vectorizer.transform([mensaje])
    return model.predict(X_test)[0]