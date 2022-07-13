import os # to get the path to the dataset folder and apropriate subfolder
import requests # to get image from the web
import shutil # to save it locally

def get_image_from_link (imagelink, outputname):
    # get the path to the dataset folder
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dataset_path = dir_path.rsplit('/',1)[0] + "/dataset/" + outputname
    filename = imagelink.split("/")[-1]

    # check if the output path folder exists, and if not create it
    if not os.path.exists(dataset_path):
        os.makedirs(dataset_path)
    print (dataset_path)

    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(imagelink, stream = True)

    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True
        
        # Open a local file with wb ( write binary ) permission.
        with open(filename,outputname) as f:
            shutil.copyfileobj(r.raw, f)
            
        print('Image sucessfully Downloaded: ',filename)
    else:
        print('Image Couldn\'t be retreived')
        

