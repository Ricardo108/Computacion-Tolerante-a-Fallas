import tkinter as tk
import pickle

class AhorcadoGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Ahorcado")

        self.palabra_a_adivinar = tk.StringVar()
        self.palabra_ingresada = tk.Entry(master, textvariable=self.palabra_a_adivinar)
        self.palabra_ingresada.pack(pady=10)

        self.iniciar_partida_btn = tk.Button(master, text="Iniciar Nueva Partida", command=self.iniciar_nueva_partida)
        self.iniciar_partida_btn.pack(pady=10)

        self.iniciar_partida_real_btn = tk.Button(master, text="Iniciar Partida", command=self.iniciar_partida, state=tk.DISABLED)
        self.iniciar_partida_real_btn.pack(pady=10)

        self.estado_label = tk.Label(master, text="")
        self.estado_label.pack(pady=10)

        self.error_label = tk.Label(master, text="", fg="red")
        self.error_label.pack(pady=10)

        self.letra_ingresada = tk.StringVar()
        self.letra_entry = tk.Entry(master, textvariable=self.letra_ingresada)
        self.letra_entry.pack(pady=10)

        self.adivinar_btn = tk.Button(master, text="Adivinar Letra", command=self.adivinar_letra, state=tk.DISABLED)
        self.adivinar_btn.pack(pady=10)

        self.letra_entry.bind("<Return>", lambda event: self.adivinar_letra())

        self.intentos_restantes_label = tk.Label(master, text="")
        self.intentos_restantes_label.pack(pady=10)

        self.intentos_maximos = 6

        self.partida_terminada = False  # Variable para rastrear si la partida ha terminado

        self.cargar_partida()

    def iniciar_nueva_partida(self):
        self.palabra_a_adivinar.set("")  # Borra la palabra a adivinar
        self.palabra_ingresada.config(state=tk.NORMAL)  # Activa el cuadro de texto
        self.iniciar_partida_real_btn.config(state=tk.NORMAL)  # Activa el botón "Iniciar"
        self.adivinar_btn.config(state=tk.DISABLED)  # Desactiva el botón "Adivinar Letra"
        self.error_label.config(text="")  # Limpia mensajes de error
        self.partida_terminada = False  # Reinicia la variable de control

    def iniciar_partida(self):
        palabra = self.palabra_a_adivinar.get().lower()
        if palabra.isalpha():
            self.palabra = palabra
            self.letras_adivinadas = []
            self.intentos = 0
            self.mostrar_tablero()
            self.guardar_estado()

            self.palabra_ingresada.config(state=tk.DISABLED)  # Desactiva el cuadro de texto
            self.iniciar_partida_real_btn.config(state=tk.DISABLED)  # Desactiva el botón "Iniciar"
            self.adivinar_btn.config(state=tk.NORMAL)  # Activa el botón "Adivinar Letra"
            self.palabra_a_adivinar.set("*" * len(self.palabra))  # Oculta la palabra
            self.partida_terminada = False  # Reinicia la variable de control

        else:
            self.error_label.config(text="Ingresa una palabra válida.")

    def adivinar_letra(self):
        if not self.partida_terminada:  # Verifica si la partida aún no ha terminado
            letra = self.letra_ingresada.get().lower()
            if letra.isalpha() and len(letra) == 1:
                if letra in self.letras_adivinadas:
                    self.error_label.config(text="Ya adivinaste esa letra. Intenta con otra.")
                elif letra in self.palabra:
                    self.letras_adivinadas.append(letra)
                    self.letra_ingresada.set('')
                    self.letra_entry.focus()
                else:
                    self.intentos += 1
                    self.error_label.config(text=f"Letra incorrecta. ¡Intentos restantes: {self.intentos_maximos - self.intentos}!")

                self.mostrar_tablero()
                self.guardar_estado()

                if "_" not in self.mostrar_tablero():
                    self.error_label.config(text=f"¡Felicidades! Has adivinado la palabra: {self.palabra}")
                    self.iniciar_partida_real_btn.config(state=tk.NORMAL)
                    self.palabra_ingresada.config(state=tk.NORMAL)
                    self.borrar_estado_guardado()
                    self.partida_terminada = True  # Marca la partida como terminada

                elif self.intentos == self.intentos_maximos:
                    self.error_label.config(text=f"¡Perdiste! La palabra era: {self.palabra}")
                    self.iniciar_partida_real_btn.config(state=tk.NORMAL)
                    self.palabra_ingresada.config(state=tk.NORMAL)
                    self.borrar_estado_guardado()
                    self.partida_terminada = True  # Marca la partida como terminada

            else:
                self.error_label.config(text="Ingresa una letra válida.")

    def mostrar_tablero(self):
        resultado = ""
        for letra in self.palabra:
            if letra in self.letras_adivinadas:
                resultado += letra + " "
            else:
                resultado += "_ "
        self.estado_label.config(text=resultado.strip())
        self.intentos_restantes_label.config(text=f"Intentos restantes: {self.intentos_maximos - self.intentos}")
        return resultado.strip()

    def guardar_estado(self):
        with open("ahorcado_estado.pkl", "wb") as archivo_estado:
            pickle.dump(self.palabra, archivo_estado)
            pickle.dump(self.letras_adivinadas, archivo_estado)
            pickle.dump(self.intentos, archivo_estado)

    def cargar_partida(self):
        try:
            with open("ahorcado_estado.pkl", "rb") as archivo_estado:
                self.palabra = pickle.load(archivo_estado)
                self.letras_adivinadas = pickle.load(archivo_estado)
                self.intentos = pickle.load(archivo_estado)
            self.mostrar_tablero()
            self.iniciar_partida_real_btn.config(state=tk.DISABLED)
            self.palabra_ingresada.config(state=tk.DISABLED)
            self.adivinar_btn.config(state=tk.NORMAL)  # Activa el botón "Adivinar Letra"
        except FileNotFoundError:
            pass

    def borrar_estado_guardado(self):
        try:
            with open("ahorcado_estado.pkl", "wb") as archivo_estado:
                pass
            self.palabra_ingresada.config(state=tk.NORMAL)  # Activa el cuadro de texto
            self.adivinar_btn.config(state=tk.DISABLED)  # Desactiva el botón "Adivinar Letra"
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")
    app = AhorcadoGUI(root)
    root.mainloop()
