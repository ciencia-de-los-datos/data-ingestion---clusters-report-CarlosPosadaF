"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


df = pd.read_fwf("clusters_report.txt", colspecs=[(3,5),(9,14),(25,29),(40,119)], header=None)
df.drop(df.index[:3], inplace=True)
df.reset_index(drop=True, inplace=True)
dfSalida = pd.DataFrame()
dfSalida['cluster'] = df[0]
dfSalida['cantidad_de_palabras_clave'] = df[1]
dfSalida['porcentaje_de_palabras_clave'] = df[2].str.replace(',', '.')
dfSalida.dropna(inplace=True)
dfSalida.reset_index(drop=True,inplace=True)
dfSalida['cluster'] = dfSalida['cluster'].str.strip().astype(int)
dfSalida['cantidad_de_palabras_clave'] = dfSalida['cantidad_de_palabras_clave'].str.strip().astype(int)
dfSalida['porcentaje_de_palabras_clave'] = dfSalida['porcentaje_de_palabras_clave'].str.strip().astype(float)
l = []
[l.append(i) for i in df[3]]
pal_clave = ' '.join(l).replace('control multi', 'control.multi')
l2 = []
[l2.append(i.strip()) for i in pal_clave[:-1].split('.')]
dfSalida['principales_palabras_clave'] = pd.concat([pd.Series(i) for i in l2]).reset_index(drop=True)
dfSalida['principales_palabras_clave'] = dfSalida['principales_palabras_clave'].str.replace(' ,', ',').replace(',',', ').str.replace('   ',' ').str.replace('  ',' ').str.strip('\n').str.replace('  ', ' ')

print(dfSalida)