from app.api.v2.models import UserModels,CommentsModel

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
