from app.tests.base_test import BaseTestCase
import json
class User(BaseTestCase):
    def test_create_account(self):
        user={"email":"jane@gmail.com","password":"123456"}
        response=self.post("/api/v2/user",user)
        self.assertEqual(response.status_code,201)
        self.assertEqual({"message": "user created successfully"},json.loads(response.data))
