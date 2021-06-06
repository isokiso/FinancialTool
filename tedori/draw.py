import matplotlib.pyplot as plt
import pandas as pd
from cal import Cal

def make_data():
    m_incomes = range(0, 1500000, 1000)
    tedori = {}

    for i, m_income in enumerate(m_incomes):
        c = Cal(m_income,26,"東京都",0,0,0).OutTedori()
        tedori[i] = c
    df = pd.DataFrame(tedori)
    print(df)
    return df.T

def make_fig(df):
    labels = ["Tedori", "Kenho", "Kaiho", "Nenkin", "Koyo","Syotoku", "Jumin"]
    fig, ax = plt.subplots()
    x = df["Gakumen"]/10000
    ax.plot(x, df["Gakumen"])
    ax.set_xlabel("Gakumen/Month (10^4)")
    ax.set_ylabel("yen/Month")
    ax.stackplot(x, df[labels[0]], df[labels[1]], df[labels[2]], df[labels[3]],df[labels[4]],df[labels[5]],df[labels[6]], labels=labels)
    ax.legend(loc="upper left")
    plt.savefig('fig.pdf')



if __name__=="__main__":
    data = make_data()
    make_fig(data)
