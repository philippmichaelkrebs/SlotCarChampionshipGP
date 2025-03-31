'''
This module is responsible for rendering the results page of the championship.
It uses Jinja2 for templating and generates an HTML file with the results.
It takes a `Championship` object as input and generates an HTML 
file with the results of the championship.
'''

import datetime
from datetime import timedelta
from itertools import count
from jinja2 import Environment, FileSystemLoader
from src.championship import Championship

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

def generate_sprint_ranking_page(championship: Championship) -> None:
    '''
    Compares the results of multiple drivers in the championship.
    
    Parameters
    ------------
    championship: Championship
        The championship object containing the drivers and their results.
    '''
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("sprint_ranking.html")
    data = {
        "championship_name": championship.name,
        "last_update": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
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
    with open("output/championship_sprint_ranking.html", "w", encoding="utf-8") as file:
        file.write(output_html)

def generate_championship_page(championship: Championship) -> None:
    '''Generates the results page for the championship'''
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("championship_ranking.html")

    _driver_prep = championship.get_driver_result(lambda d: (-d.total_laps, d.total_time))
    _idx = 0
    _driver = []
    for driver in _driver_prep:
        _gap = ''
        _person_int_front = ''
        if 0 < _idx:
            # gap to leader
            if driver.total_laps == _driver_prep[0].total_laps:
                _gap = milliseconds_to_time(driver.total_time - _driver_prep[0].total_time)
            else:
                if _driver_prep[0].total_laps - driver.total_laps == 1:
                    _gap = '1 Lap'
                else:
                    _gap = f'{_driver_prep[0].total_laps-driver.total_laps} Laps'

            # gap to person in front
            if driver.total_laps == _driver_prep[_idx-1].total_laps:
                _person_int_front = milliseconds_to_time(driver.total_time -
                                                         _driver_prep[_idx-1].total_time)
            else:
                if _driver_prep[_idx-1].total_laps - driver.total_laps == 1:
                    _person_int_front = '1 Lap'
                else:
                    _person_int_front = f'{_driver_prep[_idx-1].total_laps-driver.total_laps} Laps'

        _driver.append((_gap, _person_int_front, driver))
        _idx += 1

    counter = count(1)
    data = {
        "championship_name": championship.name,
        "last_update": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "results": [
            {
                "position": next(counter),
                "name": res.name,
                "laps": res.total_laps,
                "time": milliseconds_to_time(res.total_time),
                "gap": gap,
                "person_in_front": person_in_front,
                "lap_time": milliseconds_to_time(res.fastest_lap),
            }
            for (gap,person_in_front,res) in _driver
        ],
    }

    output_html = template.render(data)
    with open("output/race_results.html", "w", encoding="utf-8") as file:
        file.write(output_html)

def generate_fastest_lap_page(championship: Championship) -> None:
    '''
    Generates the fastest lap page for the championship.
    '''
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("fastest_lap.html")

    _driver_prep = championship.get_driver_result(lambda d: (d.fastest_lap))
    _idx = 0
    _driver = []
    for driver in _driver_prep:
        _gap = ''
        _person_int_front = ''
        if 0 < _idx:
            # gap to leader
            _gap = milliseconds_to_time(driver.fastest_lap - _driver_prep[0].fastest_lap)

            # gap to person in front
            _person_int_front = milliseconds_to_time(driver.fastest_lap -
                                                         _driver_prep[_idx-1].fastest_lap)

        _driver.append((_gap, _person_int_front, driver))
        _idx += 1

    counter = count(1)
    data = {
        "championship_name": championship.name,
        "last_update": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "results": [
            {
                "position": next(counter),
                "name": res.name,
                "lap_time": milliseconds_to_time(res.fastest_lap),
                "automotive": res.fastest_lap_race_result.car,
                "gap": gap,
                "person_in_front": person_in_front # interval is gap between 2 drivers
            }
            for (gap,person_in_front,res) in _driver
        ],
    }

    output_html = template.render(data)
    with open("output/fastest_lap.html", "w", encoding="utf-8") as file:
        file.write(output_html)

def generate_grand_prix_page(championship: Championship) -> None:
    '''Generates the results page for the championship'''
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("grand_prix.html")

    _race_result_prep = championship.get_driver_result_last_grand_prix()
    _idx = 0
    _race_result = []
    for _result in _race_result_prep:
        _gap = ''
        _person_int_front = ''
        if 0 < _idx:
            # gap to leader
            if _result.laps == _race_result_prep[0].laps:
                _gap = milliseconds_to_time(_result.time - _race_result_prep[0].time)
            else:
                if _race_result_prep[0].laps - _result.laps == 1:
                    _gap = '1 Lap'
                else:
                    _gap = f'{_race_result_prep[0].laps-_result.laps} Laps'

            # gap to person in front
            if _result.laps == _race_result_prep[_idx-1].laps:
                _person_int_front = milliseconds_to_time(_result.time -
                                                         _race_result_prep[_idx-1].time)
            else:
                if _race_result_prep[_idx-1].laps - _result.laps == 1:
                    _person_int_front = '1 Lap'
                else:
                    _person_int_front = f'{_race_result_prep[_idx-1].laps-_result.laps} Laps'

        _race_result.append((_gap, _person_int_front, _result))
        _idx += 1

    counter = count(1)
    data = {
        "championship_name": championship.name,
        "last_update": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "results": [
            {
                "position": next(counter),
                "name": res.driver,
                "laps": res.laps,
                "time": milliseconds_to_time(res.time),
                "car": res.car,
                "gap": gap,
                "person_in_front": person_in_front,
                "lap_time": milliseconds_to_time(res.best_lap_time),
            }
            for (gap,person_in_front,res) in _race_result
        ],
    }

    output_html = template.render(data)
    with open("output/grand_prix.html", "w", encoding="utf-8") as file:
        file.write(output_html)
