from werkzeug.wrappers import Response, Request
from werkzeug.routing import Map, Rule
from werkzeug.middleware.shared_data import SharedDataMiddleware
from jinja2 import Environment, FileSystemLoader
import json
import logging
import myfrappe.dbutils as mydb

env = Environment(loader=FileSystemLoader("myfrappe/templates/users"))
logging.basicConfig(
  filename = "myfrappe/logs/belog.log",
  level = logging.DEBUG
  )


@Request.application
def myapplication(request):
  
  if request.method == "GET" and request.path == "/simpleurl":
    return Response("This is a simple GET request 1 (default)")
    
  elif request.path == "/urlparam":
    urlname = request.args.get('name', 'Unknown')
    urlage = request.args.get('age', 'not known')
    return Response(f"The age of {urlname} is {urlage}")
    
  elif request.path == "/urljson":
    json2 = {}
    for thekey, thevalue in request.environ.items():
      json2[thekey] = str(thevalue)
    return Response(json.dumps(json2), mimetype = "application/json")
  
  elif request.path == "/urlhtml":
    message = "This is a variable from the backend"
    myhtml2 = f"""
        <html>
        <title>My HTML</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <body>
        <button>
        <a href="http://127.0.0.1:8000/templates/index">Back to the Index page</a>
        </button>
        <p>{message}</p>
        </body>
        </html>
    """
      
    return Response(myhtml2, mimetype="text/html")
  
  elif request.path == "/urljinja":
    thetemplate = env.get_template("utemp.html").render(title = "Home Page", username = "User 1")
    return Response(thetemplate, mimetype="text/html")





  elif request.path.startswith("/templates/") and request.method == "GET":
    return render_html(request, request.path, "r")

  elif request.path == "/dbop" and request.method == "POST":
    db_name = getattr(mydb, request.form.get("db_name") + "_op")()
    operation = request.form.get("operation")
    print(db_name + " - " + operation, flush=True)
    return Response(db_name)

  elif request.path == "/github_user" and request.method == "GET":
    from myfrappe.pyfiles.github import github_json
    data = github_json()
    return Response(json.dumps(data), content_type="application/json")


  elif request.path == "/run-task" and request.method == "POST":
    print_to_terminal()
    logging.info("run-task backend started")
    return Response("Var from backend - printed to terminal")
    
  elif request.path == "/crash" and request.method == "POST":
    try:
      x = 1 / 0
    except Exception as e:
      return Response(f'{{"error": "{e}"}}', status = 500, mimetype = "application/json")
    
  elif request.path == "/add-files" and request.method == "POST":
    render_html(request, "/files", "a")
    return render_html(request, "/templates/files", "r")
    
  elif request.path == "/read-files":
    return render_html(request, "/templates/files", "r")
    
  elif request.path == "/replace-files":
    render_html(request, "/templates/files", "w")
    return render_html(request, "/files", "r")
  
  elif request.path == "/json_page":
    return render_html(request, request.path, "r")
    
  elif request.path == "/listmongodb":
    return Response(mongo_listdb())
  
  endpoint, values = Map([Rule("/urldynamic/<int:id>",endpoint="dynurl")]).bind_to_environ(request.environ).match()
  
  if endpoint == 'dynurl':
    return Response(f"Product Id by Asief: {values['id']}")


  else:
    return Response(f"404 error: Path {request.path} not found")


myapplication = SharedDataMiddleware(myapplication, {"/static" : "myfrappe/static"}, cache=False)

def print_to_terminal(arg="Terminal BE"):
  print(arg, flush=True)
  
def render_html(request_obj, filename, crud):
  with open("myfrappe" + filename + ".html", crud) as h:
    if crud == "r":
      return Response(h.read(), mimetype = "text/html")
    elif crud == "a":
      userdate = request_obj.form.get("fname", "") + " - " + request_obj.form.get("dtstamp", "")
      h.write("<p>" + userdate + "</p>\n")
      h.close()
    elif crud == "w":
      newhtml = request_obj.form.get("editor","")
      h.write(newhtml)
      h.close()
  return Response("No option")
