# Generates a random resistor with between 3 and 6 color bands of random colors, valid to the resistor code,
# It retrieves images of this type of resistor via the Bing api and puts them in an apropriately labled folder
# within /dataset 

# Hyperparameters
threeBandWeight = .3
fourBandWeight = .4
fiveBandWeight = .2
sixBandWeight = .1

def generate_and_get_resistor():
    # Generate 1st significant digit
    # Generate 2nd significant digit
    # Generate 3rd significant digit