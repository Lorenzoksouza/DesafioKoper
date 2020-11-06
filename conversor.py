from num2words import num2words
from tkinter import *

LANG = 'pt-BR'

def numero_para_extenso(num_inicial):
    """
    Funçâo que converte numeros para seu formato por extenso com a entrada de um numero

    :param num_inicial: Double
    :return num_extenso: String
    """
    if num_inicial.find(".") != -1:
        num_inicial = num_inicial.replace(".", ",")

    if num_inicial.find(",") != -1:
        num_dividido = num_inicial.split(",")
        num_principal = int(num_dividido[0])
        num_decimal = int(num_dividido[1])
    else:
        num_principal = int(num_inicial)
        num_decimal = 0

    num_extenso = ""
    if num_principal != 0:
        num_extenso = num2words(num_principal, lang=LANG)
        if num_principal == 1:
            num_extenso = num_extenso + " real"
        if num_principal > 1:
            num_extenso = num_extenso + " reais"

    if num_decimal != 0:
        if num_principal > 0:
            num_extenso = num_extenso + " e "
        num_extenso = num_extenso + num2words(num_decimal, lang=LANG)
        if num_decimal == 1:
            num_extenso = num_extenso + " centavo"
        if num_decimal > 1:
            num_extenso = num_extenso + " centavos"

    return num_extenso


