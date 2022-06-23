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

@app.route("/")
def index():
    """Página inicial"""
    return render_template("index.html")

@app.route("/ajude", methods=["GET", "POST"])
def ajude():
    """página com demandas"""
    if request.method == "POST":
        bairro = request.form.get("bairro")
        lugares = db.execute("SELECT * FROM lugares JOIN demandas ON lugares.id = demandas.id_lugar WHERE bairro LIKE '%'|| ? || '%' ", bairro)
        return render_template("ajude.html", lugares=lugares)
    else:
        lugares = db.execute("SELECT * FROM lugares JOIN demandas ON lugares.id = demandas.id_lugar ORDER BY demandas.data DESC")
    return render_template("ajude.html", lugares=lugares)

@app.route("/sobre")
def sobre():
    """Sobre o site"""
    return render_template("sobre.html")
