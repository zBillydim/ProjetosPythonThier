import tkinter
from datetime import datetime, timedelta

class Stopwatch:
    def __init__(self, master):
        self.master = master
        self.master.title("Cronômetro") 
        self.tempo_corrido = timedelta(hours=0, minutes=0, seconds=0)
        self.rodando = False
        self.display = tkinter.StringVar()
        self.display.set("00:00:00")
        self.label = tkinter.Label(master, textvariable=self.display, font=("Arial", 48))
        self.label.pack()
        self.iniciar = tkinter.Button(master, text="Iniciar", command=self.iniciar_parar)
        self.iniciar.pack(side=tkinter.LEFT, padx=10)
        self.reiniciar = tkinter.Button(master, text="Resetar", command=self.resetar)
        self.reiniciar.pack(side=tkinter.RIGHT, padx=10)
        self.atualizar()

    def iniciar_parar(self):
        if self.rodando:
            self.rodando = False
            self.iniciar.config(text="Iniciar")
            return
        self.rodando = True 
        self.iniciar.config(text="Pausar")
        self.iniciar_contagem = datetime.now() - self.tempo_corrido

    def resetar(self):
        self.rodando = False
        self.tempo_corrido = timedelta(0)
        self.display.set("00:00:00")
        self.iniciar.config(text="Iniciar")

    def atualizar(self):
        if self.rodando:
            self.tempo_corrido = datetime.now() - self.iniciar_contagem
        self.display.set(str(self.tempo_corrido).split(".")[0])
        self.master.after(100, self.atualizar)

root = tkinter.Tk()
app = Stopwatch(root)
root.mainloop()