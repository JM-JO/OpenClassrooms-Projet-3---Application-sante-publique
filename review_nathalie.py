from pathlib import Path
import numpy as np
import pandas as pd

product_pickle = Path('data/products.pickle')
df = pd.read_pickle(product_pickle)

ser_x = df['energy-kj_100g']
ser_y = df['fat_100g']
min_x = 10
max_x = 100
min_y = 10
max_y = 100


# Option 1
#######################################
def f_bool(x, min, max):
    if np.isnan(x):
        return False
    elif x < min:
        return False
    elif x > max:
        return False
    else:
        return True


ser_x_bool = ser_x.apply(lambda x: f_bool(x, min_x, max_x))  # vaut True pour les valeurs non aberrantes
ser_y_bool = ser_y.apply(lambda y: f_bool(y, min_y, max_y))
ser_xy_bool = ser_x_bool.multiply(
    ser_y_bool)  # vaut True pour les valeurs non aberrantes de ser_x et de ser_y, sinon vaut False
# ser_x et ser_y sont les séries tracées
ser_x = ser_x[ser_xy_bool]
ser_y = ser_y[ser_xy_bool]
total_count = ser_xy_bool.sum()
print('Total count 1:', total_count)

# Option 2
#######################################
ser_x = ser_x.clip(lower=min_x, upper=max_x)
ser_y = ser_y.clip(lower=min_y, upper=max_y)
idx_not_missing = ser_x.notna() & ser_y.notna()
ser_x = ser_x[idx_not_missing]
ser_y = ser_y[idx_not_missing]
print('Total count 2:', sum(idx_not_missing))
