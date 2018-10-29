from  flask_restful import Resource
from flask import jsonify, make_response, request

class User(Resource):
    def post(self):
        data=request.get_json()

    try:
    


    except Exception as e:
        print(e)
       
