# Software Workshop 2 Final Assignment
We were given a skeleton to begin the assignment from and a strict time limit. This skeleton had been developed throughout the duration of the module and comprised the backbone of the app. The tasks involved in this assignment include:
- Create a todo list. The todo list is user-specific. This involved creating a ToDoForm (a FlaskForm) that enables users to enter their specific item todo. The ToDo relation in the data.sqlite database stores this todo item and the associated user_id (the user theat created the item). A query is made on the ToDo relation using current_user.user_id to retrieve the todo list. The list of items to do is then rendered by the view handler.
- Allow users to increment and decrement the priority of a todo item. Rather than using a FlaskForm to handle this, it was easier to use a HTML <button> tag and post the value of the todo_id with either "increment", "decrement" or "delete". The request is then handled in the view handler. Note that todo items are given a default priority of five.
- Create a file upload field to allows users to upload a file of todo items. This required creating a ToDoFileUploadForm that only allows .txt files to be uploaded. Files that are uploaded are parsed and each todo item is added to the database.

Note that these tasks are password protected.
