SECRET_KEY = "mysecretkey"

SQLALCHEMY_DATABASE_URI = "{SGBD}://{USUARIO}:{SENHA}@{HOST}/{DATABASE}".format(
    SGBD="mysql+mysqlconnector",
    USUARIO="root",
    SENHA="19242626",
    HOST="localhost",
    DATABASE="jogoteca",
)
