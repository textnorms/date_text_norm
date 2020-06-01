'''
    Este arquivo contêm dicionários auxiliares para a construção
    de datas por extenso em EN. Em especial meses.
'''

'''
    Meses escritos por extenso
'''
extensive_months_dict = {
    '01': 'january',
    '02': 'february',
    '03': 'march',
    '04': 'april',
    '05': 'may',
    '06': 'june',
    '07': 'july',
    '08': 'august',
    '09': 'september',
    '10': 'october',
    '11': 'november',
    '12': 'december'
}

'''
    Meses escritos por extenso abreviados
    para EN.
'''
shortened_months_dict = {
    '01': 'jan',
    '02': 'feb',
    '03': 'mar',
    '04': 'apr',
    '05': 'may',
    '06': 'jun',
    '07': 'jul',
    '08': 'aug',
    '09': 'sep',
    '10': 'oct',
    '11': 'nov',
    '12': 'dec'
}

'''
    Dicionário para simular erros de OCR, dde modo que letras
    semelhantes podem ser trocadas por números similares ou letras
    que possuem formato parecido podem ser trocadas entre-si.
'''
lookalike_chars = {
    'o':'0',
    '0':'o',
    'c':'ç',
    'ç':'c',
    'l':'i',
    'i':'l',
    'n':'m',
    'm':'n',
    'u':'v',
    'v':'u'
}
