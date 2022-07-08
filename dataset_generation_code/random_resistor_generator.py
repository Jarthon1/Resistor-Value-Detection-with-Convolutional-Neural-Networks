# Generates a random resistor with between 3 and 6 color bands of random colors, valid to the resistor code,
# It retrieves images of this type of resistor via the Bing api and puts them in an apropriately labled folder
# within /dataset 

import itertools
import random

# Hyperparameters
threeBandWeight = .3
fourBandWeight = .4
fiveBandWeight = .2
sixBandWeight = .1

uniqueStrings = 50

def random_resistor_generator(uniqueStrings):
    colorsToOhmsList = get_strings(uniqueStrings)
    pass

# create a list of randomly generated strings that represent resistor bands
def get_strings(uniqueStrings):
    colorsNone = ["black","brown","red","orange","yellow","green","blue","violet","grey","white","gold","silver","none"]
    colors = ["black","brown","red","orange","yellow","green","blue","violet","grey","white","gold","silver"]

    res = []
    for i in range(uniqueStrings):
        s = ""
        bands = get_bands()
        for i in range(bands):
            if i != bands - 1:
                s += random.choice(colors) + " "
            else:
                s += random.choice(colorsNone)
        res.append(s)
        
    return res

# create random sample using the weights for the band we want
def get_bands():
    sample = random.uniform(0,1)
    if  sample <= threeBandWeight:
        bands = 3
    elif sample > threeBandWeight and sample <= threeBandWeight + fourBandWeight:
        bands = 4
    elif sample > threeBandWeight + fourBandWeight and sample <= threeBandWeight + fourBandWeight + fiveBandWeight:
        bands = 5
    elif sample > threeBandWeight + fourBandWeight + fiveBandWeight:
        bands = 6
    
    return bands
        
