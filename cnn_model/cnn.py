import keras as keras
import scipy

from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import (
    Dense,
    Conv2D,
    MaxPool2D,
    Flatten,
    Dropout,
    BatchNormalization,
)

directory = "/Users/golden/Desktop/Projects/CNN_Resistors/dataset/hb74ynkjcn-1"

# def load_dataset(train_or_validate):
#     # Load image data
#     dataset = keras.utils.image_dataset_from_directory(
#         directory,
#         labels="inferred",
#         label_mode="categorical",
#         class_names=None,
#         color_mode="rgb",
#         batch_size=32,
#         image_size=(28, 28),
#         shuffle=True,
#         seed=42,
#         validation_split=.1,
#         subset=train_or_validate,
#         interpolation="bilinear",
#         follow_links=False,
#         crop_to_aspect_ratio=False
#     )
#     return dataset

def run_model():
    
    datagen_train = ImageDataGenerator(
        rotation_range=10,  # randomly rotate images in the range (degrees, 0 to 180)
        zoom_range=0.1,  # Randomly zoom image
        width_shift_range=0.1,  # randomly shift images horizontally (fraction of total width)
        height_shift_range=0.1,  # randomly shift images vertically (fraction of total height)
        horizontal_flip=True,  # randomly flip images horizontally
        vertical_flip=False, # Don't randomly flip images vertically)
    )
    datagen_valid = ImageDataGenerator(samplewise_center=True)

    training = datagen_train.flow_from_directory(
        "/Users/golden/Desktop/Projects/CNN_Resistors/dataset/train",
        target_size=(28,28),
        color_mode="rgb",
        class_mode="categorical",
    )
    # load and iterate validation dataset
    validation = datagen_valid.flow_from_directory(
        "/Users/golden/Desktop/Projects/CNN_Resistors/dataset/valid",
        target_size=(28,28),
        color_mode="rgb",
        class_mode="categorical",
    )

    # Assign labels and create vectors
    (x_train, y_train) = training
    (x_valid, y_valid) = validation

    num_classes = 11
    # Normalize our image data 
    # TODO: check if this is necessary once dataset is here
    x_train = x_train / 255
    x_valid = x_valid / 255

    # Create the model
    model = Sequential()
    model.add(Conv2D(75, (3, 3), strides=1, padding="same", activation="relu", 
                    input_shape=(28, 28, 3)))
    model.add(BatchNormalization())
    model.add(MaxPool2D((2, 2), strides=2, padding="same"))
    model.add(Conv2D(50, (3, 3), strides=1, padding="same", activation="relu"))
    model.add(Dropout(0.2))
    model.add(BatchNormalization())
    model.add(MaxPool2D((2, 2), strides=2, padding="same"))
    model.add(Conv2D(25, (3, 3), strides=1, padding="same", activation="relu"))
    model.add(BatchNormalization())
    model.add(MaxPool2D((2, 2), strides=2, padding="same"))
    model.add(Flatten())
    model.add(Dense(units=512, activation="relu"))
    model.add(Dropout(0.3))
    model.add(Dense(units=num_classes, activation="softmax"))

    model.compile(loss="categorical_crossentropy", metrics=["accuracy"])


    # Run the Model 
    model.fit(x_train, y_train, epochs=20, verbose=1, validation_data=(x_valid, y_valid))
    # model.fit(training.x, training.y, epochs=20, verbose=1, validation_data=validation)

    return model