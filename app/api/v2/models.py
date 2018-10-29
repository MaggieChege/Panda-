'''This module holds all data and logic of the users in the application'''
from flask import make_response, jsonify
from datetime import datetime
from werkzeug.security import generate_password_hash
users = []

sample_user={"email":"panda@gmail.com",
"password":generate_password_hash("123456"),
"role":"admin"
}

users.append(sample_user)

sample_comment={"id": "1",
"message": "This is a comment",
"author":"panda"}



comments = []

comments.append(sample_comment)
class UserModels():
    '''Initializes a new user'''
    def __init__(self, email, password):
        self.id = len(users) + 1
        self.email = email
        self.password = generate_password_hash(password)
        self.role = "normal"

    @staticmethod
    def get_by_mail(email):
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
        return  users.append(new_user)

class CommentsModel():
    '''Initializes a new product'''
    def __init__(self, message, author):
        self.comment_id = len(comments) + 1
        self.message = message
        self.author = author

    def save(self):
        '''Saves a product by appending it to the products list'''
        new_comment = {
            "message": self.message,
            "author": self.author,
            'date_added': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    
        return comments.append(new_comment)
        
    @staticmethod
    def get_by_id(comment_id):
        if comment_id:
            comment=[comment for comment in comments if comment['id']==str(comment_id)]
            if comment:
                return comment
            else:
                print("comment does not exist")

    @staticmethod
    def delete_by_id(comment_id):
        for x, comment in enumerate(comments):
            if  comment['id']==str(comment_id):
                comments.pop(x)