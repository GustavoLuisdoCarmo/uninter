from teste import *


conn = conectar()
while True:
    print("1-Cadastrar 2-Listar 0-Sair")
    op = input("Opcao: ")
    if op == "1": criar_produto(conn)
    elif op == "2": listar_produtos(conn)
    elif op == "0": break
conn.close()