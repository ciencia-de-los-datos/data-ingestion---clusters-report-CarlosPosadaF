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
# print(df)
# df.drop([0, 1], axis=0, inplace=True)
dfSalida = pd.DataFrame()

lista = str(df.iloc[0]).split('  ')
listaTitulos = []

for string in lista:
    if string != "" and string != " ":
        listaTitulos.append(string.lower())



listaTitulos[1] = str(listaTitulos[1]).strip() + " " + str(listaTitulos[4])
listaTitulos[2] = str(listaTitulos[2]).strip() + " " + str(listaTitulos[5]).replace("\nName: 0, dtype: object", "")
listaTitulos.pop(4)
listaTitulos.pop(4)


# print(listaTitulos)
datos = ['',' ','Cluster','Cantidad de','Porcentaje de','Principales palabras clave']

# print(len("Cluster  Cantidad de     Porcentaje de   Principales palabras clave    "))
# print(str(df.iloc[2]).index('1'))
# df.drop([0, 0], axis=0, inplace=True)
# print(df)

# dfSalida.columns = [listaTitulos[0], listaTitulos[1], listaTitulos[2], listaTitulos[3]]

dfSalida['Col1'] = None
dfSalida['Col2'] = None
dfSalida['Col3'] = None
dfSalida['Col4'] = None
# dfSalida.columns = [listaTitulos[0], listaTitulos[1], listaTitulos[2], listaTitulos[3]]
print(listaTitulos)
print(dfSalida.columns)

for i in range(len(df)):
    # print("-", str(df.iloc[i])[71:72])
    # print(str(df.iloc[i]) )
    if i == 0 or i == 1:
        continue
    
    listaRegistros = ["", "", "", ""]
    if(str(df.iloc[i])[71:72].isnumeric()):
        # print(str(df.iloc[i]) )
        # print(str(df.iloc[i])[71:72], " - Numero", )

        # df.drop(1, inplace=True)
        # df.drop(0, inplace=True)
        lista = str(df.iloc[i]).split('  ')
        
        
        
        for string in lista:
            # if string != "" and string != " " and (len(list(filter(lambda x: string in x, datos))) == 0):
            # if string != "" and string != " " and string != 'Cluster' and string != 'Cantidad de' and string != 'Porcentaje de' and string != 'Principales palabras clave':
            #     listaRegistros.append(string.strip())
            # print(string)
            try:                
                index = datos.index(string.strip())
                    
            except:
                listaRegistros.append(string.strip())
            
            
        
        for n in range(4):
            listaRegistros.pop(0)

        # listaRegistros[3] = str(listaRegistros[3]).replace("\nName: 2, dtype: object", "")
        if len(listaRegistros) == 5:
            listaRegistros[3] = str(listaRegistros[3]) + ' ' + str(listaRegistros[4])
            listaRegistros.pop(4)

        listaRegistros[3] = listaRegistros[3].replace("  ", " ")
        listaRegistros[3] = listaRegistros[3].replace(" ", ", ")
        listaRegistros[3] = listaRegistros[3].replace(",,", ",")
        print(listaRegistros)
        # dfSalida = pd.DataFrame(listaRegistros)
        

    else:
        linea = str(df.iloc[i])
        lista = str(df.iloc[i]).split('  ')
        # print(lista)
        for n in range(6):
            lista.pop(0)

        linea = ""
        for ele in lista:
            linea += ele.strip() + " "

        # print(linea)
        listaRegistros[3] = str(listaRegistros[3]).strip() + " " + linea
        listaRegistros[3] = listaRegistros[3].replace("  ", " ")
        listaRegistros[3] = listaRegistros[3].replace(" ", ", ")
        listaRegistros[3] = listaRegistros[3].replace(",,", ",")
        # print(listaRegistros)
        # dfSalida = pd.DataFrame(listaRegistros)

    dfSalida = dfSalida.append(pd.DataFrame([listaRegistros], columns=["Col1","Col2","Col3","Col4"]), ignore_index=True)
    
# dfSalida.columns = [listaTitulos[0], listaTitulos[1], listaTitulos[2], listaTitulos[3]]
dfSalida.columns = listaTitulos
print(dfSalida)



