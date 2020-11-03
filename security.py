from user import User 

users = [
	User(1,'bob','asdf')
]

#username_mapping = {u.username: u for u in users}     We don't use them anymore because we 
#														have the methods from User class													
#userid_mappind = {u.id: u for u in users}

def authenticate(username,password):

	user = User.find_by_username(username)
	if user is not None and user.password == password:
		return user 

def identity(payload):
	user_id = payload['identity']
	return User.find_by_id(user_id)
