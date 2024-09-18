from flask import Flask
from flask_restful import Resource, Api, reqparse ,abort
from flask_sqlalchemy import SQLAlchemy

#Initialize Flask app and API
app=Flask(__name__)
api=Api(app)

# Configure MySQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Nitin%400806@localhost:3306/todo_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)
 
# Define the Task model for the database
class TodoModel(db.Model):
    __tablename__='todos'
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    summary = db.Column(db.String(500), nullable=False)

# Create the tables in the database
with app.app_context():
    db.create_all()
    
#todos= {
#     1:{"task": "write hello world program", "summary": "write the code using python"},
#     2:{"task": "Task 2","summary":"writing task 2"},
#     3:{"task":"Task 3","summary":"writing task 3"},
# }    

# Argument parsers for POST and PUT methods
task_post_args= reqparse.RequestParser()
task_post_args.add_argument("task", type=str,help="Task is required.", required=True)
task_post_args.add_argument("summary", type=str, help="summary is required", required=True)

task_update_args=reqparse.RequestParser()
task_update_args.add_argument('task', type=str)
task_update_args.add_argument('summary',type=str)

# Define the TODOLIST resource (GET all tasks)
class TODOLIST(Resource):
    def get(self):
        todos=TodoModel.query.all()
        return [{'id': todo.id, 'task': todo.task, 'summary': todo.summary} for todo in todos]

# Define the TODO resource (GET, POST, PUT, DELETE individual tasks)    
class TODO(Resource):
    def get(self, todo_id):
        todo=TodoModel.query.get(todo_id)
        if not todo:
            abort(404, message="TAsk not found")
        return {'id':todo.id,'task':todo.task, 'summary':todo.summary}  
    
    def post(self,todo_id):
        args=task_post_args.parse_args()
        if TodoModel.query.get(todo_id):
            abort(409, "Task Id already taken")
        new_task=TodoModel(id=todo_id, task=args["task"], summary=args["summary"])
        db.session.add(new_task)
        db.session.commit()
        return {'id':new_task.id, 'task': new_task.task, 'summary':new_task.summary},201
    
    def put(self, todo_id):
        args=task_update_args.parse_args()
        todo=TodoModel.query.get(todo_id)
        if not todo:
            abort(404, message="Task doesn't exist, cannot update")
        if args['task']:
            todo.task=args['task']
        if args['summary']:
            todo.summary=args['summary']
        db.session.commit()    
        return {'id':todo.id,'task':todo.task, 'summary':todo.summary}
        
    def delete(self,todo_id):
        todo=TodoModel.query.get(todo_id)
        if not todo:
            abort(404, message="Task not found")
        db.session.delete(todo)    
        db.session.commit()    
        return {'message':'Task deleted'}          
             
# Add the resources to the API
api.add_resource(TODO, '/todos/<int:todo_id>')
api.add_resource(TODOLIST, '/todos')    

if __name__=='__main__':
    app.run(debug=True)
    