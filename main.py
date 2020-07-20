import sqlite3
import time

db = sqlite3.connect('database.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users (
	login TEXT,
	password TEXT
)""")

db.commit()

def main():
	print('\n1) Зарегистрировать аккаунт.')
	print('2) Посмотреть базу данных.')
	print('3) Закрыть программу.')
	action = int(input('Выберите действие: '))

	if action == 1:
		reg()
	elif action == 2:
		for database in sql.execute("SELECT * FROM users"):
			print('\n', database, sep='')
			time.sleep(0.01)

		main()
	else:
		print('\nВыключение программы.')
		time.sleep(1.5)

def reg():
	user_login = input('\nLogin: ')
	user_password = input('Password: ')

	sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
	if sql.fetchone() is None:
		sql.execute("INSERT INTO users VALUES (?, ?)", (user_login, user_password))
		db.commit()

		print('\nАккаунт успешно создан!')
		time.sleep(1.5)

		main()
	else:
		print(f'\nАккаунт с логином {user_login} уже зарегистрирован!')

		reg()

main()