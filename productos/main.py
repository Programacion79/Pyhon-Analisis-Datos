import pandas as pd


def analisisProductos():
    # df = pd.read_csv("productos.csv", encoding="utf-8", sep=",")
    # df.columns = df.columns.str.lower().str.strip()
    # dfCerrado = df[df["estado"].str.strip().str.lower() == "cerrado"]

    # Simulamos que ya existe el DataFrame df
    df = pd.read_csv("productos.csv", encoding="utf-8", sep=",")
    df.columns = df.columns.str.lower().str.strip()


    totalventas = df['valor venta'].sum()
    print(f'El total de venta es: {totalventas}')

    ventaMayor = df['valor venta'].max()
    print(f'La mayor venta es: {ventaMayor}')

    ventaMenor = df['valor venta'].min()
    print(f'La menor venta es: {ventaMenor}')

    promVenta = df['valor venta'].mean()
    print(f'Promedio de venta es: {promVenta}')


if __name__ == '__main__':
    analisisProductos()
