from simpy.core import Environment
from  simpy_config import configuracion
from simpy_config import get_times
def set_entry_data(root):
    global data_dict
    data_dict = {
        "stations": root.get_washing_stations(),
        "simulation-time": root.get_simulation_time(),
        "simulation-day": root.get_simulation_day()
    }
    set_simpy_env()
def get_entry_data()->dict:
    return data_dict
def set_simulation_times(times: dict)->None:
    global sim_times 
    sim_times = times
def get_simulation_times()->dict:
    return sim_times
def set_simpy_env():
    env = Environment()
    general_data = get_entry_data()
    env.process(configuracion(env, general_data['stations'], general_data["simulation-day"]))
    env.run(until=general_data['simulation-time'])
    get_times()
