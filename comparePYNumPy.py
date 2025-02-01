import numpy as np
import time

# Using Python loop
size = 10**6
python_list = range(size)

start = time.time()
result = [x * 2 for x in python_list]
end = time.time()
print(f"Python Loop Time: {end - start:.4f} seconds")

# Using NumPy
numpy_array = np.arange(size)

start = time.time()
result = numpy_array * 2
end = time.time()
print(f"NumPy Time: {end - start:.4f} seconds")
