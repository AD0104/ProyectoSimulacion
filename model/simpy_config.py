from random import randint
import simpy
from simpy.core import Environment
from model.carwash import AutoLavado
from model.project_constants import Constants

car_time_list = [0]
bike_time_list = [0]
truck_time_list = [0]
arrivals = []
entrys = []
outs = []

"""
    Function to control the cars and their timeouts, it gets called everytime
    a new car is generated.
"""
def car(env: Environment, nombre:str, atl: AutoLavado):
    arrivals.append(f"{nombre} llego al autolavado a las {env.now}")
    with atl.estaciones.request() as request:
        yield request
        with atl.trabajadores.request() as t_request:
            yield t_request
            
            entrys.append(f"{nombre} entro al autolavado a las {env.now}")
            
            yield env.process(atl.lavar())
            
            time = env.now
            if("Coche" in nombre):
                add_car_time(int(time))
            elif("Moto" in nombre):
                add_bike_time(int(time))
            else:
                add_truck_time(int(time))
            
            outs.append(f"{nombre} salio del autolavado a las {time}")

"""
    The following functions were created to get the messages thrown by the
    simulation, when a car arrives at the carwash, when it's getting washed
    and when it's finished.
"""
def get_arrival_messages()->list:
    return arrivals
def get_entry_messages()->list:
    return entrys
def get_out_messages()->list:
    return outs

"""
    Function to clean the lists, later append 0 to prevent
    ZeroDivisionError
"""
def set_time_lists()->None:
    car_time_list.clear()
    bike_time_list.clear()
    truck_time_list.clear()

    car_time_list.append(0)
    bike_time_list.append(0)
    truck_time_list.append(0)
    
"""
    The following methods are used to append a new time registered for the 
    different vehicles types.
"""
def add_car_time(car_time: int)-> None:
    car_time_list.append(car_time)
def add_bike_time(bike_time: int)-> None:
    bike_time_list.append(bike_time)
def add_truck_time(truck_time: int)-> None:
    truck_time_list.append(truck_time)

"""
    This method returns the total time for the different vehicle types,
    while also returning the average time.
"""
def get_times()->dict:
    dt = {
        "car-total-time": sum(car_time_list),
        "car-average-time": sum(car_time_list)/len(car_time_list),
        "bike-total-time": sum(bike_time_list),
        "bike-average-time": sum(bike_time_list)/len(bike_time_list),
        "truck-total-time": sum(truck_time_list),
        "truck-average-time": sum(truck_time_list)/len(truck_time_list)
    }
    return dt

"""
    Creating the dictionary keys to later get a random index of the keys,
    then we get the vehicle type and the default washing time, then generate
    the washing type and return that time.
"""
def generar_vehiculo()-> tuple:
    llaves_diccionario_vehiculos = ["Coche", "Camioneta", "Moto"]
    idx_llave_diccionario_vehiculos = randint(0,2)
    llave_vehiculos = llaves_diccionario_vehiculos[idx_llave_diccionario_vehiculos]
    tiempo_vehiculo = Constants().get_vehicle_type()[llave_vehiculos]

    llaves_diccionario_lavados = ["Lavado Normal", "Lavado y engrasado", "Lavado de vestiduras", "Lavado de motor"] 
    idx_llave_diccionario_lavados = randint(0,3)
    llave_lavados = llaves_diccionario_lavados[idx_llave_diccionario_lavados]
    tiempo_lavado = Constants().get_washing_type()[llave_lavados]
    
    return (tiempo_vehiculo+(tiempo_vehiculo*tiempo_lavado)), llave_vehiculos

"""
    We generate 4 inicial vehicles, then we keep generating and adding cars to the yield while the
    amount of cars generated are less than the max cars per day.
"""
def configuracion(env: Environment, numero_estaciones: int, dia: str, trabajadores: int):
    autolavado = AutoLavado(env, numero_estaciones, trabajadores)
    coches_generados, coches_maximos = 0, Constants().get_max_cars()[dia]
    llave=""
    i=0
    while(i < 4):
        tiempo_lavado, llave = generar_vehiculo()
        autolavado.set_tiempo(tiempo_lavado)
        current_vehicle = f"{llave} {i}" 
        env.process(car(env, current_vehicle, autolavado))
        i+=1
    while(coches_generados <= coches_maximos):
        yield env.timeout(randint(1, 5))
        tiempo_lavado, llave = generar_vehiculo()
        autolavado.set_tiempo(tiempo_lavado)
        current_vehicle = f"{llave} {i}"
        env.process(car(env, current_vehicle, autolavado))
        coches_generados+=1
        i+=1
