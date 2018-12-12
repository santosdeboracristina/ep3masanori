PESQUISA DE CRIMES DE ÓDIO NOS EUA DE 2014 A 2016¶
#ALUNA: DÉBORA CRISTINA SANTOS

#TURMA: B - TERCEIRO PERIODO

#FONTE DOS DADOS: https://crime-data-explorer.fr.cloud.gov/downloads-and-docs

#DATA BASE: FBI HATE CRIME

#ANO: 2014, 2015 E 2016

#*----------------------------------------------------------------------*#
#importando os dados
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline
low_memory = False

pd.options.display.max_columns = 80


#lendo o arquivo xlxs
df= pd.read_excel('FBICRIMES.xlsx', sheet_name='FBI_CRIMES')
df.info()
df
print (df.head())

#agrupando os dados por tipo de preconceito
groupby_TIPO_DE_PRECONCEITO = df.groupby('TIPO_DE_PRECONCEITO')
groupby_TIPO_DE_PRECONCEITO.groups

#Quantidade de crimes por ano x tipos de preconceito
qtdcrimes = df.groupby(['ANO','TIPO_DE_PRECONCEITO']).TIPO_DE_PRECONCEITO.count().reset_index(name="count")
print(qtdcrimes.sort_values(by='count', ascending=True))

#O pico de crimes de odio foi na California, em 2016, com 459 ocorrencias
ocor = df.groupby(['ANO','ESTADO']).ESTADO.count().sort_values().reset_index(name="QTD")

est = ocor.drop_duplicates('ESTADO')
est.ANO
lista_temp=[]
for w in est.index:
    lista_por_cidade = ocor[(ocor.ESTADO == est.ESTADO[w])]
    lista_temp.append(lista_por_cidade.loc[lista_por_cidade['QTD'].idxmax()])

lt = pd.DataFrame(lista_temp)
lt = lt.sort_values(by='QTD', ascending=False)
lt

#constando que os crimes de odio contra negros e afro americanos teve seu pico em 2016 com 1768 ocorrencias
qtdcrimes = df.groupby(['ANO','TIPO_DE_PRECONCEITO']).TIPO_DE_PRECONCEITO.count().reset_index(name="count")
qtdcrimes[qtdcrimes['count'] == qtdcrimes['count'].max()]

#Quantidade de Ocorrencias por estado
try2 = qtdcrimes.drop_duplicates('ESTADO')
try2 = try2.sort_values(by='ESTADO')
try2.ESTADO

#Quantidade de Ocorrencias por cidade
try3 = qtdcrimes.drop_duplicates('CIDADE')
try3 = try2.sort_values(by='CIDADE',ascending=True)
try3.CIDADE

#% TOP 3 CRIMES DE ODIO REPORTADOS NOS EUA DE 2014 A 2016
df1 = df.groupby(['ESTADO','TIPO_DE_PRECONCEITO','ANO']).TIPO_DE_PRECONCEITO.count().reset_index(name="QTD")
df1.TIPO_DE_PRECONCEITO.value_counts().plot(kind='pie', autopct='%.2f%%', figsize=(6, 6), legend='false' )
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.axis('equal')
plt.axis('off')
plt.legend(loc="right")
plt.show

#QUANTIDADE DE CRIMES CONTRA NEGROS E AFRO AMERICANOS DE 2014 - 2016
df1 = df.groupby(['ANO','TIPO_DE_PRECONCEITO']).TIPO_DE_PRECONCEITO.count().reset_index(name="count_peri")
est = df1.drop_duplicates('ANO')
est.ANO
lista_temp=[]
for w in est.index:
    lista_por_ano = df1[(df1.ANO == est.ANO[w])]
    lista_temp.append(lista_por_ano.loc[lista_por_ano['count_peri'].idxmax()])

lt = pd.DataFrame(lista_temp)
lt = lt.sort_values(by='count_peri', ascending=True)
lt

#TOP 3 CRIMES DE ODIO MAIS REPORTADOS NOS EUA DE 2014 A 2016
df.query('ANO == "2014"')['TIPO_DE_PRECONCEITO'].value_counts().plot(kind='barh',figsize=(25, 5))
plt.suptitle('PRECONCEITOS MAIS FORTES NOS EUA EM 2014', size=20)
plt.xlabel("Qtd de crimes devido ao Preconceito")
plt.ylabel("Tipos de Preconceitos que levou aos crimes")
plt.grid(True)
plt.show()

df.query('ANO == "2015"')['TIPO_DE_PRECONCEITO'].value_counts().plot(kind='barh',figsize=(25, 5))
plt.suptitle('PRECONCEITOS MAIS FORTES NOS EUA EM 2015', size=20)
plt.xlabel("Qtd de crimes devido ao Preconceito")
plt.ylabel("Tipos de Preconceitos que levou aos crimes")
plt.grid(True)
plt.show()

df.query('ANO == "2016"')['TIPO_DE_PRECONCEITO'].value_counts().plot(kind='barh',figsize=(25, 5))
plt.suptitle('PRECONCEITOS MAIS FORTES NOS EUA EM 2016', size=20)
plt.xlabel("Qtd de crimes devido ao Preconceito")
plt.ylabel("Tipos de Preconceitos que levou aos crimes")
plt.grid(True)
plt.show()

