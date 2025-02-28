# CleanCode
Tests.py

Nuestro proyecto consta de 12 pruebas unitarias

Integrantes:
Tomás Mercado
Juan Esteban Marín

Definicion de variables
-Monto = Es la cantidad de dinero que se deposita en la cuenta de ahorro al principio

-Tasa de interés = Es el porcentaje que se aplicará al saldo inicial para calcular los intereses

Periodo: Es el número de meses en los que se realizará el cálculo de los intereses

Caso 1
	Entradas
	monto = 300000
        interes = 0.035
        periodo = 24

	Salida
		 7451971.429

Caso 2
	Entradas
	monto = 500000
        interes = 0.06
        periodo = 36
	
	Salida
		19079983.33


Caso 3
	Entradas
	monto = 1000000
        interes = 0.1
        periodo = 60
	
	Salida
		65999990

Caso 4
	Entradas
	monto = 250000
        interes = 0.05
        periodo = 1
	
	Salida
		262480
Caso 5
	Entrada
	monto = 200000
        interes = 0.045
        periodo = 12

	Salida
		2507977.778

CASOS EXTRAORDINARIOS
		
Caso 6
	Entradas
	monto = 1000000
        interes = 0.02
        periodo = 1

	
	Salidas
		1019950

Caso 7
	Entradas
	monto = 200000
        interes = 0.05
        periodo = 600

	
	Salidas
		125999980

Caso 8
	Entradas
	monto = 500000
        interes = 1
        periodo = 12

	
	Salidas
		11999999


CASOS ERRONEOS

Caso 9
	Entradas
	monto = 300000
        interes = -0.05
        periodo = 12

	
	Salidas
		Error: tasa invalida


Caso 10
	Entradas
	monto = 500000
        interes = 0.06
        periodo = -12

	
	Salidas
		Error: meses invalidos


Caso 11
	Entradas
	monto = 600000
        interes = 0
        periodo = 24

	
	Salidas
		Error: 	Tasa de interes del 0%


Caso 12
	Entradas
	monto = 300000
        interes = 1,5
        periodo = 12

	
	Salidas
	Error: tasa de interes mayor al 100%