###パッケージのインストール
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
import statsmodels.api as sm

###データ成型
df=pd.read_csv("../data/2015_pop.csv")
df=df[df["city_name"].apply(lambda x : x.strip()[-1]=="市")]
df=df.sort_values(by="2015_pop",ascending=False).reset_index(drop=True)
df["rank_log"]=np.log(df.index.values+1)
df["pop_log"]=np.log(df["2015_pop"])

###図示
fig=plt.figure(dpi=300)
ax=fig.add_subplot(111)
fig.suptitle("ランクサイズルールの図示")
ax.scatter(x=df["pop_log"],y=df["rank_log"])
ax.set_xlabel("人口(対数)")
ax.set_ylabel("順位(対数)")
ax.set_xlim(11,15)
x=np.linspace(11,15,10)
y=-x+16
ax.plot(x,y,color="black")
fig.show()
fig.savefig("../data/rank_size.png")

###線形関係の検証
##相関係数の計算
corcoef=np.corrcoef(x=df["pop_log"],y=df["rank_log"])[0,1]
print(corcoef)
##2次の項を説明変数に含めた際の回帰結果
X=pd.DataFrame({"pop_log^1":df["pop_log"],
                "pop_log^2":np.square(df["pop_log"])})
Y=df["rank_log"]
model = sm.OLS(Y, sm.add_constant(X))
results = model.fit()
print(results.summary())


