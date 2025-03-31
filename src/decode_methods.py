'''
Methods to decode the results from different formats.
'''

import re
import datetime
from src.championship import GrandPrix, Championship
from src.race import RaceResult

def remove_extra_whitespaces(text:str) -> str:
    '''
    Removes extra whitespaces from a string.
    
    Parameters
    ------------
    text: str
        The string from which to remove extra whitespaces.
    
    Returns
    ------------
    str
        The string with extra whitespaces removed.
    '''
    return re.sub(r'\s+', ' ', text).strip()


def parse_results_cockpitxp(file_path:str) -> Championship:
    '''
    Parses the results from a file and returns a Championchip object.
    The file is expected to be in the cockpitXP format.
    
    Parameters
    ------------
    file_path: str
        The path to the file to be parsed.
    
    Returns
    ------------
    Championchip
        The Championchip object containing the parsed results.
    '''
    grand_prix : GrandPrix = None
    championchip = Championship("Ferraro", datetime.datetime.now())

    with open(file_path, "r", encoding="utf-8") as reader:
        for line in reader:
            if line.startswith("----"):
                if grand_prix:
                    championchip.add_result(grand_prix)
                grand_prix = championchip.create_grand_prix()
                continue
            if len(line) < 99:
                continue

            name = line[:25].rstrip().encode("cp273", "ignore").decode("cp273")
            if not re.sub(r'\s+', '', name):
                continue
            name = remove_extra_whitespaces(name)

            result = {'driver': name}

            result['car'] = remove_extra_whitespaces(line[25:80])
            result['laps'] = int(re.sub(r'\s+', '', line[80:86]))
            result['time'] = int(re.sub(r'\s+', '', line[86:96]))
            result['position'] = int(re.sub(r'\s+', '', line[96:99]))
            result['best_lap_time'] = int(re.sub(r'\s+', '', line[99:]))
            result['id'] = grand_prix.id

            _res = RaceResult(result)
            grand_prix.add_race_result(_res)

    championchip.add_result(grand_prix)
    return championchip
