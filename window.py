from tkinter import StringVar, Tk, END
from tkinter import ttk
import tkinter as tk
from middle import set_entry_data, get_arriving_text, get_entry_text, get_out_text 
class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Simulador de Auto Lavado")
        self.configure(width=600, height=800)
        self.configure(bg='lightgray')

        mid_window_pady = 400 
        
        general_padx = 10
        general_pady = 10

        tk.Label(self, text="Estaciones de lavado").grid(column=0, row=0, padx=general_padx, pady=(mid_window_pady, 0))
        self.washing_station_entry = StringVar()
        tk.Entry(self, textvariable=self.washing_station_entry).grid(column=1, row=0, padx=general_padx, pady=(mid_window_pady,0))

        tk.Label(self, text="Tiempo de simulacion").grid(column=0, row=1, padx=general_padx, pady=general_pady)
        self.simulation_time = StringVar()
        tk.Entry(self, textvariable=self.simulation_time).grid(column=1, row=1, padx=general_padx, pady=general_pady)

        self.current_var_simday = StringVar()
        tk.Label(self, text="Dia de simulacion").grid(column=0, row=2, padx=general_padx, pady=general_pady)
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
        current_simulation_day.grid(column=1, row=2, padx=general_padx, pady=general_pady)
        tk.Button(self, text="Guardar", command=self.transport_data).grid(column=0, row=3, columnspan=2, padx=general_padx, pady=general_pady)

        tk.Label(self, text="Llegada al autolavado").grid(column=3, row=0, padx=general_padx, pady=general_pady)
        self.arriving_text_area = tk.Text(self, height=10, width=150)
        self.arriving_text_area['state']='disabled'
        self.arriving_text_area.grid(column=2, row=0, padx=general_padx, pady=general_pady)

        tk.Label(self, text="Entrada a lavado").grid(column=3, row=1, padx=general_padx, pady=general_pady)
        self.entry_wash_text_area = tk.Text(self, height=10, width=150)
        self.entry_wash_text_area['state']='disabled'
        self.entry_wash_text_area.grid(column=2, row=1, padx=general_padx, pady=general_pady)

        tk.Label(self, text="Salida del lavado").grid(column=3, row=3, padx=general_padx, pady=general_pady)
        self.out_wash_text_area = tk.Text(self, height=10, width=150)
        self.out_wash_text_area['state']='disabled'
        self.out_wash_text_area.grid(column=2, row=3, padx=general_padx, pady=general_pady)

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
        self.arriving_text_area['state']='normal'
        self.arriving_text_area.delete(1.0, "end")
        self.arriving_text_area.insert("end", text)
        self.arriving_text_area['state']='disabled'
    def update_entry_ta(self, text):
        self.entry_wash_text_area['state']='normal'
        self.entry_wash_text_area.delete(1.0, 'end')
        self.entry_wash_text_area.insert('end', text)
        self.entry_wash_text_area['state']='disabled'
    def update_out_ta(self, text):
        self.out_wash_text_area['state']='normal'
        self.out_wash_text_area.delete(1.0, 'end')
        self.out_wash_text_area.insert('end', text)
        self.out_wash_text_area['state']='disabled'
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

