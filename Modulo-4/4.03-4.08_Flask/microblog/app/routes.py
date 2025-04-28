from flask import (
    render_template, 
    request, redirect, 
    url_for, 
    flash #! Tem como usar mas não sei como usar
    )
# Sim, é só esse import para disparar o __init__.py
# e recuperar a referência do objeto Flask
from app import app
from app import alquimias


@app.route("/")
def index():
    user = None
    username = request.args.get("username")
    if username: user = {"username" : username}

    return render_template(
        "index.html", # página existente na pasta
        title="Página Inicial", # atributo dinâmico
        user=user # atributo dinâmico user
    )

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if alquimias.validate_user_password(username, password):
            print("\nLogin bem sucedido!\n")
            return redirect(url_for("index", username=username))
        else:
            print("\nUsuário ou senha inválidos\n")
            return redirect(url_for("login"))

    else:
        # request.method == "GET"
        return render_template("login.html", title="Login")
    
@app.route("/cadastro", methods=["POST"])
def cadastro():
    username = request.form["username"]

    if alquimias.user_existis(username):
        print("\nUsuário já existe!\n")
        return redirect(url_for("login"))
    
    else:
        username = username
        password = request.form["password"]
        remember = True if request.form.get("remember") == "on" else False
        alquimias.create_user(username, password, remember)
        return redirect(url_for("index", username=username))