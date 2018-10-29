from app.api.v2.models import UserModels,CommentsModel
from app.pycli.login import Login
from app.pycli.comment import Comment

task=str(input("Enter task: "))

if task=="add user":
    email=str(input("Enter email: "))
    password=str(input("Enter password: "))
    user=UserModels(email,password)
    user.save()
    print("user created successfully")

if task== "add comment":
    message=str(input("Enter message: "))
    author=str(input("Enter author: "))
    comment=CommentsModel(message, author)
    comment.save()
    print("Comment added successfully")

if task=="login":
    email=str(input("Enter email: "))
    password=str(input("Enter password: "))

    if not email or email=="":
        print("email is required")
    elif not password or password=="":
        print("password is required")
    else:
        attempt=Login(email,password)
        if attempt:
              print("Logged in successfully")

if task=="delete comment":
    comment_id=str(input("Enter comment id: "))
    if comment_id:
        deleted=Comment.delete_comment(comment_id)
        if deleted:
            print("Comment deleted successfully")
    print("Comment does not exist")







