from cnn import run_model

model = run_model()
model.summary()
model.save("model")