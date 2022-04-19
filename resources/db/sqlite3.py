import sqlite3 as sql
import os

class SqliteHandler:
    """
    Cuando se instancia la clase, se crea una conexion con la base de datos de Sqlite configurada para interactucar con la misma.\n
    La conexion se cierra cuando el objecto es eliminado.\n
    Para mas informacion sobre el uso de los metodos: https://www.sqlite.org/index.html
    """

    def __init__(self):
        self.conn = sql.connect("satelites-database.db")
        self.conn.commit()


    def create_model(self, name: str, attributes: dict):
        parsed_attributes = "(name text PRIMARY KEY, "
        for attribute in attributes:
            parsed_attributes = parsed_attributes + attribute + " " + attributes[attribute] + ", "
        parsed_attributes = parsed_attributes[:-2] + ")"
        curs = self.conn.cursor()
        curs.execute(f'CREATE TABLE IF NOT EXISTS {name} {parsed_attributes};')
        self.conn.commit()


    def create_object(self, model: str, name: str):
        curs = self.conn.cursor()
        curs.execute(f'INSERT OR IGNORE INTO {model} (name) VALUES("{name}")')
        self.conn.commit()


    def set_model_attribute(self, model: str, name: str, attribute: str, value):
        if model == None or name == None or attribute == None:
            raise Exception("Todos los atributos son obligatorios a excepcion de value")
        curs = self.conn.cursor()
        curs.execute(f'UPDATE {model} SET {attribute}="{value}" WHERE name="{name}";')
        self.conn.commit()

    
    def get_model_attribute(self, model: str, name: str, attribute: str):
        if model == None or name == None or attribute == None:
            raise Exception("Todos los atributos son obligatorios")
        curs = self.conn.cursor()
        curs.execute(f'SELECT {attribute} FROM {model} WHERE name="{name}";')
        attribute = curs.fetchall()
        self.conn.commit()
        return attribute[0][0]


    def disconnect(self):
        self.conn.close()
    