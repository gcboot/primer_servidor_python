
from jinja2 import Environment
from jinja2 import FileSystemLoader
from wsgiref.simple_server import make_server

env = Environment(loader=FileSystemLoader('templates')) # configurar la carpte donde estan los templates

def aplication(environ, start_response): # Interfaz - WSGI
  status = '200 OK' # El status debe de tener 4 caracteres

  context = {
    'username': 'gcboot',
    'courses': ['Python', 'Django', 'Flask', 'Base de datos']
  }

  path = environ.get('PATH_INFO')

  if path == '/':
    template = env.get_template('index.html')
    response = template.render(**context) # kwargs
  elif path == '/users':
    template = env.get_template('users.html')
    response = template.render(**context) 

  start_response(status, [])
  return [ bytes(response, 'UTF-8') ] # Respuesta del cliente

PORT = 8000


with make_server('localhost', PORT, aplication) as server:
  print(f'>>> El Servidor se encuentra a la eschuca en el puerto {PORT}')
  server.serve_forever()

