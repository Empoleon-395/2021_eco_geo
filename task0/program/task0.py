import os
import matplotlib.pyplot as plt
import japanize_matplotlib
import pandas as pd

df=pd.read_csv("../data/longterm_pop.csv")

fig=plt.figure(figsize=(6,3),dpi=300)
fig.suptitle("2000年から2015年までの日本の人口推移")
ax=fig.add_subplot(111)
ax.plot(df["pop"])
label=list(" ")
label.extend(df["year"][list(range(0,len(df["year"]),2))])
ax.set_xticklabels(label)
fig.show()
fig.savefig("../data/pop_plot.png")
