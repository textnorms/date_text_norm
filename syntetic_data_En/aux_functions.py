'''
    This file implements some auxiliary functions for the project.
'''

def combinations(lista, listb):
    '''
        Combinate two lists given its elements. Implementation obtained in:
        https://stackoverflow.com/questions/6499327/the-pythonic-way-to-generate-pairs
    '''
    return [ (i,j) for i in lista for j in listb ]