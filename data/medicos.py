from faker import Faker
import random


def crear_listado():
    # Crear una instancia de faker
    
    faker = Faker()
    
    # Lista vacia
    medicos = []


    for i in range (1000):
        nombre = faker.name()
        salario = 1000000
        
        medicos.append({
            'id': i,
            'nombre': nombre,
            'salario': salario
            
        })
        
    return medicos