from num2words import num2words
from tkinter import *


def numero_para_extenso(num_inicial="0"):
    """
    Funçâo que converte numeros para seu formato por extenso com a entrada de um numero

    :param num_inicial: Double
    :return num_extenso: String
    """
    LANG = 'pt-BR'
    if num_inicial != '':
        if num_inicial.find(",") != -1:
            num_inicial = num_inicial.replace(",", ".")
        # Verificação do input para ver se é numerico
        try:
            var = float(num_inicial)
        except ValueError:
            return ("Isso não é um número")
        # Identificação de casas decimais
        if num_inicial.find(".") != -1:
            # Divisão do numero em antes e depois da virgula
            num_dividido = num_inicial.split(".")
            num_principal = int(num_dividido[0])
            num_decimal = int(num_dividido[1])
        else:
            num_principal = int(num_inicial)
            num_decimal = 0

        # inicialização da variavel que vai guardar numero por extenso
        num_extenso = ""

        # Verificação da primeira parte do número
        if num_principal != 0:
            num_extenso = num2words(num_principal, lang=LANG)
            if num_principal == 1:
                num_extenso = num_extenso + " real"
            if num_principal > 1:
                num_extenso = num_extenso + " reais"

        # Verificação da sugunda parte do número
        if num_decimal != 0:
            if num_principal > 0:
                num_extenso = num_extenso + " e "
            num_extenso = num_extenso + num2words(num_decimal, lang=LANG)
            if num_decimal == 1:
                num_extenso = num_extenso + " centavo"
            if num_decimal > 1:
                num_extenso = num_extenso + " centavos"

        # Retorno do numero ja com as nomenclaturas
        return num_extenso


# Classe para uma tela simples para melhor visualização e utilização
class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")

        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Conversor de numero para extenso")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.numeroLabel = Label(self.segundoContainer, text="Numero", font=self.fontePadrao)
        self.numeroLabel.pack(side=LEFT)

        self.numero = Entry(self.segundoContainer)
        self.numero["width"] = 30
        self.numero["font"] = self.fontePadrao
        self.numero.pack(side=LEFT)

        self.converter = Button(self.quartoContainer)
        self.converter["text"] = "Converter"
        self.converter["font"] = ("Calibri", "8")
        self.converter["width"] = 12
        self.converter["command"] = self.converter_numero
        self.converter.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    def converter_numero(self):
        num = self.numero.get()
        num_extenso = numero_para_extenso(num)
        self.mensagem["text"] = num_extenso


root = Tk()
Application(root)
root.mainloop()
