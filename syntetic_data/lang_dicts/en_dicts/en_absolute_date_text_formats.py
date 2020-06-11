'''
    Este arquivo é responsável por especificar os formatos de dados que serão considerados
    por default para a geração de novos textos. 
    
    - A inclusão de novos formatos necessita apenas de declarar a função responsável pela sua
    geração e em seguida passar para o dicionário 'date_formats_dict' o nome da função
'''

from num2words import num2words
from .en_aux_dicts import extensive_months_dict
from .en_aux_dicts import shortened_months_dict

def all_extensive_numbers(day,month,year):
    '''
        Todos os dias em notação por extenso:
        E.g.:
        - um do um de dois mil
    '''
    input_day = num2words(int(day),lang='en')
    input_month = num2words(int(month),lang='en')
    input_year = num2words(int(year),lang='en')
    return f'{input_day} of {input_month} of {input_year}'

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
    input_day = num2words(int(day),lang='en')
    input_month = extensive_months_dict[month]
    input_year = num2words(int(year),lang='en')
    return f'{input_day} of {input_month} of {input_year}'

def text_shortmonth_text(day,month,year):
    '''
        Dia e ano escritos por extenso e mês
        escrito como o mês abreviado.
    '''
    input_day = num2words(int(day),lang='en')
    input_month = shortened_months_dict[month]
    input_year = num2words(int(year),lang='en')
    return f'{input_day} of {input_month} of {input_year}'

def format1(day,month,year):
    '''
        Date format 1 described as:
        "vinte e oito de abril de 2005" for the date 28/04/2005
    '''
    input_day = num2words(int(day),lang='en')
    input_month = extensive_months_dict[month]
    input_year = year
    return f'{input_day} of {input_month} of {input_year}'

def format2(day,month,year):
    '''
        Date format 2 described as:
        "vinte e oito de abr de dois mil e cinco" for the date 28/04/2005
    '''
    input_day = num2words(int(day),lang='en')
    input_month = shortened_months_dict[month]
    input_year = num2words(int(year),lang='en')
    return f'{input_day} of {input_month} of {input_year}'

def format3(day,month,year):
    '''
        Date format 3 described as:
        "vinte e oito de abril de dois mil e cinco" for the date 28/04/2005
    '''
    input_day = num2words(int(day),lang='en')
    input_month = extensive_months_dict[month]
    input_year = num2words(int(year),lang='en')
    return f'{input_day} of {input_month} of {input_year}'

def format4(day,month,year):
    '''
        Date format 4 described as:
        "vigésimo oitavo dia do mês quatro de dois mil e cinco" for the date 28/04/2005
    '''
    input_day = num2words(int(day),to='ordinal',lang='en')
    input_month = num2words(int(month),lang='en')
    input_year = num2words(int(year),lang='en')
    return f'{input_day} day of month {input_month} of {input_year}'

def format5(day,month,year):
    '''
        Date format 5 described as:
        "28 de Abril de 2005" for the date 28/04/2005
    '''
    input_day = day
    input_month = extensive_months_dict[month].capitalize()
    input_year = year
    return f'{input_day} of {input_month} of {input_year}'

def format6(day,month,year):
    '''
        Date format 6 described as:
        "28 de abril de dois mil e cinco" for the date 28/04/2005
    '''
    input_day = day
    input_month = extensive_months_dict[month]
    input_year = num2words(int(year),lang='en')
    return f'{input_day} of {input_month} of {input_year}'

def format7(day,month,year):
    '''
        Date format 7 described as:
        "28-04 de dois mil e cinco" for the date 28/04/2005
    '''
    input_day = day
    input_month = month
    input_year = num2words(int(year),lang='en')
    return f'{input_day}-{input_month} of {input_year}'

def format8(day,month,year):
    '''
        Date format 8 described as:
        "vinte e oito - 04 - 2005" for the date 28/04/2005
    '''
    input_day = num2words(int(day),lang='en')
    input_month = month
    input_year = year
    return f'{input_day} - {input_month} - {input_year}'

def format9(day,month,year):
    '''
        Date format 9 described as:
        "vinte e oito de abril - 2005" for the date 28/04/2005
    '''
    input_day = num2words(int(day),lang='en')
    input_month = extensive_months_dict[month]
    input_year = year
    return f'{input_day} of {input_month} - {input_year}'

def format10(day,month,year):
    '''
        Date format 10 described as:
        "28th de abril de 2005" for the date 28/04/2005
    '''
    input_day = day
    input_month = extensive_months_dict[month]
    input_year = year
    
    if input_day == 1 or input_day == '01' or input_day == '1':
        return f'{input_day}st of {input_month} of {input_year}'
    elif input_day == 2 or input_day == '02' or input_day == '2':
        return f'{input_day}nd of {input_month} of {input_year}'
    elif input_day == 3 or input_day == '03' or input_day == '3':
        return f'{input_day}rd of {input_month} of {input_year}'
    else:
        return f'{input_day}th of {input_month} of {input_year}'

def format11(day,month,year):
    '''
        Date format 11 described as:
        "28th - 04 - 2005" for the date 28/04/2005
    '''
    input_day = day
    input_month = month
    input_year = year
    
    if input_day == 1 or input_day == '01' or input_day == '1':
        return f'{input_day}st-{input_month}-{input_year}'
    elif input_day == 2 or input_day == '02' or input_day == '2':
        return f'{input_day}nd-{input_month}-{input_year}'
    elif input_day == 3 or input_day == '03' or input_day == '3':
        return f'{input_day}rd-{input_month}-{input_year}'
    else:
        return f'{input_day}th-{input_month}-{input_year}'

def format12(day,month,year):
    '''
        Date format 12 described as:
        "28th / 04 / 2005" for the date 28/04/2005
    '''
    input_day = day
    input_month = month
    input_year = year

    if input_day == 1 or input_day == '01' or input_day == '1':
        return f'{input_day}st/{input_month}/{input_year}'
    elif input_day == 2 or input_day == '02' or input_day == '2':
        return f'{input_day}nd/{input_month}/{input_year}'
    elif input_day == 3 or input_day == '03' or input_day == '3':
        return f'{input_day}rd/{input_month}/{input_year}'
    else:
        return f'{input_day}th/{input_month}/{input_year}'

def format13(day,month,year):
    '''
        Date format 13 described as:
        "28th / Abril / 2005" for the date 28/04/2005
    '''
    input_day = day
    input_month = extensive_months_dict[month].capitalize()
    input_year = year

    if input_day == 1 or input_day == '01' or input_day == '1':
        return f'{input_day}st/{input_month}/{input_year}'
    elif input_day == 2 or input_day == '02' or input_day == '2':
        return f'{input_day}nd/{input_month}/{input_year}'
    elif input_day == 3 or input_day == '03' or input_day == '3':
        return f'{input_day}rd/{input_month}/{input_year}'
    else:
        return f'{input_day}th/{input_month}/{input_year}'

def format14(day,month,year):
    '''
        Date format 14 described as:
        "28 / abril / 2005" for the date 28/04/2005
    '''
    input_day = day
    input_month = extensive_months_dict[month]
    input_year = year
    return f'{input_day}/{input_month}/{input_year}'

def format15(day,month,year):
    '''
        Date format 15 described as:
        "vinte e oito abril dois mil e cinco" for the date 28/04/2005
    '''
    input_day = num2words(int(day), lang='en')
    input_month = extensive_months_dict[month]
    input_year = num2words(int(year),lang='en')
    return f'{input_day} {input_month} {input_year}'

def format16(day,month,year):
    '''
        Date format 16 described as:
        "28 abril dois mil e cinco" for the date 28/04/2005
    '''
    input_day = day
    input_month = extensive_months_dict[month]
    input_year = num2words(int(year),lang='en')
    return f'{input_day} {input_month} {input_year}'

def format17(day,month,year):
    '''
        Date format 17 described as:
        "28/04 dois mil e cinco" for the date 28/04/2005
    '''
    input_day = day
    input_month = month
    input_year = num2words(int(year),lang='en')
    return f'{input_day}/{input_month} {input_year}'

def format18(day,month,year):
    '''
        Date format 18 described as:
        "28.04 dois mil e cinco" for the date 28/04/2005
    '''
    input_day = day
    input_month = month
    input_year = num2words(int(year),lang='en')
    return f'{input_day}.{input_month} {input_year}'


def format19(day,month,year):
    '''
        Date format 19 described as:
        "28-04 dois mil e cinco" for the date 28/04/2005
    '''
    input_day = day
    input_month = month
    input_year = num2words(int(year),lang='en')
    return f'{input_day}-{input_month} {input_year}'


def format20(day,month,year):
    '''
        Date format 20 described as:
        "vinte e oito/abril/dois mil e cinco" for the date 28/04/2005
    '''
    input_day = num2words(int(day),lang='en')
    input_month = extensive_months_dict[month]
    input_year = num2words(int(year),lang='en')
    return f'{input_day}/{input_month}/{input_year}'

def format21(day,month,year):
    '''
        Date format 21 described as:
        "28 do mês quatro de 2005" for the date 28/04/2005
    '''
    input_day = day
    input_month = num2words(int(month),lang='en')
    input_year = year
    return f'{input_day} of month {input_month} of {input_year}'

def format22(day,month,year):
    '''
        Date format 22 described as:
        "28-4-2005" for the date 28/04/2005
    '''
    input_day = day
    input_month = int(month)
    input_year = year
    return f'{input_day}-{input_month}-{input_year}'

def format23(day,month,year):
    '''
        Date format 23 described as:
        "28 - 4 - 2005" for the date 28/04/2005
    '''
    input_day = day
    input_month = int(month)
    input_year = year
    return f'{input_day} - {input_month} - {input_year}'

def format24(day,month,year):
    '''
        Date format 24 described as:
        "28-04-2005" for the date 28/04/2005
    '''
    input_day = day
    input_month = month
    input_year = year
    return f'{input_day}-{input_month}-{input_year}'

def format25(day,month,year):
    '''
        Date format 25 described as:
        "28 - 04 - 2005" for the date 28/04/2005
    '''
    input_day = day
    input_month = month
    input_year = year
    return f'{input_day} - {input_month} - {input_year}'

def format26(day,month,year):
    '''
        Date format 26 described as:
        "28-abril-2005" for the date 28/04/2005
    '''
    input_day = day
    input_month = extensive_months_dict[month]
    input_year = year
    return f'{input_day}-{input_month}-{input_year}'

def format27(day,month,year):
    '''
        Date format 27 described as:
        "28 - abril - 2005" for the date 28/04/2005
    '''
    input_day = day
    input_month =  extensive_months_dict[month]
    input_year = year
    return f'{input_day} - {input_month} - {input_year}'

def format28(day,month,year):
    '''
        Date format 28 described as:
        "28-abr-2005" for the date 28/04/2005
    '''
    input_day = day
    input_month =  shortened_months_dict[month]
    input_year = year
    return f'{input_day}-{input_month}-{input_year}'

def format29(day,month,year):
    '''
        Date format 29 described as:
        "28 - abr - 2005" for the date 28/04/2005
    '''
    input_day = day
    input_month =  shortened_months_dict[month]
    input_year = year
    return f'{input_day} - {input_month} - {input_year}'

def format30(day,month,year):
    '''
        Date format 30 described as:
        "28.4.2005" for the date 28/04/2005
    '''
    input_day = day
    input_month = int(month)
    input_year = year
    return f'{input_day}.{input_month}.{input_year}'

def format31(day,month,year):
    '''
        Date format 31 described as:
        "28 . 4 . 2005" for the date 28/04/2005
    '''
    input_day = day
    input_month = int(month)
    input_year = year
    return f'{input_day} . {input_month} . {input_year}'

def format32(day,month,year):
    '''
        Date format 32 described as:
        "28.04.2005" for the date 28/04/2005
    '''
    input_day = day
    input_month = month
    input_year = year
    return f'{input_day}.{input_month}.{input_year}'

def format33(day,month,year):
    '''
        Date format 33 described as:
        "28 . 04 . 2005" for the date 28/04/2005
    '''
    input_day = day
    input_month = month
    input_year = year
    return f'{input_day} . {input_month} . {input_year}'

def format34(day,month,year):
    '''
        Date format 34 described as:
        "28.abril.2005" for the date 28/04/2005
    '''
    input_day = day
    input_month = extensive_months_dict[month]
    input_year = year
    return f'{input_day}.{input_month}.{input_year}'

def format35(day,month,year):
    '''
        Date format 35 described as:
        "28 . abril . 2005" for the date 28/04/2005
    '''
    input_day = day
    input_month = extensive_months_dict[month]
    input_year = year
    return f'{input_day} . {input_month} . {input_year}'

def format36(day,month,year):
    '''
        Date format 36 described as:
        "28.abr.2005" for the date 28/04/2005
    '''
    input_day = day
    input_month = shortened_months_dict[month]
    input_year = year
    return f'{input_day}.{input_month}.{input_year}'

def format37(day,month,year):
    '''
        Date format 37 described as:
        "28 . abr . 2005" for the date 28/04/2005
    '''
    input_day = day
    input_month = shortened_months_dict[month]
    input_year = year
    return f'{input_day} . {input_month} . {input_year}'

def format38(day,month,year):
    '''
        Date format 38 described as:
        "28/04/2005" for the date 28/04/2005
    '''
    input_day = day
    input_month = month
    input_year = year
    return f'{input_day}/{input_month}/{input_year}'

def format39(day,month,year):
    '''
        Date format 39 described as:
        "28 / 04 / 2005" for the date 28/04/2005
    '''
    input_day = day
    input_month = month
    input_year = year
    return f'{input_day} / {input_month} / {input_year}'

def format40(day,month,year):
    '''
        Date format 40 described as:
        "28 / abril / 2005" for the date 28/04/2005
    '''
    input_day = int(day)
    input_month = extensive_months_dict[month]
    input_year = int(year)
    return f'{input_day}/{input_month}/{input_year}'

def format41(day,month,year):
    '''
        Date format 41 described as:
        "28 / abril / 2005" for the date 28/04/2005
    '''
    input_day = int(day)
    input_month = extensive_months_dict[month]
    input_year = int(year)
    return f'{input_day} / {input_month} / {input_year}'

def format42(day,month,year):
    '''
        Date format 42 described as:
        "28/abr/2005" for the date 28/04/2005
    '''
    input_day = int(day)
    input_month = shortened_months_dict[month]
    input_year = int(year)
    return f'{input_day}/{input_month}/{input_year}'

def format43(day,month,year):
    '''
        Date format 43 described as:
        "28 / abr / 2005" for the date 28/04/2005
    '''
    input_day = int(day)
    input_month = shortened_months_dict[month]
    input_year = int(year)
    return f'{input_day} / {input_month} / {input_year}'

def format44(day,month,year):
    '''
        Date format 44 described as:
        "28/4/2005" for the date 28/04/2005
    '''
    input_day = int(day)
    input_month = int(month)
    input_year = int(year)
    return f'{input_day}/{input_month}/{input_year}'

def format45(day,month,year):
    '''
        Date format 45 described as:
        "28 / 4 / 2005" for the date 28/04/2005.
    '''
    input_day = int(day)
    input_month = int(month)
    input_year = int(year)
    return f'{input_day} / {input_month} / {input_year}'

'''
    Não se esqueça de incluir aqui as funções declaradas para gerar datas completas.
'''
absolute_date_formats_dict = {
    '1':format1,
    '2':format2,
    '3':format3,
    '4':format4,
    '5':format5,
    '6':format6,
    '7':format7,
    '8':format8,
    '9':format9,
    '10':format10,
    '11':format11,
    '12':format12,
    '13':format13,
    '14':format14,
    '15':format15,
    '16':format16,
    '17':format17,
    '18':format18,
    '19':format19,
    '20':format20,
    '21':format21,
    '22':format22,
    '23':format23,
    '24':format24,
    '25':format25,
    '26':format26,
    '27':format27,
    '28':format28,
    '29':format29,
    '30':format30,
    '31':format31,
    '32':format32,
    '33':format33,
    '34':format34,
    '35':format35,
    '36':format36,
    '37':format37,
    '38':format38,
    '39':format39,
    '40':format40,
    '41':format41,
    '42':format42,
    '43':format43,
    '44':format44,
    '45':format45,
}
