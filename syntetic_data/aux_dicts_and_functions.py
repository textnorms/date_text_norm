'''
    This file implements some auxiliary functions and dicts for the project.
'''

'''
    Dicts
'''
from collections import OrderedDict

'''
    This dict implements default values for each sample

'''
occurences_per_sample_dict = OrderedDict([
    ('DD/MM/YYYY',1),
    ('DD/MM',7),
    ('MM/YYYY',3)
])


'''
    Functions
'''
def combinations(lista, listb):
    '''
        Combinate two lists given its elements. Implementation obtained in:
        https://stackoverflow.com/questions/6499327/the-pythonic-way-to-generate-pairs
    '''
    return [ (i,j) for i in lista for j in listb ]