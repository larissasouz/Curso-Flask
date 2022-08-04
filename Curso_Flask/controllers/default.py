from Curso_Flask import Curso_Flask

@Curso_Flask.route("/")
def index():
   return "Hello Lari!"