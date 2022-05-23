from enum import auto
import random
import simpy

ESTACIONES_DE_LAVADO=3
NUMERO_DE_TRABAJADORES=2
TIEMPO_SIMULACION=60    #Tiempo en minutos 
#8HRS = 480min
DIAS=["Mar","Mier","Juev","Vier","Sab","Dom"]
TIEMPO_ENTRE_VEHICULO=[30,15]
COCHES_MAX_DIA=[15,30]
TIPO_LAVADO=[
    "Lavado Normal",
    "Lavado y engrasado",
    "Lavado de vestiduras",
    "Lavado de motor"
]
TIPOS_VEHICULOS={
    "Coche": 15,
    "Camioneta":30,
    "Moto": 7
}

class AutoLavado():
    def __init__(self, env, estaciones):
        self.env = env
        self.estaciones = simpy.Resource(env, estaciones)
        
    def set_tiempo(self, tiempo_lavado=int) -> None:
        self.tiempo_lavado = tiempo_lavado
    def set_trabajadores(self, trabajadores=int) -> None:
        self.trabajadores = trabajadores

    def lavar(self, nombre_coche):
        yield self.env.timeout(self.tiempo_lavado)
        print("Lavado removio %d%% de %s" %(random.randint(50, 99), nombre_coche))

def car(env, nombre, atl):
    print('%s llego al auto lavado a la hora %.2f.' % (nombre, env.now))
    with atl.estaciones.request() as request:
        yield request
        
        print('%s entro al auto lavado a las %.2f.' % (nombre, env.now))
        yield env.process(atl.lavar(nombre))
        print('%s sale del autolavado a las %.2f.' % (nombre, env.now))

def generar_vehiculo():
    llaves_diccionario = ["Coche", "Camioneta", "Moto"]
    idx_llave_diccionario = random.randint(0,2)
    llave = llaves_diccionario[idx_llave_diccionario]
    tiempo_vehiculo = TIPOS_VEHICULOS[llave]

    idx_tipo_lavado = random.randint(0,3)
    if(idx_tipo_lavado == 0):
        return tiempo_vehiculo, llave
    elif(idx_tipo_lavado == 1):
        return (tiempo_vehiculo+5), llave
    else:
        return (tiempo_vehiculo*2), llave

def set_tiempo_entre_coches():
    idx_dia = random.randint(0, 5)
    if(idx_dia < 2):
        return TIEMPO_ENTRE_VEHICULO[0]
    return TIEMPO_ENTRE_VEHICULO[1]

def configuracion(env, numero_estaciones):
    autolavado = AutoLavado(env, numero_estaciones)
    for i in range(4):
        tiempo_lavado, llave = generar_vehiculo()
        autolavado.set_tiempo(tiempo_lavado=tiempo_lavado)
        env.process(car(env, llave+" "+str(i), autolavado))
    intervalo_tiempo = set_tiempo_entre_coches()
    while True:
        yield env.timeout(random.randint(intervalo_tiempo-2, intervalo_tiempo+2))
        i+=1
        env.process(car(env, llave+" "+str(i), autolavado))

# Create an environment and start the setup process
env = simpy.Environment()
env.process(configuracion(env, ESTACIONES_DE_LAVADO))
env.run(until=TIEMPO_SIMULACION)