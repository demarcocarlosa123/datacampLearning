import pandas as pd
import numpy as np
import matplotlib
df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])

df.boxplot()