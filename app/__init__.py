from flask import Flask, render_template, request, redirect, url_for

def create_app():
    app = Flask(__name__)
    
    
    # ROUTES
    
    # STATIC ROUTES
    # @app.route("/", methods=["GET","POST"])
    # def home_page():
    #     print ("URL:", request.url)
    #     print ("METHOD:", request.method)
    #     return "Hello from Home Page"
    
    @app.get("/about")
    def about_page ():
        return{"message": "Server running", "page": "About Page"}
    
    
    # DYNAMIC ROUTES
    @app.get("/profile/<name>")
    def profile_page(name):
        return f"<p>Hello {name}</p>"
    
    # SPECIFY THE TYPE OF VALUE FOR THE DYNAMIC ROUTE
    @app.get("/todo/<int:id>")
    def todo_page_id(id):
        return f"<h2>This is the content of todo with id of {id}</h2>"
    
    # REQUEST OBJECT
    # https://www.bing.com/search?pglt=41&q=test&cvid=
    
    # args /query parameters
    @app.get("/test")
    def test_page():
      return request.args
    
    # TODO APP ROUTES
    todo_db = []
    
    @app.get("/todo")
    @app.route("/", methods=["GET","POST"])
    def todo_page():
        return render_template("todo.html", todos= enumerate(todo_db))
    
    @app.get("/todo/delete/<int:index>")
    def todo_delete(index):
        idx = int(index)
        todo_db.pop(idx)

        #Redirect to todo page
        return redirect(url_for('todo_page'))
    
    @app.post("/todo/update/<int:index>")
    def todo_update(index):
        new_todo = request.form.get("task")
        if new_todo is not None:
            todo_db[index] = new_todo
        return redirect(url_for("todo_page"))

   
    @app.post("/todo/create")
    def todo_create():
        form_data = request.form
        todo = form_data.get('todo')
        
        # ADD TASK TO 
        todo_db.append(todo)
        
        # REDIRECT TO HOME PAGE
        return redirect(url_for('todo_page'))
        
    
    # ERROR HANDLING IN ROUTES
    # 404
    @app.errorhandler(404)
    def error404_page(error):
        return "<h1>Page doesn't exist!</h1>"
    
    return app

# .get()
# .post()
# .delete()
# .patch()
# .put()
# .route()
# universal