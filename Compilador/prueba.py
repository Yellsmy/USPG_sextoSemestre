import tkinter as tk
from tkinter import filedialog, messagebox
from analizadorLexico import ejecutar
from analizadorSintactico import call_Parse

def almacenar_tokens(tokens):
    nombre_archivo = filedialog.asksaveasfilename(defaultextension=".txt")
    if nombre_archivo:
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            for token in tokens:
                archivo.write(f"{token}\n")
        messagebox.showinfo("Tokens Guardados", "Los tokens se han almacenado en el archivo.")

def analizar_lexico():
    archivo = archivo_entry.get()
    with open(archivo, 'r', encoding='utf-8') as f:
        codigo = f.read()
    tokens = ejecutar(codigo)
    resultado_text.delete(1.0, tk.END)
    for token in tokens:
        resultado_text.insert(tk.END, token + '\n')
    almacenar_tokens(tokens)

def analizar_sintactico():
    archivo = archivo_entry.get()
    with open(archivo, 'r', encoding='utf-8') as f:
        codigo = f.read()
    resultado_text.delete(1.0, tk.END)
    result = call_Parse(codigo)
    resultado_text.insert(tk.END, str(result))

ventana = tk.Tk()
ventana.title("Compilador")

# Parte superior: Nombre del archivo y botón de análisis léxico
nombre_archivo_label = tk.Label(ventana, text="Nombre del archivo:")
nombre_archivo_label.grid(row=0, column=0)
archivo_entry = tk.Entry(ventana)
archivo_entry.grid(row=0, column=1)
analisis_lexico_button = tk.Button(ventana, text="Analizador Léxico", command=analizar_lexico)
analisis_lexico_button.grid(row=0, column=2)

# Columna izquierda: Tokens y botón de análisis léxico
resultado_text = tk.Text(ventana, height=15, width=30)
resultado_text.grid(row=1, column=0, padx=10, pady=10)
scrollbar = tk.Scrollbar(ventana, command=resultado_text.yview)
scrollbar.grid(row=1, column=1, sticky='nsew')
resultado_text.config(yscrollcommand=scrollbar.set)

# Columna derecha: Árbol y botón de análisis sintáctico
analisis_sintactico_button = tk.Button(ventana, text="Analizador Sintáctico", command=analizar_sintactico)
analisis_sintactico_button.grid(row=1, column=2)

ventana.mainloop()






#versio1

# Campo de entrada para el nombre del archivo
archivo_label = tk.Label(ventana, text="Nombre del archivo:")
archivo_label.pack()
archivo_entry = tk.Entry(ventana)
archivo_entry.pack()

# Botón para ejecutar el analizador léxico
lexico_button = tk.Button(ventana, text="Analizador Léxico", command=analizar_lexico)
lexico_button.pack()

# Botón para ejecutar el analizador sintáctico
sintactico_button = tk.Button(ventana, text="Analizador Sintáctico", command=analizar_sintactico)
sintactico_button.pack()

# Área de texto para mostrar resultados
resultado_text = tk.Text(ventana)
resultado_text.pack()

ventana.mainloop()



resultado_text = tk.Text(ventana, height=15, width=30)
resultado_text.grid(row=1, column=0, padx=10, pady=10, columnspan=2)
scrollbar = tk.Scrollbar(ventana, command=resultado_text.yview)
scrollbar.grid(row=1, column=2, sticky='ns')
resultado_text.config(yscrollcommand=scrollbar.set)
resultado_text.bind("<MouseWheel>", scroll)

resultado_text.grid(column=0,row=3,padx=4,pady=4) 