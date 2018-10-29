from app.tests.base_test import BaseTestCase
import json

class Comment(BaseTestCase):
    def test_add_comment(self):
        comment={"message":"Hi am a message","author":"panda"}
        response=self.post("/api/v2/comments",comment)
        self.assertEqual(response.status_code,201)
        self.assertEqual({"message": "comment added successfully"},json.loads(response.data))
