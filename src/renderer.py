'''
This module is responsible for rendering the results page of the championship.
It uses Jinja2 for templating and generates an HTML file with the results.
It takes a `Championchip` object as input and generates an HTML 
file with the results of the championship.
'''

from datetime import timedelta
from jinja2 import Environment, FileSystemLoader
from src.championchip import Championchip

def milliseconds_to_time(milliseconds:int) -> str:
    '''
    Converts milliseconds to a formatted time string.
    
    Parameters
    ------------
    milliseconds: int
        The time in milliseconds to be converted.
    
    Returns
    ------------
    str
        The formatted time string in the format "mm:ss:fff".
    '''
    time = timedelta(milliseconds=milliseconds)
    minutes, seconds = divmod(time.total_seconds(), 60)
    millis = int(milliseconds % 1000)
    return f"{int(minutes)}:{int(seconds):02}.{millis:03}"

def generate_results_page(championship: Championchip) -> None:
    '''Generates the results page for the championship'''
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("best_races.html")

    data = {
        "championship_name": championship.name,
        "results": [
            {
                "position": res.best_grand_prix.position,
                "name": res.name,
                "laps": res.best_grand_prix.laps,
                "time": milliseconds_to_time(res.best_grand_prix.time),
                "car": res.best_grand_prix.car,
                "lap_time": milliseconds_to_time(res.fastest_lap),
                "best_placement": res.best_grand_prix.position,
                "num_grand_prix": res.number_of_grands_prix,
                "best_grand_prix": res.best_grand_prix.race_id,
            }
            for res in championship.get_driver_result()
        ],
    }

    output_html = template.render(data)
    with open("output/race_results.html", "w", encoding="utf-8") as file:
        file.write(output_html)
