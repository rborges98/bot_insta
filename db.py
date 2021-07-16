import sqlite3

conexao = sqlite3.connect('db_bot.db')
mycursor = conexao.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS contas_seguir (contas text)")

