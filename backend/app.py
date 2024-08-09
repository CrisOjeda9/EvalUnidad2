from fastapi import FastAPI
#from routes.persona import persona
#from routes.usuario import usuario
from routes.users import user
from routes.persons import person
from routes.roles import roles
from routes.usersrols import userrol
from routes.medicamentos import medicamento
from routes.dispensaciones import dispensacion



app= FastAPI()
#app.include_router(persona)
#app.include_router(usuario)
app.include_router(user)
app.include_router(person)
app.include_router(roles)
app.include_router(userrol)
app.include_router(medicamento)
app.include_router(dispensacion)



from fastapi.middleware.cors import CORSMiddleware

# Configura CORS para permitir solicitudes desde cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Cambia a ["http://localhost:5173"] si quieres restringir a tu frontend
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos; puedes ajustar esto si es necesario
    allow_headers=["*"],  # Permitir todos los encabezados; puedes ajustar esto si es necesario
)

# Incluye tus routers


print("Bienvenido a mi aplicacion")