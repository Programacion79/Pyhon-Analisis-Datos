import pandas as pd

def analisisProductos():
    df = pd.read_csv("productos.csv", encoding="utf-8", sep=",")
    print(df)




if __name__ == '__main__':
    analisisProductos()

