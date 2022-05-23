from random import randint
import simpy
from simpy.core import Environment
from carwash import AutoLavado
from project_constants import Constants

def car(env: Environment, nombre:str, atl: AutoLavado):
    print('%s llego al auto lavado a la hora %.2f.' % (nombre, env.now))
    with atl.estaciones.request() as request:
        yield request
        print('%s entro al auto lavado a las %.2f.' % (nombre, env.now))
        yield env.process(atl.lavar(nombre))
        print('%s sale del autolavado a las %.2f.' % (nombre, env.now))

def generar_vehiculo()-> tuple:
    llaves_diccionario = ["Coche", "Camioneta", "Moto"]
    idx_llave_diccionario = randint(0,2)
    llave = llaves_diccionario[idx_llave_diccionario]
    tiempo_vehiculo = Constants().get_vehicle_type()[llave] 

    idx_tipo_lavado = randint(0,3)
    if(idx_tipo_lavado == 0):
        return tiempo_vehiculo, llave
    elif(idx_tipo_lavado == 1):
        return (tiempo_vehiculo+5), llave
    else:
        return (tiempo_vehiculo*2), llave

def set_tiempo_entre_coches(dia: str)->int:
    for idx, value in enumerate(Constants().get_days()):
        if(dia == value): #Found the selected day
            if idx > 2:
                return Constants().get_timeout()[1] 
    return Constants().get_timeout()[0] 

def configuracion(env: Environment, numero_estaciones: int, dia: str):
    autolavado = AutoLavado(env, numero_estaciones)
    i=0
    while(i < 4):
        tiempo_lavado, llave = generar_vehiculo()
        autolavado.set_tiempo(tiempo_lavado)
        current_vehicle = f"{llave} {i}" 
        env.process(car(env, current_vehicle, autolavado))
        i+=1
    intervalo_tiempo = set_tiempo_entre_coches(dia)
    while True:
        yield env.timeout(randint(intervalo_tiempo-2, intervalo_tiempo+2))
        i+=1
        env.process(car(env, f"{llave} {i}", autolavado))
