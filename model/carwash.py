from random import randint
import simpy
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
        print("Lavado removio %d%% de %s" %(randint(50, 99), nombre_coche))
