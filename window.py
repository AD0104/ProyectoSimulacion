from tkinter import StringVar, Tk
from tkinter import ttk
import tkinter as tk
from middle import set_entry_data 
class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Simulador de Auto Lavado")
        self.configure(width=600, height=800)
        self.configure(bg='lightgray')

        tk.Label(self, text="Estaciones de lavado").grid(column=0, row=0)
        self.washing_station_entry = StringVar()
        tk.Entry(self, textvariable=self.washing_station_entry).grid(column=1, row=0)

        tk.Label(self, text="Tiempo de simulacion").grid(column=3, row=0)
        self.simulation_time = StringVar()
        tk.Entry(self, textvariable=self.simulation_time).grid(column=4, row=0)

        self.current_var_simday = StringVar()
        tk.Label(self, text="Dia de simulacion").grid(column=6, row=0)
        current_simulation_day = ttk.Combobox(self, textvariable=self.current_var_simday)
        current_simulation_day['values'] = [
            "Martes",
            "Miercoles",
            "Jueves",
            "Viernes",
            "Sabado",
            "Domingo"
        ]
        current_simulation_day['state']='readonly'
        current_simulation_day.current(newindex=0)
        current_simulation_day.grid(column=7, row=0)

        self.current_var_washtype = StringVar()
        tk.Label(self, text="Tipo de lavado").grid(column=8, row=0)
        wash_type = ttk.Combobox(self, textvariable=self.current_var_washtype)
        wash_type['values'] = [
            "Lavado Normal",
            "Lavado y engrasado",
            "Lavado de vestiduras",
            "Lavado de motor"
        ]
        wash_type['state']='readonly'
        wash_type.current(newindex=0)
        wash_type.grid(column=9, row=0)

        tk.Button(self, text="Guardar", command=self.transport_data).grid(column=0, row=1)

        self.mainloop()
    def get_washing_stations(self)->int:
        entry_value = self.washing_station_entry.get()
        if(entry_value == ""):
            print("Error, empty field")
            return -1
        return int(entry_value)
    def get_simulation_time(self):
        entry_value = self.simulation_time.get()
        if(entry_value == ""):
            print("Error, empty field")
            return -1
        return int(entry_value)
    def get_simulation_day(self):
        return self.current_var_simday.get()
    def get_wash_type(self):
        return self.current_var_washtype.get()
    def transport_data(self):
        set_entry_data(self)
