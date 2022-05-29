from random import randint
import simpy
class AutoLavado():
    def __init__(self, env, estaciones, trabajadores):
        self.env = env
        self.estaciones = simpy.Resource(env, estaciones)
        self.trabajadores = simpy.Resource(env, trabajadores)
        
    def set_tiempo(self, tiempo_lavado=int) -> None:
        self.tiempo_lavado = tiempo_lavado

    def set_trabajadores(self, trabajadores=int) -> None:
        self.trabajadores = trabajadores

    def lavar(self):
        yield self.env.timeout(self.tiempo_lavado)
