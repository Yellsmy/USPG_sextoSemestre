import tkinter as tk
from tkinter import filedialog, messagebox,ttk
from PIL import Image,ImageTk
from Errores import LexicalError
from analizadorLexico import ejecutar 
from analizadorSintactico import call_Parse, print_ast
from main import nombre__crear_archivo

def almacenar_tokens(tokens):
    # Crea una nueva ventana emergente
    ventana_emergente = tk.Toplevel(ventana)
    ventana_emergente.title("Almacenar Tokens")

    # Etiqueta de pregunta
    pregunta_label = tk.Label(ventana_emergente, text="¿Desea almacenar los tokens en un archivo?")
    pregunta_label.pack()

    # Botón "Sí" para almacenar los tokens
    def guardar_tokens():
        nombre_archivo = nombre__crear_archivo()
        try:
            with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
                for token in tokens:
                    archivo.write(f"{token}\n")
            archivo.close()
            messagebox.showinfo(f"Tokens Guardados", "Los tokens se han almacenado en el archivo: {nombre_archivo}")
        except Exception as e:
            print(f"Ocurrió un error al almacenar los tokens en el archivo: {e}")
        ventana_emergente.destroy()   
    boton_si = tk.Button(ventana_emergente, text="Sí", command=guardar_tokens)
    boton_si.pack()

    # Botón "No" para no almacenar los tokens
    def no_guardar_tokens():
        ventana_emergente.destroy()

    boton_no = tk.Button(ventana_emergente, text="No", command=no_guardar_tokens)
    boton_no.pack()


def mostrar_error(error_msg):
    messagebox.showerror("Error", error_msg)


def analizar_lexico():
    # Obtener el nombre del archivo del campo de entrada
    archivo = archivo_entry.get()
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            codigo = f.read()
        # Ejecutar el analizador léxico
        tokens = ejecutar(codigo)
        # Mostrar los tokens en el área de texto
        resultado_text.delete(1.0, tk.END)
        for token in tokens:
            resultado_text.insert(tk.END, token + '\n')
        
        # Preguntar si se desean almacenar los tokens
        almacenar_tokens(tokens)
    except LexicalError as e:
        error_message = str(e)
        mostrar_error(error_message)

def imprimir_arbol(node, widget, level=0):
    indentation = " " * level * 2
    if isinstance(node, tuple):
        widget.insert(tk.END, f"{indentation}{node[0]}\n")
        for child in node[1:]:
            imprimir_arbol(child, widget, level + 1)
    elif isinstance(node, list):
        for child in node:
            imprimir_arbol(child, widget, level + 1)
    else:
        widget.insert(tk.END, f"{indentation}{node}\n")

def analizar_sintactico():
    # Obtener el nombre del archivo del campo de entrada
    archivo = archivo_entry.get()
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            codigo = f.read()
        # Ejecutar el analizador sintáctico y mostrar el resultado en el área de texto
        resultado_text_s.delete(1.0, tk.END)  # Limpiar el widget Text
        result = call_Parse(codigo)  # Obtener el resultado del análisis sintáctico
        imprimir_arbol(result, resultado_text_s)  # Imprimir el árbol en el widget Text
    except LexicalError as e:
        error_message = str(e)
        mostrar_error(error_message)

def scroll(event):
    resultado_text.yview_scroll(int(-1*(event.delta/120)), "units")
    resultado_text_s.yview_scroll(int(-1*(event.delta/120)), "units")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Compilador")
ventana.geometry("800x600")



# Campo de entrada para el nombre del archivo
archivo_label = ttk.LabelFrame(ventana, text="Nombre del archivo:")
archivo_label.grid(column=0,row=0,columnspan=2, padx=5, pady=5)
archivo_entry = ttk.Entry(archivo_label)
archivo_entry.grid(column=0,row=1, columnspan=2,padx=4,pady=4)

'''#imagen
img=Image.open("fondo.png")
img=img.resize((200,200))
img=ImageTk.PhotoImage(img)
img_lbl=tk.Label(ventana,image=img,bg="#1F1B1C")
img_lbl.image=img
img_lbl.grid()'''

#Label analizador léxico
lexico_label = ttk.LabelFrame(ventana, text="Analizador Léxico")
lexico_label.grid(column=0,row=3,padx=5,pady=5)

# Área de texto para mostrar resultados
resultado_text = tk.Text(lexico_label)
resultado_text.grid(column=0,row=3,padx=4,pady=4) 
scrollbar = tk.Scrollbar(lexico_label, command=resultado_text.yview)
scrollbar.grid(row=3, column=1, sticky='ns')
resultado_text.config(yscrollcommand=scrollbar.set)
resultado_text.bind("<MouseWheel>", scroll)

# Botón para ejecutar el analizador léxico
lexico_button = ttk.Button(lexico_label, text="Analizador Léxico", command=analizar_lexico)
lexico_button.grid(column=0,row=4,padx=4,pady=4)


#Label analizador sintáctico
sintactico_label = ttk.LabelFrame(ventana, text="Analizador Sintáctico")
sintactico_label.grid(column=2,row=3,padx=5,pady=5)

# Área de texto para mostrar resultados
resultado_text_s = tk.Text(sintactico_label)
resultado_text_s.grid(column=2,row=3,padx=4,pady=4) 
scrollbar_s = tk.Scrollbar(sintactico_label, command=resultado_text_s.yview)
scrollbar_s.grid(row=3, column=4, sticky='ns')
resultado_text_s.config(yscrollcommand=scrollbar_s.set)
resultado_text_s.bind("<MouseWheel>", scroll)
# Botón para ejecutar el analizador sintáctico
sintactico_button = ttk.Button(sintactico_label, text="Analizador Sintáctico", command=analizar_sintactico)
sintactico_button.grid(column=2,row=4,padx=4,pady=4)



ventana.mainloop()
#Error durante el analisis lexico: 'LexicalError' object is not iterable
#Error durante el analisis lexico: 'None Type' object is not iterable
#Error durante el análisis léxico: [Errno 2] No such file or directory: 'test'