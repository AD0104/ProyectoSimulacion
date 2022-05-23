from simpy.core import Environment
from  simpy_config import configuracion
def set_entry_data(root):
    global data_dict
    data_dict = {
        "stations": root.get_washing_stations(),
        "simulation-time": root.get_simulation_time(),
        "simulation-day": root.get_simulation_day(),
        "wash-type": root.get_wash_type()
    }
    set_simpy_env()
def get_entry_data()->dict:
    return data_dict
def set_simpy_env():
    env = Environment()
    general_data = get_entry_data()
    env.process(configuracion(env, general_data['stations'], general_data["simulation-day"]))
    env.run(until=general_data['simulation-time'])
