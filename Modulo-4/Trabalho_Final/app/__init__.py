import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

########## Iniciando conexão com o banco ##########
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite+pysqlite:///microblog.db"
db = SQLAlchemy()
db.init_app(app) # Cria automaticamente uma pasta instance/ para o bannco
###################################################


# A função básica do init do pacote é importar seus módulos (lembra?)
# Para evitar import circular (já que routes import app)
# fazemos isso no final do script
from app import routes, alquimias
from app.models import models

######### Criando as tabelas em models ##########
with app.app_context():
    db.create_all()

# from app.database import models

#run inplícito