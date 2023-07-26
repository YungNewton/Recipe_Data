from CarFacts import Car

new_car = Car('black',4,'ferrari')

import pandas as pd
midterm_scores = [96,90,85]
df = pd.DataFrame(midterm_scores, columns=['midterm_scores'])

print(type(df))

shape = df.shape
print(shape)
df.sort_values(by='midterm_scores', ascending=False)
