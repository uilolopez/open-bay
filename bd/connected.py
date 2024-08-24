import pymongo
import time
def connected(collection):
    MONGO_HOST="localhost"
    MOONGO_PORT="27017"
    MONGO_TIMEOUT=1000 #tiempo para conectarse y si no se sale

    MONGO_URI="mongodb://"+MONGO_HOST+":"+MOONGO_PORT+"/"

    MONGO_BASEDATOS="openbay"# contienen tablasf
    MONGO_COLECCION=collection #tablas que contienen documentos jason para cada registyro de usuario

    try:
        cliente=pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=MONGO_TIMEOUT)
        base_datos=cliente[MONGO_BASEDATOS]
        coleccion=base_datos[MONGO_COLECCION]
        
        """for document in coleccion.find():
            print(document["user"])
            time.sleep(1)"""
        return coleccion
        #cliente.server_info()
        #print("coneccion exitosa..¡¡¡!!!")
        cliente.close()
    except pymongo.errors.ServerSelectionTimeoutError as errorTime:
        print("limite de tiempo exedido")
    except pymongo.errors.ConectionFailure as errorConection:
        print("error de conecion con la base de datos")



