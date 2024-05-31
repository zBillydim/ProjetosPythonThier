import tkinter
from tkinter.messagebox import showinfo

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Lista de Tarefas")
        self.master.geometry("300x500")
        self.tarefas = []
        self.tarefa = tkinter.StringVar()
        self.label = tkinter.Label(master, text="Tarefa:", font=("Arial", 12))
        self.label.pack(pady=5, padx=10, anchor="w")
        self.entrada = tkinter.Entry(master, textvariable=self.tarefa, width=45)
        self.entrada.pack(pady=5)
        self.adicionar = tkinter.Button(master, text="Adicionar tarefa", command=self.add_task)
        self.adicionar.pack(pady=5, padx=10, anchor="w")
        self.lista = tkinter.Listbox(master, height=20, width=45)
        self.lista.pack()
        self.remover = tkinter.Button(master, text="Remover tarefa", command=self.remove_task)
        self.remover.pack(pady=5, padx=10, anchor="w")
    def add_task(self):
        tarefa = self.tarefa.get()
        if tarefa:
            self.tarefas.append(tarefa)
            self.lista.insert(tkinter.END, tarefa)
            self.tarefa.set("")
            return
        showinfo("Erro", "Por favor, insira uma tarefa.")
    def remove_task(self):
        indice = self.lista.curselection()
        if indice:
            self.lista.delete(indice)
            self.tarefas.pop(indice[0])
            return
        showinfo("Erro", "Selecione uma tarefa para remover.")
    def update_tasks_listbox(self):
        self.lista.delete(0, tkinter.END)
        for tarefa in self.tarefas:
            self.lista.insert(tkinter.END, tarefa)
root = tkinter.Tk()
app = ToDoListApp(root)
root.mainloop()