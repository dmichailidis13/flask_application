import sqlite3
from flask_restful import Resource, reqparse
from flask import request






class User:

	def __init__(self,_id,username,password):
		self.id = _id
		self.username = username
		self.password = password

	@classmethod
	def find_by_username(cls,username):

		connection = sqlite3.connect('data.db')
		cursor = connection.cursor()

		query = "SELECT * FROM users WHERE username = ?"

		result = cursor.execute(query,(username,))
		row = result.fetchone()
		if row is not None:
			user = cls(row[0],row[1],row[2])      # We could write it as User(*row)
		else:
			user = None

		connection.close()
		return user

	@classmethod
	def find_by_id(cls,_id):

		connection = sqlite3.connect('data.db')
		cursor = connection.cursor()

		query = "SELECT * FROM users WHERE id = ?"

		result = cursor.execute(query,(_id,))
		row = result.fetchone()
		if row is not None:
			user = cls(row[0],row[1],row[2])      # We could write it as User(*row)
		else:
			user = None

		connection.close()
		return user

class UserRegister(Resource):

	parser = reqparse.RequestParser()
	parser.add_argument('username',
			type = str,
			required = True,
			help = "username is required!"
		)
	parser.add_argument('password',
			type = str,
			required = True,
			help = "password is required!"
		)
	

	def post(self):
		data = UserRegister.parser.parse_args()

		if User.find_by_username(data['username']) is not None:

			return {'message': 'A user with this username already exists'}, 400

		connection = sqlite3.connect('data.db')
		cursor = connection.cursor()

		query = "INSERT INTO users VALUES (NULL,?,?)"

		

		cursor.execute(query,(data['username'],data['password']))

		connection.commit()
		connection.close()

		return {'message':"User created succesfully"}, 201
