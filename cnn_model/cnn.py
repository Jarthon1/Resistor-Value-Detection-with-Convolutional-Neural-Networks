import keras as keras

from keras.models import Sequential
from keras.layers import (
    Dense,
    Conv2D,
    MaxPool2D,
    Flatten,
    Dropout,
    BatchNormalization,
)

directory = "/../dataset/"

def load_dataset(subset):
    # Load image data
    dataset = keras.utils.image_dataset_from_directory(
        directory,
        labels="inferred",
        label_mode="catagorical",
        class_names=None,
        color_mode="rgb",
        batch_size=32,
        image_size=(28, 28),
        shuffle=True,
        seed=None,
        validation_split=.1,
        subset=subset,
        interpolation="bilinear",
        follow_links=False,
        crop_to_aspect_ratio=False
    )
    return dataset

def run_model():
    
    training = load_dataset("training")
    validation = load_dataset("validation")

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

    model.summary()

    model.fit(training.image, y_train, epochs=20, verbose=1, validation_data=(x_valid, y_valid))

    return model