class Invalidinterest(Exception):
    pass

class Invalidmonths(Exception):
    pass


def calcular_ahorro_programado(monto: float, interes: float, periodo: int):

    if interes < 0.1 or interes > 1:
       raise Invalidinterest( "ERROR: La tasa de interes es invalida" )
    
    if periodo < 1:
       raise Invalidmonths( "ERROR: El periodo es invalido" )

    return monto*(1+interes)*periodo-1/interes