from flask import Flask #request
from flask_restful import Api #reqparse
from flask_jwt import JWT #jwt_required

from security import authenticate, identity
from user import UserRegister
from item import Item, ItemList

app1 = Flask(__name__)
app1.secret_key = 'dimitris'
api = Api(app1)

jwt = JWT(app1, authenticate, identity) # new endpoint /auth

#items = []    # We will store data in a database, so we no longer need the "items" list

# When we work with Flask RESTful we don't need to return jsonify items



 

api.add_resource(Item, '/item/<string:name>') 
api.add_resource(ItemList, '/items') 
api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
	app1.run(port = 5000, debug = True)
	
	


