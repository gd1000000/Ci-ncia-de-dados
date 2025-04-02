import matplotlib.pyplot as plt

#importa a biblioteca pandas
import pandas as pd

def exibirGrafico():7
#criar o dataframe
df =pd.DataFrame({
    "Meses": ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
    "temperaturas": [29, 31, 30, 28, 27, 25, 21, 24, 27, 28, 29, 33] 
})

#Redimensionando o gráfico
plt.figure(figsize=[10.0, 5.0])

#Criação do gráfico
plt.plot(df['Meses'],df['Temperatura'], color="blue")

#Definição dos títulos
plt.title("temperatura média ao longo do tempo")
plt.xlabel("Meses")
plt.ylabel("Temperatura")

#Exibindo o gráfico
plt.show()
plt.savefig('chart2.png')

#Exibe no console dados estatísticos 
print(f'temperaturas: \n{df['Temperaturas'].describe()}')
