'''
    Implements the language dicts for each language.
    If you want to contribute with new language formats, it is important
    to follow the patterns below
'''
from collections import OrderedDict

'''
    EN dicts
'''
from .en_dicts.en_absolute_date_text_formats import absolute_date_formats_dict \
    as en_absolute_date_formats_dict
from .en_dicts.en_dd_mm_text_formats import dd_mm_date_formats_dict \
    as en_dd_mm_date_formats_dict
from .en_dicts.en_mm_yyyy_text_formats import mm_yyyy_date_formats_dict \
    as en_mm_yyyy_date_formats_dict

'''
    PT-BR dicts
'''
from .pt_dicts.pt_absolute_date_text_formats import absolute_date_formats_dict \
    as pt_absolute_date_formats_dict
from .pt_dicts.pt_incomplete_dd_mm_text_formats import dd_mm_date_formats_dict \
    as pt_dd_mm_date_formats_dict
from .pt_dicts.pt_incomplete_mm_yyyy_text_formats import mm_yyyy_date_formats_dict \
    as pt_mm_yyyy_date_formats_dict    

'''
    Absolute dates dicts
'''
absolute_date_formats_dict_collection = OrderedDict([
    ('en',en_absolute_date_formats_dict),
    ('pt',pt_absolute_date_formats_dict)
])


'''
    Incomplete MM/YYYY dates dicts
'''
incomplete_mm_yyyy_date_formats_dict_collection = OrderedDict([
    ('en',en_mm_yyyy_date_formats_dict),
    ('pt',pt_mm_yyyy_date_formats_dict)
])


'''
    Incomplete DD/MM dates dicts
'''
incomplete_dd_mm_date_formats_dict_collection = OrderedDict([
    ('en',en_dd_mm_date_formats_dict),
    ('pt',pt_dd_mm_date_formats_dict)
])