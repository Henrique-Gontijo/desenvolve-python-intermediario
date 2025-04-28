from datetime import datetime
from sqlalchemy import select
from app import db
from app.models.models import User

def validate_user_password(username, password):
    ''' Testa se o usuário e senha correspondem a um registro no banco '''
    # ATENÇÃO o comando utilizado é SCALAR não SCALARS, logo ele retorna só o 1° resultado
    res = db.session.scalars(select(User).where(User.username == username))
    res = res.first()
    return (res and res.password == password)

def user_existis(username):
    ''' Testa se o usuário informado corresponde a um registro no banco '''
    res = db.session.scalars(select(User).where(User.username == username))
    return res.first()

def create_user(username, password, remember=False, last_login=None):
    new_user = User(
        username = username,
        password = password,
        remember = remember,
        last_login = last_login if last_login else datetime.now()
    )

    db.session.add(new_user)
    db.session.commit()