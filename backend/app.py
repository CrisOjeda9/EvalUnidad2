from fastapi import FastAPI
#from routes.persona import persona
#from routes.usuario import usuario
from routes.users import user
from routes.persons import person
from routes.roles import roles
from routes.usuarios_roles import UsuarioRol

app= FastAPI()
#app.include_router(persona)
#app.include_router(usuario)
app.include_router(user)
app.include_router(person)
app.include_router(roles)
app.include_router(UsuarioRol)




print("Bienvenido a mi aplicacion")