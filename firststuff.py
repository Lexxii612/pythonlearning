# Comments are here
# import libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(data)
print(data[0])

squared_data = data ** 2

print(squared_data)

#for t in data:
#    print(t*t)


average_squared = np.mean(squared_data)

print(average_squared)

df = pd.DataFrame(squared_data, columns=['Squared Data'])

print(df)
# df.plot(kind='bar', color='purple', legend=None)
# plt.title('hello world')
# plt.xlabel('Index')
# plt.ylabel('squares')
# plt.xticks(range(len(squared_data)))
# plt.show()

x = 42
print(x)

print(type(x))