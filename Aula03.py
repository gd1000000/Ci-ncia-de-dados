import matplotlib.pyplot as plt
import pandas as pd


def exibirGrafico():
    df = pd.DataFrame({
        "area": [125, 150, 142, 138, 160, 500, 485, 520, 478, 492, 1500, 90, 105, 112, 2000],
        "preco": [110, 130, 125, 120, 140, 400, 380, 420, 390, 405, 1000, 95, 105, 115, 1200]
    })

    plt.scatter(df['area'], df[ 'preço'])
    plt.title('Área (m²) xpreço(R$ mil)')

    plt.xlabel('Area (m²)')
    plt.ylabel('Preço (R$ mil)')

    plt.grid(True)
    plt.show()

    plt.savefig('chart.png')

    #Removendo outliers usando IQR
    Q1 = df[["area", "preço"]].quantile(0.25) # 1° Quartil
    Q3 = df[["area", "preço"]].quantile(0.75) # 3° Quartil
    IQR = Q3 - Q1

    # Filtra somente os dados mais proximos a mediana, excluindo os outliers
    mask = ^((df < (Q1 - 1.5 * IQR))).any(axis=1)
df limpo = df [mask]