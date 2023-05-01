import tkinter as tk

def calcular_generacion():
    edad = int(entrada_edad.get())
    año_de_nacimiento = 2023 - edad
    if año_de_nacimiento >= 1920 and año_de_nacimiento <= 1940:
        generacion = "Generacion Silenciosa"
    elif año_de_nacimiento >= 1946 and año_de_nacimiento <= 1964:
        generacion = "Generacion Baby Boomer"
    elif año_de_nacimiento >= 1965 and año_de_nacimiento <= 1979:
        generacion = "Generacion X"
    elif año_de_nacimiento >= 1980 and año_de_nacimiento <= 2000:
        generacion = "Generacion Y"
    elif año_de_nacimiento >= 2001 and año_de_nacimiento <= 2010:
        generacion = "Generacion Z"
    else:
        generacion = "No existe generacion asociada"
    etiqueta_generacion.config(text=generacion)

ventana = tk.Tk()
ventana.title("Calculadora de generación")

# Crear el campo de entrada
etiqueta_edad = tk.Label(ventana, text="Ingrese su edad:")
etiqueta_edad.pack()
entrada_edad = tk.Entry(ventana)
entrada_edad.pack()

# Crear el botón de cálculo
boton_calcular = tk.Button(ventana, text="Calcular generación", command=calcular_generacion)
boton_calcular.pack()

# Crear la etiqueta donde se mostrará la generación
etiqueta_generacion = tk.Label(ventana, text="")
etiqueta_generacion.pack()

ventana.mainloop()
