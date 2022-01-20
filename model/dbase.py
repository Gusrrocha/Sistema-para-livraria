import sqlite3

def connect():
    conn = sqlite3.connect('database/boosysk.sqlite')
    return conn