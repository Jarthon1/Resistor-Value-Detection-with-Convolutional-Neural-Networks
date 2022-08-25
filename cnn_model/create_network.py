print('-1\n')
from cnn import run_model

print('0\n')
model = run_model()
print('1\n')
model.summary()
print('2\n')
model.save("model")
print('3\n')
