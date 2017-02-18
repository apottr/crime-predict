import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier as GBC


inputs = pd.DataFrame({
    'A': [0,1,0,1],
    'B': [0,1,1,0],
    'Targets': [0,1,0,0]
})

net = GBC(n_estimators=200,max_depth=3)

net.fit(inputs[['A','B']],inputs['Targets'])

print net.predict([[1,1]])


