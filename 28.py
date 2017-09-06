import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#a = {'nos':[1,2,3], 'grades':[44,55,32], 'g':[9,7,6]}

#df =  pd.DataFrame(a)

#df.to_json('df.json')

df = pd.read_json('df.json')

df.to_html('fg.html')



print(df)

df.plot()
plt.show()