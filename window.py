from tkinter import StringVar, Tk, END, NORMAL
from tkinter import Text
from tkinter import ttk
import tkinter as tk
from turtle import heading
from middle import set_entry_data, get_arriving_text, get_entry_text, get_out_text 
from middle import get_simulation_times
class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Simulador de Auto Lavado")
        self.configure(width=600, height=800)
        self.configure(bg='lightgray')

        mid_window_pady = 400
        general_pady=5
        
        width=50
        height=5

        tk.Label(self, text="Estaciones de lavado").grid(column=0, row=0, pady=(mid_window_pady,0))
        self.washing_station_entry = StringVar()
        tk.Entry(self, textvariable=self.washing_station_entry).grid(column=1, row=0, pady=(mid_window_pady,0))

        tk.Label(self, text="Tiempo de simulacion").grid(column=0, row=1)
        self.simulation_time = StringVar()
        tk.Entry(self, textvariable=self.simulation_time).grid(column=1, row=1)

        self.current_var_simday = StringVar()
        tk.Label(self, text="Dia de simulacion").grid(column=0, row=2)
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
        current_simulation_day.grid(column=1, row=2)

        tk.Button(self, text="Guardar", command=self.transport_data).grid(column=0, row=3)
        tk.Button(self, text="Borrar", command=self.clean_tas).grid(column=1, row=3)

        tk.Label(self, text="Llegada al autolavado").grid(column=3, row=0, pady=(mid_window_pady, 0))
        self.arriving_text_area = Text(self, height=height, width=width)

        tk.Label(self, text="Entrada a lavado").grid(column=3, row=1)
        self.entry_wash_text_area = Text(self, height=height, width=width)

        tk.Label(self, text="Salida del lavado").grid(column=3, row=3)
        self.out_wash_text_area = Text(self, height=height, width=width)

        tk.Label(self, text="Tiempos totales").grid(column=3, row=4)
        self.total_time = Text(self, height=height, width=width)

        tk.Label(self, text="Tiempo medio").grid(column=5, row=4)
        self.average_time = Text(self, height=height, width=width)

        self.arriving_text_area.grid(column=2, row=0, pady=(mid_window_pady, 0))
        self.entry_wash_text_area.grid(column=2, row=1)
        self.out_wash_text_area.grid(column=2, row=3)
        self.total_time.grid(column=2, row=4)
        self.average_time.grid(column=4, row=4)

        self.mainloop()

    def get_washing_stations(self)->int:
        entry_value = self.washing_station_entry.get()
        if(entry_value == ""):
            try:
                self.spawn_popup()
                raise ValueError
            except: 
                pass
        return int(entry_value)
    def get_simulation_time(self):
        entry_value = self.simulation_time.get()
        if(entry_value == ""):
            try:
                self.spawn_popup()
                raise ValueError
            except ValueError as ve:
                pass
        return int(entry_value)
    def spawn_popup(self):
        popup = tk.Toplevel(self)
        popup.wm_title("Error")
        tk.Label(popup, text="Campo vacio").pack(side='top', fill='x', pady=10)
        tk.Button(popup, text="Aceptar", command=popup.destroy).pack()
    def get_simulation_day(self):
        return self.current_var_simday.get()
    def update_arriving_ta(self, text):
        self.arriving_text_area.insert("end", text)
    def update_entry_ta(self, text):
        self.entry_wash_text_area.insert('end', text)
    def update_out_ta(self, text):
        self.out_wash_text_area.insert('end', text)
    def update_totalT_ta(self, text):
        self.total_time.insert('end', text)
    def update_averageT_ta(self, text):
        self.average_time.insert(END,text)
    def clean_tas(self):
        self.arriving_text_area.delete('0.0', END)
        self.entry_wash_text_area.delete('0.0', END)
        self.out_wash_text_area.delete('0.0', END)
        self.total_time.delete('0.0',END)
        self.average_time.delete('0.0', END)

    def transport_data(self):
        set_entry_data(self)

        text = get_arriving_text()
        send_text = ""
        for curr_text in text:
            send_text+=curr_text
            send_text+='\n'
        self.update_arriving_ta(send_text)

        send_text=""
        text=get_entry_text()
        for curr_text in text:
            send_text+=curr_text
            send_text+='\n'
        self.update_entry_ta(send_text)

        send_text=""
        text=get_out_text()
        for curr_text in text:
            send_text+=curr_text
            send_text+='\n'
        self.update_out_ta(send_text)

        local_dict = get_simulation_times()
        total_times, average_times = "",""
        for key, value in local_dict.items():
            if("total" in key):
                total_times+=(key+": "+str(value))
                total_times+='\n'
            else:
                average_times+=(key+": "+str(value))
                average_times+='\n'
        self.update_totalT_ta(total_times)
        self.update_averageT_ta(average_times)
