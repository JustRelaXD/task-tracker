from flask import Flask, render_template_string, request, redirect
import sqlite3
from datetime import date

app = Flask(__name__)

import sqlite3

def inital_db():
    conn = sqlite3.connect("tasks.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            task_date TEXT NOT NULL,
            task_time TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

initial_db() 

@app.route("\", methods=["GET])