from Curso_Flask import app

@app.route("/")
def index():
   return "Hello Lari!"