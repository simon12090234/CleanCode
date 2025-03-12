import sys 
sys.path.append("src")

from model import app

amount = float( input( "Ingrese la couta mensual a ahorrar: ") )
interest = float( input( "Ingrese el interés en su valor decimal: ") )
period= int( input( "Ingrese el número de cuotas que quiere ahorrar: ") ) 

try:
    payment = app.Calculate_programmed_savings( amount, interest, period )

    print( f"El valor de la cuota es: {payment}" )
except Exception as err :
    print(f"No se puedo calcular el monto a ahorrar { err } ")