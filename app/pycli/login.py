from app.api.v2.models import UserModels
from werkzeug.security import check_password_hash

class Login():
    def __init__(self,email,password):
        self.email=email
        self.password=password

    def verify(self):
        user=UserModels.get_by_mail(self.email)
        if user:
            return check_password_hash(user['password'],self.password)
        print("invalid credentials")        




    