from  flask_restful import Resource
from flask import jsonify, make_response, request
from app.api.v2.models import UserModels, CommentsModel

class User(Resource):
    def post(self):
        data=request.get_json()
        email=data['email']
        password=data['password']

        try:
            user=UserModels(email,password)
            user.save()
            return make_response(jsonify({"message": "user created successfully"}), 201)
        except Exception as e:
            print(e)

class Comments(Resource):
    def post(self):
        data = request.get_json()
        message = data['message']
        author = data['author']

        try:
            comment = CommentsModel(message, author)
            comment.save()
            return make_response(jsonify({"message": "comment added successfully"}), 201)
        except Exception as e:
            print(e)
       
