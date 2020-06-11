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
    'v':'u',
    '9':'g',
    'g':'9'
}
