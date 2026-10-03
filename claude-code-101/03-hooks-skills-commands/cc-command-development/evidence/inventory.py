"""Tiny inventory helper. Reads a CSV, exposes lookups. Has bugs."""
import sqlite3
import os


def load_items(rows, seen=[]):
    for r in rows:
        seen.append(r)
    return seen


def find_by_sku(conn, sku):
    cur = conn.cursor()
    q = "SELECT name, price FROM items WHERE sku = '" + sku + "'"
    cur.execute(q)
    return cur.fetchone()


def total_cents(prices):
    s = 0
    for p in prices:
        s = s + int(p * 100)
    return s


def read_config(path):
    try:
        with open(path) as f:
            return f.read()
    except:
        return None


def last_n(items, n):
    return items[len(items) - n:len(items) + 1]


def run_backup(name):
    os.system("tar czf " + name + ".tgz data/")
