'''
    Este arquivo é responsável por especificar os formatos de dados que serão considerados
    por default para a geração de novos textos. 
    
    - A inclusão de novos formatos necessita apenas de declarar a função responsável pela sua
    geração e em seguida passar para o dicionário 'date_formats_dict' o nome da função
'''

from num2words import num2words
from .aux_dicts import extensive_months_dict
from .aux_dicts import shortened_months_dict

def all_extensive_numbers(day,month,year):
    '''
        Todos os dias em notação por extenso:
        E.g.:
        - um do um de dois mil
    '''
    input_day = num2words(int(day),lang='pt_BR')
    input_month = num2words(int(month),lang='pt_BR')
    input_year = num2words(int(year),lang='pt_BR')

    return f'{input_day} do {input_month} de {input_year}'


def dot_as_sep(day,month,year):
    '''
        Alterando o separador
        para um ponto ao invés do / 
    '''
    return f'{day}.{month}.{year}'


def text_fullmonth_text(day,month,year):
    '''
        Dia e ano escritos por extenso e mês
        escrito como o mês por extenso.
    '''
    input_day = num2words(int(day),lang='pt_BR')
    input_month = extensive_months_dict[month]
    input_year = num2words(int(year),lang='pt_BR')

    return f'{input_day} de {input_month} de {input_year}'

def text_shortmonth_text(day,month,year):
    '''
        Dia e ano escritos por extenso e mês
        escrito como o mês abreviado.
    '''
    
    input_day = num2words(int(day),lang='pt_BR')
    input_month = shortened_months_dict[month]
    input_year = num2words(int(year),lang='pt_BR')

    return f'{input_day} de {input_month} de {input_year}'


'''
    Não se esqueça de incluir aqui as funções declaradas para gerar datas completas.
'''
date_formats_dict = {
    '1':all_extensive_numbers,
    '2':dot_as_sep,
    '3':text_fullmonth_text,
    '4':text_shortmonth_text
}