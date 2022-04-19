from resources.exceptions.utils import ObjectNotFound

def findObject(objects, key, value):
    try:
        for obj in objects:
            if obj[key].lower() == value.lower():
                return obj
        raise ObjectNotFound("No se encontro el objeto solicitado")
    except Exception as default_error:
        raise ObjectNotFound("No se encontro el objeto solicitado")