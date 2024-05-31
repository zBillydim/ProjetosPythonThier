import tkinter

class BMICalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora de IMC")
        self.peso = tkinter.DoubleVar()
        self.peso.set("")
        self.altura = tkinter.DoubleVar()
        self.altura.set("")
        self.resultado = tkinter.StringVar()
        self.resultado.set("Seu IMC é: ")
        self.label_peso = tkinter.Label(master, text="Peso (kg):")
        self.label_peso.pack()
        self.entrada_peso = tkinter.Entry(master, textvariable=self.peso)
        self.entrada_peso.pack()
        self.label_altura = tkinter.Label(master, text="Altura (m):")
        self.label_altura.pack()
        self.entrada_altura = tkinter.Entry(master, textvariable=self.altura)
        self.entrada_altura.pack()
        self.calcular = tkinter.Button(master, text="Calcular", command=self.calculate_bmi)
        self.calcular.pack()
        self.label_resultado = tkinter.Label(master, textvariable=self.resultado)
        self.label_resultado.pack()

    def calculate_bmi(self):
        imc = self.peso.get() / (self.altura.get() ** 2)
        categoria = self.show_bmi_category(imc)
        self.resultado.set(f"Seu IMC é: {imc:.2f} ({categoria})")

    def show_bmi_category(self, imc):
        if imc < 18.5:
            return "Abaixo do Peso"
        elif 18.5 <= imc < 25:
            return "Peso Normal"
        elif 25 <= imc < 30:
            return "Sobrepeso"
        elif 30 <= imc < 35:
            return "Obesidade Grau 1"
        elif 35 <= imc < 40:
            return "Obesidade Grau 2"
        return "Obesidade Grau 3"

root = tkinter.Tk()
app = BMICalculator(root)
root.mainloop()