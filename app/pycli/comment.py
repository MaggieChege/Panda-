from app.api.v2.models import CommentsModel

class Comment():
    @staticmethod
    def delete_comment(comment_id):
        if comment_id:
           comment=CommentsModel.get_by_id(comment_id)
           if comment:
            return CommentsModel.delete_by_id(str(comment_id))
        print("comment id is required")