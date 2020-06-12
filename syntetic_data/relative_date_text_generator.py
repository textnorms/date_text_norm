'''
    This file implements a date text generation
    sample for all the classes
    the implementations for each sample
'''

'''
    Importing num2words module:
    https://github.com/savoirfairelinux/num2words
'''
from num2words import num2words


'''
    Importing dependencies from datetime module
'''
from datetime import datetime
from datetime import timedelta

'''
    Importing pandas module:
    https://github.com/pandas-dev/pandas
'''
import pandas as pd

'''
    Importing random dependencies
'''
from random import random
from random import randint
from random import sample

'''
    Importing dependencies from Collections
'''
from collections import OrderedDict

'''
    Importing authorial modules, further description about
    them can be found on their implementations.
'''
from .text_noise import text_noise_dict
from .lang_dicts import relative_date_formats_dict_collection
from .aux_dicts_and_functions import combinations

from .date_text_generator import DateTextGenerator

class RelativeDateTextGenerator(DateTextGenerator):
    '''
        This class relative date text generation for
        a number of samples defined by n_samples.
    '''
    def __init__(self,n_samples=100,
        text_noise_rate=0.0,
        max_noise_types_per_sample=3,
        max_noise_occurences_per_sample = 2,
        text_noise_methods=text_noise_dict,
        language='en'):

        self.n_samples = n_samples

        self.date_text_gen_methods = OrderedDict([
            ('Relative',relative_date_formats_dict_collection[language])
            ])

        self.text_error_rate = text_noise_rate
        self.text_noise_methods = text_noise_methods

        self.max_noise_occurences_per_sample = max_noise_occurences_per_sample
        self.max_noise_types_per_sample = max_noise_types_per_sample

    def generate_date_dataset(self):
        '''
            Generates the dataset for all the supported formats            
        '''

        returnable_dataset_list = [
                self._generate_single_date_dataset(
                sample_range=range(self.n_samples),
                date_text_gen_methods=self.date_text_gen_methods['Relative'])]

        return pd.concat(returnable_dataset_list,ignore_index=True)

    def _generate_single_date_dataset(self,sample_range,
        date_text_gen_methods,samples_per_method=1):
        '''
           Generates a pandas dataset for a given date_range, target format and its date
           text generation methods. With the samples_per_method variable is possible to
           increase the amount of date text formats per target.
        '''

        X = []
        method_ids = []
        noise_types = [] # N/A if has no noise, or the keys from text_noise_implementations
        y = []

        for sample in sample_range:
            
            # Sampling method and its ids
            for method_id,date_text_gen_method in self.sample_from_dict(date_text_gen_methods,
                samples_per_method):
                
                method_ids.append(
                    int(method_id)
                )

                text_sample,target = date_text_gen_method(sample)

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

                y.append(target) 

        dataset = pd.DataFrame(list(zip(method_ids,noise_types,X,y,len(X)*['Relative '])),
            columns=['Input Pattern','Noise Type','Input','Target','Target Format'])

        return dataset

    def generate_demo(self,sample=13):
        '''
            Generates a demo for all the text forms
            contained in the model for a given date.
        '''        
        methods = []
        generated_texts = []

        day,month, year = date.split('/')

        for method_id,date_text_gen_method in self.absolute_date_text_gen_methods.items():
        
            methods.append(method_id)
            generated_texts.append(date_text_gen_method(day,month,year))


        dataset = pd.DataFrame(list(zip(methods,generated_texts,[date]*len(self.absolute_date_text_gen_methods))),
            columns=['Input Pattern','Generated Text','Origin Sample'])

        return dataset