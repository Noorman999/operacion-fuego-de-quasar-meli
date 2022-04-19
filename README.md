![alt text](https://lh3.googleusercontent.com/fxBEPzc-TSycO2wbfC0OCZlhCdalG4raWv3KBx1QJ3x25ftZARu2rkZubT0XiwRZoa15Z4s8rSant631c0JJEmxR59b3y-CQxIGnn7Y "Logo")

## Operación Fuego de Quasar by Norman Funes

Programa en Python que retorna la fuente y contenido de un mensaje de auxilio emitido por un Shuttle en el medio del espacio. Para esto, tenemos tres satélites que nos
permiten triangular la posición.

## Informacion a tener en cuenta
Link del proyecto en la nube: [https://operacion-fuego-de-quasar-meli.herokuapp.com/](https://operacion-fuego-de-quasar-meli.herokuapp.com/)

#### Satelites:

Kenobi en Posicion x=-500 y=-200

Skywalker en Posicion x=-100 y=-100

Sato en Posicion x=500 y=100

#### Formato del Mensaje:
  ● El mensaje recibido en cada satélite se recibe en forma de arreglo de strings.
  
   ● Cuando una palabra del mensaje no pueda ser determinada, se reemplaza por un string en blanco en el array.
   
      ○ Ejemplo: [“este”, “es”, “”, “mensaje”]
      
  ● Puede existir un desfasaje en el mensaje que se respeta en todos los recibidos por los satelites (el arreglo de strings para todos siempre va a tener la misma longitud).
  
      ○ Ejemplo:
        ■ Kenobi: [“”, “este”, “es”, “un”, “mensaje”]
        ■ Skywalker: [“”, “este”, “”, “un”, “mensaje”]
        ■ Sato: [“”, ””, ”es”, ””, ”mensaje”]

## Nivel 1

Parametros: Distancia del shuttle a cada uno de los satelites (flotantes)

Respuesta: Posicion del Shuttle en X e Y

```def GetLocation(self, kenobiDistance, skywalkerDistance, satoDistance)```


Parametros: Mensajes indeterminados mandados a los satelites

Respuesta: Mensaje completo

```def GetMessage(self, kenobiMessage, skywalkerMessage, satoMessage)```


Las funciones de  ```GetLocation``` y ```GetMessage``` se encuentran dentro del path ```resources/models/shuttle.py```

## Nivel 2

Se puede acceder a la API mediante ```https://operacion-fuego-de-quasar-meli.herokuapp.com/topsecret/```

### POST ```/topsecret_split/```

#### Request

```
{
    "satellites": [
        {
            "name": "kenobi",
            "distance": 300,
            "message": ["", "este", "", "", "mensaje", ""]
        },
        {
            "name": "skywalker",
            "distance": 632.45,
            "message": ["", "", "es", "", "", "secreto"]
        },
        {
            "name": "sato",
            "distance": 1000,
            "message": ["", "este", "", "un", "", ""]
        }
    ]
}
```

#### Response

```
{
    "position": {
        "x": -499.99,
        "y": 99.96
    },
    "message": "este es un mensaje secreto"
}
```

## Nivel 3

Se puede acceder a la API mediante ```https://operacion-fuego-de-quasar-meli.herokuapp.com/topsecret_split/```

### POST ```/topsecret_split/{satelite}```

#### Request

```
  {
    "name": "skywalker",
    "distance": 632.45,
    "message": ["", "es", "", "", "secreto"]
  }
```

#### Response

```
RESPONSE
{
    "status": "Satelite skywalker cargado"
}
```

### GET ```/topsecret_split/```

#### Response

```
RESPONSE
{
    "position": {
        "x": -499.99,
        "y": 99.96
    },
    "message": "este es un mensaje secreto"
}
```

## Disclaimer

  This project was created with the only fact of presenting it as a development test for the company "MercadoLibre"
