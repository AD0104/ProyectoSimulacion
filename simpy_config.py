from random import randint
import simpy
from simpy.core import Environment
from carwash import AutoLavado
from project_constants import Constants

car_time_list = [0]
bike_time_list = [0]
truck_time_list = [0]
arrivals = []
entrys = []
outs = []

def car(env: Environment, nombre:str, atl: AutoLavado):
    arrivals.append(f"{nombre} llego al autolavado a las {env.now}")
    #print('%s llego al auto lavado a la hora %.2f.' % (nombre, env.now))
    with atl.estaciones.request() as request:
        yield request
        entrys.append(f"{nombre} entro al autolavado a las {env.now}")
        #print('%s entro al auto lavado a las %.2f.' % (nombre, env.now))
        yield env.process(atl.lavar(nombre))
        time = env.now
        if("Coche" in nombre):
            add_car_time(int(time))
        elif("Moto" in nombre):
            add_bike_time(int(time))
        else:
            add_truck_time(int(time))
        outs.append(f"{nombre} salio del autolavado a las {time}")
        #print(f"{nombre} salio del autolavado a las {time}")
def get_arrival_messages()->list:
    return arrivals
def get_entry_messages()->list:
    return entrys
def get_out_messages()->list:
    return outs
def set_time_lists(new_list: list)->None:
    car_time_list = new_list
    bike_time_list = new_list
    truck_time_list = new_list
def add_car_time(car_time: int)-> None:
    print("Its a car")
    car_time_list.append(car_time)
def add_bike_time(bike_time: int)-> None:
    print("Its a bike")
    bike_time_list.append(bike_time)
def add_truck_time(truck_time: int)-> None:
    print("Its a truck")
    truck_time_list.append(truck_time)
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
