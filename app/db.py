from sqlalchemy import create_engine

DATABASE_URL = "mysql+mysqlconnector://root:12345@localhost/chatbot_gastos"

engine = create_engine(DATABASE_URL)