"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7v75269vf5qbc20k0-a.oregon-postgres.render.com",
        database="todo_ss03",
        user="root",
        password="z0sTtJWgERVceJ2JBP46Cg1rknC8fzum")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
