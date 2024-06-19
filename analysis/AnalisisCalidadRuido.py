import pandas as pd

from generators.generadorDecibelios import generarDatosRuido

def construirDataRuido():
    #Creando Un dataFrame
    datosRuido=generarDatosRuido()
    dataFrameRuido=pd.DataFrame(datosRuido,columns=['id','nivel Ruido','comuna'])
    dataFrameRuido.to_csv('datosRuido.csv',index=False)
    print(dataFrameRuido)

construirDataRuido()