from bd import connected
from models import class__main__data

def verify__email(email):
    coleccion=connected.connected("users")
    for documet in coleccion.find():
        if documet["email"]==email:
            return False
    return True
def veify__login(email,password):
    coleccion=connected.connected("users")
    for documet in coleccion.find():
        if documet["email"]==email:
            if documet["password"]==password:
                return True
            else:
                return False
            