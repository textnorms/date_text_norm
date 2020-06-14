'''
    This file implements the relative dates format for a given date
'''

from num2words import num2words

def format1(sample):
    '''
        Implements pair -7d and 7 days ago
    '''
    sample_text = sample

    if sample > 1:
        return f'{sample_text} days ago',f'-{sample}d'
    else:
        return f'{sample_text} day ago',f'-{sample}d'

def format2(sample):
    '''
        Implements pair -7d and seven days ago
    '''
    sample_text = num2words(sample,lang='en')

    if sample > 1:
        return f'{sample_text} days ago',f'-{sample}d'
    else:
        return f'{sample_text} day ago',f'-{sample}d'
    

def format3(sample):
    '''
        Implements pair -7m and 7 months ago
    '''
    sample_text = sample

    if sample > 1:
        return f'{sample_text} months ago',f'-{sample}m'
    else:
        return f'{sample_text} month ago',f'-{sample}m'

def format4(sample):
    '''
        Implements pair -7m and seven months ago
    '''
    sample_text = num2words(sample,lang='en')

    if sample > 1:
        return f'{sample_text} months ago',f'-{sample}m'
    else:
        return f'{sample_text} month ago',f'-{sample}m'
    

def format5(sample):
    '''
        Implements pair -7y and 7 years ago
    '''
    sample_text = sample

    if sample > 1:
        return f'{sample_text} years ago',f'-{sample}y'
    else:
        return f'{sample_text} year ago',f'-{sample}y'

def format6(sample):
    '''
        Implements pair -7y and seven years ago
    '''
    sample_text = num2words(sample,lang='en')

    if sample > 1:
        return f'{sample_text} years ago',f'-{sample}y'
    else:
        return f'{sample_text} year ago',f'-{sample}y'

def format7(sample):
    '''
        Implements pair 7d and for 7 days
    '''
    sample_text = sample

    if sample > 1:
        return f'for {sample_text} days',f'{sample}d'
    else:
        return f'for {sample_text} day',f'{sample}d'

def format8(sample):
    '''
        Implements pair 7d and for seven days
    '''
    sample_text = num2words(sample,lang='en')

    if sample > 1:
        return f'for {sample_text} days',f'{sample}d'
    else:
        return f'for {sample_text} day',f'{sample}d'

def format9(sample):
    '''
        Implements pair 7m and for 7 months
    '''

    sample_text  = sample

    if sample > 1:
        return f'for {sample_text} months',f'{sample}m'
    else:
        return f'for {sample_text} month',f'{sample}m'

def format10(sample):
    '''
        Implements pair 7m and for seven months
    '''
    sample_text = num2words(sample,lang='en')

    if sample > 1:
        return f'for {sample_text} months',f'{sample}m'
    else:
        return f'for {sample_text} month',f'{sample}m'

def format11(sample):
    '''
        Implements pair 7y and for 7 years
    '''

    sample_text  = sample

    if sample > 1:
        return f'for {sample_text} years',f'{sample}y'
    else:
        return f'for {sample_text} year',f'{sample}y'

def format12(sample):
    '''
        Implements pair 7y and for seven years
    '''
    sample_text = num2words(sample,lang='en')

    if sample > 1:
        return f'for {sample_text} years',f'{sample}y'
    else:
        return f'for {sample_text} year',f'{sample}y'


def format13(sample):
    '''
        Implements pair 7d and during 7 days
    '''

    sample_text  = sample

    if sample > 1:
        return f'during {sample_text} days',f'{sample}d'
    else:
        return f'during {sample_text} day',f'{sample}d'

def format14(sample):
    '''
        Implements pair 7d and during seven days
    '''
    sample_text = num2words(sample,lang='en')

    if sample > 1:
        return f'during {sample_text} days',f'{sample}d'
    else:
        return f'during {sample_text} day',f'{sample}d'

def format15(sample):
    '''
        Implements pair 7m and during 7 months
    '''

    sample_text  = sample

    if sample > 1:
        return f'during {sample_text} months',f'{sample}m'
    else:
        return f'during {sample_text} month',f'{sample}m'

def format16(sample):
    '''
        Implements pair 7m and during seven months
    '''
    sample_text = num2words(sample,lang='en')

    if sample > 1:
        return f'during {sample_text} months',f'{sample}m'
    else:
        return f'during {sample_text} month',f'{sample}m'

def format17(sample):
    '''
        Implements pair 7y and during 7 years
    '''

    sample_text  = sample

    if sample > 1:
        return f'during {sample_text} years',f'{sample}y'
    else:
        return f'during {sample_text} year',f'{sample}y'

def format18(sample):
    '''
        Implements pair 7y and during seven years
    '''
    sample_text = num2words(sample,lang='en')

    if sample > 1:
        return f'during {sample_text} years',f'{sample}y'
    else:
        return f'during {sample_text} year',f'{sample}y'

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
    '18':format18
}