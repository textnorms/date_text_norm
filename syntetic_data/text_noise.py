'''
    Este arquivo implementa a criação de ruído para entradas de texto, 
    como é o caso de erros de caracteres parecidos ou caracteres faltantes.
'''

from .noise_dicts import lookalike_chars
from random import sample
from collections import OrderedDict

def findAllOccurrences(s, ch):
    '''
        Encontra todas as ocorrências de uma letra em uma dada
        string. Código copiado de:
        https://stackoverflow.com/questions/13009675/find-all-the-occurrences-of-a-character-in-a-string
    '''
    return [i for i, letter in enumerate(s) if letter == ch]

def lookalike_replace_noise(input_text,K):
    '''
        Essa função troca K caracteres de uma string por caracteres que
        podem ser semelhantes dadas algumas fontes específicas.
    '''
    
    # Procurando dentre os caracteres que ocorrem, quais são
    # os que são candidatos à serem trocados
    chars_to_replace = list(lookalike_chars.keys())
    
    replace_candidates = OrderedDict()

    for char in chars_to_replace:

        char_occurencies = findAllOccurrences(input_text,char)

        if len(char_occurencies) > 0: replace_candidates[char] = char_occurencies

    # Alterando estes caracteres de forma aleatória
    K_counter = 0
    input_text_as_list = list(input_text)
    
    while(K_counter < K):

        candidate_chars = list(replace_candidates.keys())
        
        try:
            char2replace = sample(candidate_chars,1)[0]
        except:
            break

        locations = replace_candidates[char2replace]

        try:
            location_to_replace = sample(locations,1)[0]
        except:
            continue

        # Removing the just used key 
        locations.remove(location_to_replace)

        # Obtaining the new char from char2replpace dict
        new_char = lookalike_chars[char2replace]


        if len(locations) < 1:
            # Removing key if has no more locations
            replace_candidates.pop(char2replace,None)

        # Inserting new char to target string
        input_text_as_list[location_to_replace] = new_char
        
        # Counter incrementing
        K_counter += 1
    
    return "".join(input_text_as_list)


def unexpected_space_noise(input_text,K):
    '''
        Given an input text, k random spaces will
        be inserted between non space chars, creating
        noisy texts with random splitting.
    '''
    # Initializinng counter and creating aux variable
    K_count = 0
    new_text = input_text
    
    while(K_count<K):
        # Obtaining the split point for the string
        split_point = sample(range(len(new_text)),1)[0]

        # Skipping operation the if value is a ' ' or is the beggining or the end of seq
        if new_text[split_point] == ' ' or split_point==0 or split_point == len(text_noise_dict):
            
            continue
        
        # Spliting list to insert noise data
        new_text = new_text[:split_point] + ' ' + new_text[split_point:]
        
        K_count+=1

    return new_text


def remove_char_noise(input_text,K):
    '''
        This function removes K random chars from the text input.
    '''
    # Converting the input to a list to
    # allow removing chars
    input_text_as_list = list(input_text)
    
    for k in range(K):
        index_to_remove = sample(range(len(input_text_as_list)),1)[0]
        
        del input_text_as_list[index_to_remove]

    return "".join(input_text_as_list)


'''
    This dict exports all the implemented noise
    functions implemented in this file for
    further usage on the main class
'''
text_noise_dict = {
    'lookalike_replace_noise':lookalike_replace_noise,
    'unexpected_space_noise':unexpected_space_noise,
    'remove_char_noise':remove_char_noise
}