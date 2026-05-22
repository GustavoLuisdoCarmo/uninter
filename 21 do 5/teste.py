import sqlite3

def conectar():
    conn = sqlite3.connect('loja.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS produto (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL,
        estoque INTEGER DEFAULT 0
    )''')
    conn.commit()
    return conn

def criar_produto(conn):
    nome = input("Nome do produto: ")
    preco = float(input("Preço: R$ "))
    estoque = int(input("Estoque: "))
    conn.execute(
    "INSERT INTO produto (nome, preco, estoque) VALUES (?, ?, ?)",
    (nome, preco, estoque)
    )
    conn.commit()
    print(f"'{nome}' cadastrado!")

def listar_produtos(conn):
    cursor = conn.execute(
    "SELECT id, nome, preco, estoque FROM produto ORDER BY \
nome"
    )
    produtos = cursor.fetchall()
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    for p in produtos:
        print(p[0], p[1], "R$", p[2], "| Estoque:", p[3])