from bd import connected
from models import class__main__data
from bson.objectid import ObjectId
import pymongo
def delete__message(id__message):
    collection__user=connected.connected("mail")
    for document in collection__user.find():
        print(document["_id"])
        if str(document["_id"])== str(id__message):
            collection__user.delete_one({'_id': document["_id"]})

def update_balance(email, new_balance):
    collection__user=connected.connected("users")
    # Actualizar el documento
    result = collection__user.update_one(
        {'email': email},  # Filtro para encontrar el documento
        {'$set': {'cripto': int(new_balance)}}  # Campos a actualizar
    )

def toggle_admin_status(email):
    collection_user = connected.connected("users")
    
    # Buscar el documento del usuario por email
    document = collection_user.find_one({'email': email})
    
    if document:
        # Invertir el estado del campo 'admin'
        new_status = not document.get('admin', False)
        result = collection_user.update_one(
            {'email': email},  # Filtro para encontrar el documento
            {'$set': {'admin': new_status}}  # Actualizar el campo 'admin'
        )
        
        # Verificar si la actualización fue exitosa
        if result.modified_count == 1:
            print(f"El estado de admin para {email} se ha actualizado a {new_status}.")
        else:
            print(f"No se pudo actualizar el estado de admin para {email}.")
    else:
        print(f"No se encontró ningún usuario con el email {email}.")

