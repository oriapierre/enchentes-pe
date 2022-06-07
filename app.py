import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

# Configure application
app = Flask(__name__)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///observa.db")

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/", methods=["GET", "POST"])
def index():
    """Homepage"""
    if request.method == "POST":
        bairro = request.form.get("bairro")
        abrigos = db.execute("SELECT * FROM abrigos WHERE bairro = ?", bairro)
        return render_template("index.html", abrigos=abrigos)
    else:
        abrigos = db.execute("SELECT * FROM abrigos")
    return render_template("index.html", abrigos=abrigos)

@app.route("/sobre")
def sobre():
    """Sobre o site"""
    return render_template("sobre.html")

@app.route("/ajude")
def ajude():
    """ajude"""
    return render_template("ajude.html")

@app.route("/informacoes")
def informacoes():
    """informacoes"""
    return render_template("informacoes.html")

@app.route("/contato")
def contato():
    """contato"""
    return render_template("contato.html")

@app.route("/outracoisa")
def outracoisa():
    """outra coisa"""
    return render_template("outracoisa.html")
