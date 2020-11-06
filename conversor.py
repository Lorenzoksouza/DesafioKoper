from num2words import num2words

LANG = 'pt-BR'


def numero_para_extenso(num_inicial):
    """

    :param num_inicial: Double
    :return num_extenso: String
    """
    num_extenso = num2words(num_inicial, LANG)
    return num_extenso
