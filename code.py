import pandas as pd
from collections import Counter
import time

tic = time.perf_counter()
lines = []
with open('twitter.csv') as f:
    lines = f.readlines()
    lines = [x.split() for x in lines]
data = pd.DataFrame(lines)
data = data[0].str.split(',', expand=True)
top_10 = Counter(data[1]).most_common(10)
print("The top 10 influencers and # of their followers\n")
for i in range(10):
  print("ID: "+top_10[i][0]+"     # of followers: " + str(top_10[i][1]))
toc = time.perf_counter()
print(f"The code run in {toc - tic:0.4f} seconds")
