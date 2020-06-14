'''
    This file implements the relative dates format for a given sample
'''

from num2words import num2words

def format1(sample):
    '''
        Implements pair -7d and há 7 dias
    '''
    sample_text = sample

    if sample > 1:
        return f'há {sample_text} dias',f'-{sample}d'
    else:
        return f'há {sample_text} dia',f'-{sample}d'

def format2(sample):
    '''
        Implements pair -7m and há 7 meses
    '''
    sample_text = sample

    if sample > 1:
        return f'há {sample_text} meses',f'-{sample}m'
    else:
        return f'há {sample_text} mês',f'-{sample}m'

def format3(sample):
    '''
        Implements pair -7y and há 7 anos
    '''
    sample_text = sample

    if sample > 1:
        return f'há {sample_text} anos',f'-{sample}y'
    else:
        return f'há {sample_text} ano',f'-{sample}y'
    
def format4(sample):
    '''
        Implements pair -7d and há sete dias
    '''
    sample_text = num2words(sample,lang='pt_BR')

    if sample > 1:
        return f'há {sample_text} dias',f'-{sample}d'
    else:
        return f'há {sample_text} dia',f'-{sample}d'

def format5(sample):
    '''
        Implements pair -7m and há sete meses
    '''
    sample_text = num2words(sample,lang='pt_BR')

    if sample > 1:
        return f'há {sample_text} meses',f'-{sample}m'
    else:
        return f'há {sample_text} mês',f'-{sample}m'

def format6(sample):
    '''
        Implements pair -7y and há sete anos
    '''
    sample_text = num2words(sample,lang='pt_BR')

    if sample > 1:
        return f'há {sample_text} anos',f'-{sample}y'
    else:
        return f'há {sample_text} ano',f'-{sample}y'
    
def format7(sample):
    '''
        Implements pair -7d and faz 7 dias
    '''
    sample_text = sample

    if sample > 1:
        return f'faz {sample_text} dias',f'-{sample}d'
    else:
        return f'faz {sample_text} dia',f'-{sample}d'

def format8(sample):
    '''
        Implements pair -7m and faz 7 meses
    '''
    sample_text = sample

    if sample > 1:
        return f'faz {sample_text} meses',f'-{sample}m'
    else:
        return f'faz {sample_text} mês',f'-{sample}m'

def format9(sample):
    '''
        Implements pair -7y and faz 7 anos
    '''
    sample_text = sample

    if sample > 1:
        return f'faz {sample_text} anos',f'-{sample}y'
    else:
        return f'faz {sample_text} ano',f'-{sample}y'
    
def format10(sample):
    '''
        Implements pair -7d and faz sete dias
    '''
    sample_text = num2words(sample,lang='pt_BR')

    if sample > 1:
        return f'faz {sample_text} dias',f'-{sample}d'
    else:
        return f'faz {sample_text} dia',f'-{sample}d'

def format11(sample):
    '''
        Implements pair -7m and faz sete meses
    '''
    sample_text = num2words(sample,lang='pt_BR')

    if sample > 1:
        return f'faz {sample_text} meses',f'-{sample}m'
    else:
        return f'faz {sample_text} mês',f'-{sample}m'

def format12(sample):
    '''
        Implements pair -7y and faz sete anos
    '''
    sample_text = num2words(sample,lang='pt_BR')

    if sample > 1:
        return f'faz {sample_text} anos',f'-{sample}y'
    else:
        return f'faz {sample_text} ano',f'-{sample}y'

def format13(sample):
    '''
        Implements pair 7d and por 7 dias
    '''
    sample_text = sample

    if sample > 1:
        return f'por {sample_text} dias',f'{sample}d'
    else:
        return f'por {sample_text} dia',f'{sample}d'

def format14(sample):
    '''
        Implements pair 7m and por 7 meses
    '''
    sample_text = sample

    if sample > 1:
        return f'por {sample_text} meses',f'{sample}m'
    else:
        return f'por {sample_text} mês',f'{sample}m'

def format15(sample):
    '''
        Implements pair 7y and por 7 anos
    '''
    sample_text = sample

    if sample > 1:
        return f'por {sample_text} anos',f'{sample}y'
    else:
        return f'por {sample_text} ano',f'{sample}y'
    
def format16(sample):
    '''
        Implements pair 7d and por sete dias
    '''
    sample_text = num2words(sample,lang='pt_BR')

    if sample > 1:
        return f'por {sample_text} dias',f'{sample}d'
    else:
        return f'por {sample_text} dia',f'{sample}d'

def format17(sample):
    '''
        Implements pair 7m and por sete meses
    '''
    sample_text = num2words(sample,lang='pt_BR')

    if sample > 1:
        return f'por {sample_text} meses',f'{sample}m'
    else:
        return f'por {sample_text} mês',f'{sample}m'

def format18(sample):
    '''
        Implements pair 7y and por sete anos
    '''
    sample_text = num2words(sample,lang='pt_BR')

    if sample > 1:
        return f'por {sample_text} anos',f'{sample}y'
    else:
        return f'por {sample_text} ano',f'{sample}y'

def format19(sample):
    '''
        Implements pair 7d and durante 7 dias
    '''
    sample_text = sample

    if sample > 1:
        return f'durante {sample_text} dias',f'{sample}d'
    else:
        return f'durante {sample_text} dia',f'{sample}d'

def format20(sample):
    '''
        Implements pair 7m and durante 7 meses
    '''
    sample_text = sample

    if sample > 1:
        return f'durante {sample_text} meses',f'{sample}m'
    else:
        return f'durante {sample_text} mês',f'{sample}m'

def format21(sample):
    '''
        Implements pair 7y and durante 7 anos
    '''
    sample_text = sample

    if sample > 1:
        return f'durante {sample_text} anos',f'{sample}y'
    else:
        return f'durante {sample_text} ano',f'{sample}y'
    
def format22(sample):
    '''
        Implements pair 7d and durante sete dias
    '''
    sample_text = num2words(sample,lang='pt_BR')

    if sample > 1:
        return f'durante {sample_text} dias',f'{sample}d'
    else:
        return f'durante {sample_text} dia',f'{sample}d'

def format23(sample):
    '''
        Implements pair 7m and durante sete meses
    '''
    sample_text = num2words(sample,lang='pt_BR')

    if sample > 1:
        return f'durante {sample_text} meses',f'{sample}m'
    else:
        return f'durante {sample_text} mês',f'{sample}m'

def format24(sample):
    '''
        Implements pair 7y and durante sete anos
    '''
    sample_text = num2words(sample,lang='pt_BR')

    if sample > 1:
        return f'durante {sample_text} anos',f'{sample}y'
    else:
        return f'durante {sample_text} ano',f'{sample}y'

def format25(sample):
    '''
        Implements pair 7d and ao 7º dia
    '''
    sample_text = sample

    return f'durante {sample_text}º dia',f'{sample}d'

def format26(sample):
    '''
        Implements pair 7m and ao 7º mês
    '''
    sample_text = sample

    return f'ao {sample_text}º mês',f'{sample}m'

def format27(sample):
    '''
        Implements pair 7y and ao 7º ano
    '''
    sample_text = sample

    return f'ao {sample_text}º ano',f'{sample}y'
    
def format28(sample):
    '''
        Implements pair 7d and ao sétimo dia
    '''
    sample_text = num2words(sample,lang='pt_BR',ordinal=True)

    return f'ao {sample_text} dia',f'{sample}d'

def format29(sample):
    '''
        Implements pair 7m ao sétimo mês
    '''
    sample_text = num2words(sample,lang='pt_BR',ordinal=True)

    return f'ao {sample_text} mês',f'{sample}m'

def format30(sample):
    '''
        Implements pair 7y and ao sétimo ano
    '''
    sample_text = num2words(sample,lang='pt_BR',ordinal=True)

    return f'ao {sample_text} ano',f'{sample}y'


def format31(sample):
    '''
        Implements pair -7d and 7 dias atrás
    '''
    sample_text = sample

    if sample > 1:
        return f'{sample_text} dias atrás',f'-{sample}d'
    else:
        return f'{sample_text} dia atrás',f'-{sample}d'

def format32(sample):
    '''
        Implements pair -7m and 7 meses atrás
    '''
    sample_text = sample

    if sample > 1:
        return f'{sample_text} meses atrás',f'-{sample}m'
    else:
        return f'{sample_text} mês atrás',f'-{sample}m'

def format33(sample):
    '''
        Implements pair -7y and 7 anos atrás
    '''
    sample_text = sample

    if sample > 1:
        return f'{sample_text} anos atrás',f'-{sample}y'
    else:
        return f'{sample_text} ano atrás',f'-{sample}y'
    
def format34(sample):
    '''
        Implements pair -7d and sete dias atrás
    '''
    sample_text = num2words(sample,lang='pt_BR')

    if sample > 1:
        return f'{sample_text} dias atrás',f'-{sample}d'
    else:
        return f'{sample_text} dia atrás',f'-{sample}d'

def format35(sample):
    '''
        Implements pair -7m and sete meses atrás
    '''
    sample_text = num2words(sample,lang='pt_BR')

    if sample > 1:
        return f'{sample_text} meses atrás',f'-{sample}m'
    else:
        return f'{sample_text} mês atrás',f'-{sample}m'

def format36(sample):
    '''
        Implements pair -7y and sete anos atrás
    '''
    sample_text = num2words(sample,lang='pt_BR')

    if sample > 1:
        return f'{sample_text} anos atrás',f'-{sample}y'
    else:
        return f'{sample_text} ano atrás',f'-{sample}y'


'''
    Including  the text generation formats functions in a dict as specified
    below. Always remember to include it in a format as soon as you create new
    formats
'''
relative_date_formats_dict = {
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
    '36':format36
}