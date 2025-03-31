'''Runs the file monitoring and processing script.'''
# -*- coding: utf-8 -*-

import os
import sys
import time

from src.renderer import generate_championship_page, generate_sprint_ranking_page
from src.renderer import generate_fastest_lap_page, generate_grand_prix_page
from src.decode_methods import parse_results_cockpitxp

FILE_PATH = ''

def file_has_changed(last_mtime):
    '''Check if the file modification time has changed.'''
    try:
        current_mtime = os.path.getmtime(FILE_PATH)
        return current_mtime != last_mtime, current_mtime
    except FileNotFoundError:
        return False, last_mtime

def monitor_file():
    '''Monitor the file for changes and process it.'''
    inital_run = True
    if inital_run:
        print("Initial run...")
        result = parse_results_cockpitxp(FILE_PATH)
        generate_championship_page(result)
        generate_sprint_ranking_page(result)
        generate_fastest_lap_page(result)
        generate_grand_prix_page(result)
        inital_run = False

    last_mtime = os.path.getmtime(FILE_PATH)  # Get initial modification time
    while True:
        time.sleep(2)  # Check updates every 2 seconds
        changed, last_mtime = file_has_changed(last_mtime)

        if changed:
            print("File updated! Reading new results...")
            result = parse_results_cockpitxp(FILE_PATH)
            generate_championship_page(result)
            generate_sprint_ranking_page(result)
            generate_fastest_lap_page(result)
            generate_grand_prix_page(result)


if len(sys.argv) > 1:
    FILE_PATH = sys.argv[1]
else:
    raise ValueError("Please provide the file path as an argument.")

monitor_file()
