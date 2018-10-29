from app.tests.base_test import BaseTestCase

class User(BaseTestCase):
    def test_create_account(self):
        user={"email":"jane@gmail.com","password":"123456"}
        response=self.post("/user",user)

        self.assertEqual(response.status_code,201)
