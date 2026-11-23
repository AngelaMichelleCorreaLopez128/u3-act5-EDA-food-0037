import pandas as pd
import matplotlib.pyplot as plt
# Angela Correa NC = 0037
# 1. Leer el archivo CSV
df_food_india = pd.read_csv('indian_food.csv')
print("\n--- DATOS LEÍDOS DESDE CSV, comida India 0037 ---")
print(df_food_india)
print("\n--- Mostrar Nombre comida + ingredientes 0037 ---")
recetas = df_food_india[['name', 'ingredients']]
print(recetas)
print("\n--- Tiempo de cocinado mostrar 10 registros con head 0037 ---")
nombre_y__hora = df_food_india[['name', 'cook_time']].head(10)
print(nombre_y__hora)