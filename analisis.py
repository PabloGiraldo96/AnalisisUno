import pandas as pd

from data.comidas import comidas

from data.medicos import crear_listado


#Obtener datos 

tabla= pd.read_csv('./data/empleados.csv')

tabla_dos = pd.DataFrame(comidas, columns=['comida', 'valor'])

# print(tabla_dos)


print(tabla)
print("\n") 
print(tabla.head(50))

print("\n") 
print(tabla.tail(100))

print(tabla[['nombres', 'salario']])


# print(comidas)

medicos = crear_listado()

tabla_tres = pd.DataFrame(medicos)

# print(tabla_tres)