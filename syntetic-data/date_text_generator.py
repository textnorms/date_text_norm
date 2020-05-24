from num2words import num2words
from datetime import datetime
from datetime import timedelta
import pandas as pd
from date_text_formats import date_formats_dict

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
        text_gen_methods=date_formats_dict):

        self.start_date = datetime.strptime(start_date, "%d/%m/%Y")
        self.end_date = datetime.strptime(end_date, "%d/%m/%Y")

        self.date_range = self.generate_date_range(self.start_date,self.end_date)

        self.text_gen_methods = text_gen_methods

    def generate_date_dataset(self):

        X = []
        ids = []

        for method_id,date_text_gen_method in self.text_gen_methods.items():

            for sample in self.date_range:
                day,month,year = sample.split('/')
                
                ids.append(
                    method_id
                )

                X.append(
                    date_text_gen_method(day,month,year)
                )

        target_reptitions = len(self.text_gen_methods.keys())
        dataset = pd.DataFrame(list(zip(ids,X,target_reptitions*self.date_range)),
            columns=['Tipo padrão','Entrada','Canônico'])

        return dataset


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

a = DateTextGenerator(start_date='01/01/1900',end_date='31/12/2020')

print(a.generate_date_dataset())