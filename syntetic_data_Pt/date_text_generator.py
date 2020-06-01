from num2words import num2words
from datetime import datetime
from datetime import timedelta
import pandas as pd
from random import random
from random import randint
from random import sample
from .text_noise import text_noise_dict
from .date_text_formats import date_formats_dict

class DateTextGenerator():

    '''
    Essa classe implementa um gerador de texto sintético
    que usa como entrada datas no formato canônico e produz
    amostras em formatos textuais não canônicos. 
    E.g.:
        - Entrada: 01/05/2020
        - Saídas possíveis:
            - 01 de maio de 2020;
            - primeiro de maior de 2020;
            - primeiro de maio de dois mil e vinte;
            - primeiro do 05 de 2020;
                .
                .
                .
    '''
    def __init__(self,start_date='01/01/0001',
        end_date='31/12/2999',
        text_noise_rate=0.0,
        max_noise_types_per_sample=3,
        max_noise_occurences_per_sample = 2,
        text_gen_methods=date_formats_dict,
        text_noise_methods=text_noise_dict):

        self.start_date = datetime.strptime(start_date, "%d/%m/%Y")
        self.end_date = datetime.strptime(end_date, "%d/%m/%Y")

        self.date_range = self.generate_date_range(self.start_date,self.end_date)

        self.text_gen_methods = text_gen_methods

        self.text_error_rate = text_noise_rate
        self.text_noise_methods = text_noise_methods

        self.max_noise_occurences_per_sample = max_noise_occurences_per_sample
        self.max_noise_types_per_sample = max_noise_types_per_sample

    def generate_date_dataset(self):

        X = []
        method_ids = []
        noise_types = [] # N/A if has no noise, or the keys from text_noise_implementations

        for sample in self.date_range:
            
            # Sampling method and its ids
            method_id,date_text_gen_method = self.sample_from_dict(self.text_gen_methods)[0]

            day,month,year = sample.split('/')
            
            method_ids.append(
                method_id
            )

            text_sample = date_text_gen_method(day,month,year)

            noise_type = 'N/A'

            if random() < self.text_error_rate:
                # Applying noise
                text_sample,noise_type = self._apply_noise(text_sample)
            
            noise_types.append(
                noise_type    
            )

            X.append(
                text_sample
            )

        dataset = pd.DataFrame(list(zip(method_ids,noise_types,X,self.date_range)),
            columns=['Input Pattern','Noise Type','Input','Target'])

        return dataset

    def generate_demo(self,date='01/01/2020'):
        '''
            Generates a demo for all the text forms
            contained in the model for a given date.
        '''        
        methods = []
        generated_texts = []

        day,month, year = date.split('/')

        for method_id,date_text_gen_method in self.text_gen_methods.items():
        
            methods.append(method_id)
            generated_texts.append(date_text_gen_method(day,month,year))


        dataset = pd.DataFrame(list(zip(methods,generated_texts,[date]*len(self.text_gen_methods))),
            columns=['Input Pattern','Generated Text','Origin Sample'])

        return dataset

    def _apply_noise(self,input_text):
        '''
            Selects a random noise type and apply it to
            input_text. This function returns input_text
            with noise and the noise type applied.
        '''
        
        # Introducing some randomness to the proccess of selecting
        # the number of samples
        noise_types = randint(1,self.max_noise_types_per_sample)
        
        # This list will keep track of the noises applied to 
        # each sample and will be used to included to the final
        # dataframe 
        applied_noises = []

        for noise_type in sample(list(self.text_noise_methods.keys()),noise_types):
            noise_func = self.text_noise_methods[noise_type]
            
            # Defining the number of occurrences per sample
            noise_occurrences = randint(1,self.max_noise_occurences_per_sample)

            # Applying noise to multi samples
            input_text  = noise_func(input_text,noise_occurrences)

            applied_noises.append(noise_type)


        return input_text,applied_noises

    @staticmethod
    def sample_from_dict(dict_to_sample,n_samples=1):
        '''
            This method implements a form of sampling n_samples from
            a dict. This is code was inspired in the implementation
            described in:
            https://stackoverflow.com/questions/10125568/how-to-randomly-choose-multiple-keys-and-its-value-in-a-dictionary-python
        '''

        # Sampling n_samples keys
        keys_and_values = sample(dict_to_sample.items(), n_samples)
        
        # Returns the values and the keys corresponding
        # each sampled value
        return keys_and_values

    @staticmethod
    def generate_date_range (start_date,end_date,step=1):
        '''
           Implementa um range de datas com os dias que estão entre
           start_date e end_date. Implementação inspirada em:
            https://gist.github.com/ramhiser/989263a7a136601e3723
            e
            https://stackoverflow.com/questions/339007/how-to-pad-zeroes-to-a-string
        '''
        
        dates = []

        for d in range(0, (end_date - start_date).days + step, step):
            date_i = start_date + timedelta(days=d)
            
            dia = str(date_i.date().day).zfill(2)
            mes = str(date_i.date().month).zfill(2)
            ano = str(date_i.date().year).zfill(4)

            dates.append(f'{dia}/{mes}/{ano}')

        return dates