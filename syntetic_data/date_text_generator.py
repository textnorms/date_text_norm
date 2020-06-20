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
from .lang_dicts import absolute_date_formats_dict_collection
from .lang_dicts import incomplete_mm_yyyy_date_formats_dict_collection
from .lang_dicts import incomplete_dd_mm_date_formats_dict_collection
from .aux_dicts_and_functions import combinations
from .aux_dicts_and_functions import occurences_per_sample_dict

class DateTextGenerator():
    '''
        This class implements date-text generation for
        a period defined by start_date and end_date.
        You can specify noise rate, date text formats per sample
        and language.
    '''
    def __init__(self,start_date='01/01/0001',
        end_date='31/12/2999',
        text_noise_rate=0.0,
        max_noise_types_per_sample=3,
        max_noise_occurences_per_sample = 2,
        occurences_per_sample_dict=occurences_per_sample_dict,
        text_noise_methods=text_noise_dict,
        language='en'):

        self.start_date = datetime.strptime(start_date, "%d/%m/%Y")
        self.end_date = datetime.strptime(end_date, "%d/%m/%Y")
        self.date_range = self.generate_date_range(self.start_date,self.end_date)

        self.occurences_per_sample_dict = occurences_per_sample_dict
        self.date_text_gen_methods = OrderedDict([
            ('DD/MM/YYYY',absolute_date_formats_dict_collection[language]),
            ('DD/MM',incomplete_dd_mm_date_formats_dict_collection[language]),
            ('MM/YYYY',incomplete_mm_yyyy_date_formats_dict_collection[language])
        ])

        self.text_error_rate = text_noise_rate
        self.text_noise_methods = text_noise_methods

        self.max_noise_occurences_per_sample = max_noise_occurences_per_sample
        self.max_noise_types_per_sample = max_noise_types_per_sample

    def generate_date_dataset(self):
        '''
            Generates the dataset for all the supported formats            
        '''

        date_range_df = pd.DataFrame(self.date_range,columns=['sample','pattern'])

        returnable_dataset_list = [
                self._generate_single_date_dataset(
                date_range=date_range_df.loc[date_range_df.pattern == key]['sample'].to_list(),
                target_format=date_range_df.loc[date_range_df.pattern == key]['pattern'].to_list(),
                date_text_gen_methods=self.date_text_gen_methods[key],
                samples_per_method=value) for key,value in self.occurences_per_sample_dict.items()]

        return pd.concat(returnable_dataset_list,ignore_index=True)

    def _generate_single_date_dataset(self,date_range,target_format,
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

        for sample in date_range:
            
            # Sampling method and its ids
            for method_id,date_text_gen_method in self.sample_from_dict(date_text_gen_methods,
                samples_per_method):

                day,month,year = self.parse_days_months_years(sample,target_format[0])
                
                method_ids.append(
                    int(method_id)
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

                y.append(sample)

        dataset = pd.DataFrame(list(zip(method_ids,noise_types,X,y,samples_per_method*target_format)),
            columns=['Input Pattern','Noise Type','Input','Target','Target Format'])

        return dataset

    def generate_demo(self,date='01/01/2020',date_type='DD/MM/YYYY'):
        '''
            Generates a demo for all the text forms
            contained in the model for a given date.
        '''        
        methods = []
        generated_texts = []

        day,month, year = self.parse_days_months_years(date,date_type)

        for method_id,date_text_gen_method in self.date_text_gen_methods[date_type].items():
        
            methods.append(method_id)
            generated_texts.append(date_text_gen_method(day,month,year))


        dataset = pd.DataFrame(list(zip(methods,generated_texts,[date]*len(self.date_text_gen_methods[date_type]))),
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
    def parse_days_months_years(sample,sample_format):
        if sample_format == 'DD/MM/YYYY':
            day,month,year = sample.split('/')
        elif sample_format == 'DD/MM':
            day,month = sample.split('/')
            year = None
        elif sample_format == 'MM/YYYY':
            day = None
            month,year =sample.split('/')
        else:
            raise NotImplementedError(f'\
                Format {sample_format} not implemented :(')

        return day,month,year 

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

    def generate_date_range(self,start_date,end_date):
        '''
            This method generates all the available date ranges for a given
            start_date and end_date period.
        '''

        dates = []

        dates = self.generate_absolute_date_range(start_date,end_date)
        dates = dates + self.generate_incomplete_date_range(start_date,end_date)

        return dates

    @staticmethod
    def generate_absolute_date_range (start_date,end_date,step=1):
        '''
           Implements a list of all absolute dates in the period between
           start_date e end_date.
        '''

        dates = list(pd.date_range(start=start_date, end=end_date, freq='D').strftime(date_format = "%d/%m/%Y"))

        return combinations(dates,['DD/MM/YYYY'])

    @staticmethod
    def generate_incomplete_date_range(start_date,end_date,step=1):
        '''
            Generates the list of all possible incomplete dates in
            the period specified by start_date and end_date.
        '''

        # generating MM/YYYY formats in the interval
        months_years_in_period = list(pd.date_range(start=start_date, end=end_date, freq='M').strftime(date_format = "%m/%Y"))
        
        dates_MM_YYYY = combinations(months_years_in_period,['MM/YYYY'])

        # generating DD/MM formats in the interval
        days_months_in_period = list(pd.date_range(start=start_date, end=end_date, freq='D').strftime(date_format = "%d/%m"))[:366]

        dates_DD_MM = combinations(days_months_in_period,['DD/MM'])

        return dates_MM_YYYY + dates_DD_MM
