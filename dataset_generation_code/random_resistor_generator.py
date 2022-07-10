# Generates a random resistor with 3 to 6 color bands of random colors, valid to the resistor code,
# It retrieves images of this type of resistor via the Bing api and puts them in an apropriately labled folder
# within /dataset 

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

# returns a six word string of colors joined by underscores representing 
# the label of the image
def get_label(colorString):
    lst = colorString.split()
    if len(lst) == 3:
        while len(lst) < 6:
            lst.append("none")
    elif len(lst) == 4:
        last = lst.pop()
        lst.append("none")
        lst.append(last)
        lst.append("none")
    elif len(lst) == 5:
        lst.append("none")
    return "_".join(lst)

# create a set of unique randomly generated strings that represent resistor bands
def get_strings(uniqueStrings):
    colorsNone = ["black","brown","red","orange","yellow","green","blue","violet","grey","white","gold","silver","none"]
    colors = ["black","brown","red","orange","yellow","green","blue","violet","grey","white","gold","silver"]

    res = set()
    while len(res) < uniqueStrings:
        s = ""
        bands = get_bands()
        for i in range(bands):
            if i != bands - 1:
                s += random.choice(colors) + " "
            else:
                s += random.choice(colorsNone)
        res.add(s)
        
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
        
