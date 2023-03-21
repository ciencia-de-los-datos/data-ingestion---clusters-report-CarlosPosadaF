"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd

df = pd.read_fwf("clusters_report.txt", sep = "\t")

dfSalida = pd.DataFrame()

lista = str(df.iloc[0]).split('  ')
listaTitulos = []

for string in lista:
    if string != "" and string != " ":
        listaTitulos.append(string.lower().strip())



listaTitulos[1] = str(listaTitulos[1]).strip() + " " + str(listaTitulos[4])
listaTitulos[2] = str(listaTitulos[2]).strip() + " " + str(listaTitulos[5])
listaTitulos.pop(4)
listaTitulos.pop(4)

datos = ['',' ','Cluster','Cantidad de','Porcentaje de','Principales palabras clave']

dfSalida['Col1'] = None
dfSalida['Col2'] = None
dfSalida['Col3'] = None
dfSalida['Col4'] = None
dfSalida.columns = [listaTitulos[0], listaTitulos[1], listaTitulos[2], listaTitulos[3]]

for i in range(len(df)):
    if i == 0 or i == 1:
        continue
    
    listaRegistros = ["", "", "", ""]
    if(str(df.iloc[i])[71:72].isnumeric()):
        lista = str(df.iloc[i]).split('  ')
        
        for string in lista:
            try:                
                index = datos.index(string.strip())                    
            except:
                listaRegistros.append(string.strip())
        
        for n in range(4):
            listaRegistros.pop(0)

        if len(listaRegistros) == 5:
            listaRegistros[3] = str(listaRegistros[3]) + ' ' + str(listaRegistros[4])
            listaRegistros.pop(4)

        listaRegistros[3] = listaRegistros[3].replace("  ", " ")
        listaRegistros[3] = listaRegistros[3].replace(" ", ", ")
        listaRegistros[3] = listaRegistros[3].replace(",,", ",")
        print(listaRegistros)
        
    else:
        linea = str(df.iloc[i])
        lista = str(df.iloc[i]).split('  ')

        for n in range(6):
            lista.pop(0)

        linea = ""
        for ele in lista:
            linea += ele.strip() + " "

        listaRegistros[3] = str(listaRegistros[3]).strip() + " " + linea
        listaRegistros[3] = listaRegistros[3].replace("  ", " ")
        listaRegistros[3] = listaRegistros[3].replace(" ", ", ")
        listaRegistros[3] = listaRegistros[3].replace(",,", ",")
        print(listaRegistros)
    

print(dfSalida)



