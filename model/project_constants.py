class Constants():
    def __init__(self):
        self.estaciones_de_lavado=2 #Initial default value 
        self.tiempo_simulacion=60    #Tiempo en minutos 
        #8HRS = 480min
        self.DIAS=["Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
        self.TIEMPO_ENTRE_VEHICULO=[30,15]
        self.COCHES_MAX_DIA={
                "Martes": 15,
                "Miercoles": 15,
                "Jueves": 15,
                "Viernes": 30,
                "Sabado": 30,
                "Domingo": 30
            }
        self.TIPO_LAVADO={
                "Lavado Normal": 1,
                "Lavado y engrasado": .10,
                "Lavado de vestiduras": 2,
                "Lavado de motor": 2
            }
        self.TIPOS_VEHICULOS={
            "Coche": 15,
            "Camioneta":30,
            "Moto": 7
        }
    def set_washing_stations(self,stations=int) -> None:
        self.estaciones_de_lavado=stations
    def get_washihng_stations(self)->int:
        return self.estaciones_de_lavado
    def set_simulation_time(self, time=int) -> None:
        self.tiempo_simulacion = time 
    def get_simulation_time(self) -> int:
        return self.tiempo_simulacion
    def get_days(self) -> list:
        return self.DIAS
    def get_timeout(self) -> list:
        return self.TIEMPO_ENTRE_VEHICULO
    def get_max_cars(self)->dict:
        return self.COCHES_MAX_DIA
    def get_vehicle_type(self)->dict:
        return self.TIPOS_VEHICULOS
    def get_washing_type(self)->dict:
        return self.TIPO_LAVADO

