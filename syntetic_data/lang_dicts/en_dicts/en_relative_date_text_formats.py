'''
    This file implements the relative dates format for a given date
'''

from num2words import num2words

def format1(sample):
    '''
        converts -7d to 7 days ago
    '''
    sample_text = sample

    if sample > 1:
        return f'{sample_text} days ago',f'-{sample}d'
    else:
        return f'{sample_text} day ago',f'-{sample}d'

def format2(sample):
    '''
        Converts 7d to seven days ago
    '''
    sample_text = num2words(sample,lang='en')

    if sample > 1:
        return f'{sample_text} days ago',f'-{sample}d'
    else:
        return f'{sample_text} day ago',f'-{sample}d'
    

def format3(sample):
    '''
        converts -7m to 7 months ago
    '''
    sample_text = sample

    if sample > 1:
        return f'{sample_text} months ago',f'-{sample}m'
    else:
        return f'{sample_text} month ago',f'-{sample}m'

def format4(sample):
    '''
        Converts -7m to seven months ago
    '''
    sample_text = num2words(sample,lang='en')

    if sample > 1:
        return f'{sample_text} months ago',f'-{sample}m'
    else:
        return f'{sample_text} month ago',f'-{sample}m'
    

def format5(sample):
    '''
        converts -7y to 7 years ago
    '''
    sample_text = sample

    if sample > 1:
        return f'{sample_text} years ago',f'-{sample}y'
    else:
        return f'{sample_text} year ago',f'-{sample}y'

def format6(sample):
    '''
        Converts -7y to seven days ago
    '''
    sample_text = num2words(sample,lang='en')

    if sample > 1:
        return f'{sample_text} days ago',f'-{sample}y'
    else:
        return f'{sample_text} day ago',f'-{sample}y'

def format5(sample):
    '''
        converts -7y to 7 years ago
    '''
    sample_text = sample

    if sample > 1:
        return f'{sample_text} years ago',f'-{sample}y'
    else:
        return f'{sample_text} year ago',f'-{sample}y'

def format6(sample):
    '''
        Converts -7y to seven days ago
    '''
    sample_text = num2words(sample,lang='en')

    if sample > 1:
        return f'{sample_text} days ago',f'-{sample}y'
    else:
        return f'{sample_text} day ago',f'-{sample}y'


relative_date_formats_dict = {
    '1':format1,
    '2':format2,
    '3':format3,
    '4':format4
}
