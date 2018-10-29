'''This module holds all data and logic of the users in the application'''
from flask import make_response, jsonify
from datetime import datetime

users = []

sample_user={"email":"panda@gmail.com",
"password":"123456",
"role":"admin"
}

users.append(sample_user)



comments = []


class UserModels():
    '''Initializes a new user'''
    def __init__(self, email, password, role):
        self.id = len(users) + 1
        self.email = email
        self.password = password
        self.role = "normal"

    def get_by_mail(self,email):
        user=[user for user in users if user['email']==str(email)]
        return user
        
    def save(self):
        '''Saves a user by appending them to the users list'''
        new_user = {
                "id": self.id,
                "email": self.email,
                "password": self.password,
                "role": self.role,
                'date_added': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
        users.append(new_user)

        response = jsonify(new_user)

        return response

class CommentsModel():
    '''Initializes a new product'''
    def __init__(self, comment_id, message, author):
        self.comment_id = comment_id
        self.message = message
        self.author = author

    def save(self):
        '''Saves a product by appending it to the products list'''
        new_comment = {
            "comment_id": self.comment_id,
            "message": self.message["message"],
            "author": self.author["author"],
            'date_added': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        comments.append(new_comment)