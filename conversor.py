from num2words import num2words

LANG = 'pt-BR'


def numero_para_extenso(num_inicial):
    """

    :param num_inicial: Double
    :return num_extenso: String
    """
    num_inicial = str(num_inicial)
    print(num_inicial)
    if num_inicial.find(".") != -1:
        num_dividido = num_inicial.split(".")
        num_principal = num_dividido[0]
        num_decimal = num_dividido[1]
        print(num_principal, num_decimal)

    num_extenso = num2words(num_inicial, lang=LANG)
    return num_extenso
