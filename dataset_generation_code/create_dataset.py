from query_bing_search_api import image_retriever
from random_resistor_generator import *
from colors_to_ohms import *
from random_resistor_generator import *

uniqueStrings = 50

strings = get_strings(uniqueStrings)

for string in strings:
    ohms = colors_to_ohms(string)
    foldername = get_label(string)

    image_retriever(ohms,foldername)
