
import datetime
from typing import List
from src.race import RaceResult
from src.driver import Driver

class GrandPrix:
    '''Grand Prix class assigns results to a grand prix'''

    def __init__(self, name:str, date:datetime.datetime, location:str):
        '''Initializes a Grand Prix with name, date, and location.'''
        self._name = name
        self._date = date
        self._location = location
        self._results : List[RaceResult] = []

    @property
    def name(self) -> str:
        '''Returns the name of the Grand Prix.'''
        return self._name

    @property
    def results(self) -> List[RaceResult]:
        '''Returns the results of the Grand Prix.'''
        return self._results

    def add_race_result(self, race_result: 'RaceResult') -> None:
        '''
        Adds a RaceResult to the results list.
        
        Parameters
        ------------
        race_result: 'RaceResult'
            The RaceResult to be added.
        '''
        self._results.append(race_result)


class Championchip:
    '''Championchip class assigns grand prix to a championchip'''

    def __init__(self, name:str, date:datetime.datetime):
        '''Initializes a Championchip with name and date.'''
        self.name = name
        self.date = date
        self.drivers : List[Driver] = []
        self.grand_prix : List[GrandPrix] = []

    def add_result(self, grandprix: GrandPrix) -> None:
        """
        Adds a grand prix to the championchip.

        Parameters
        ------------
        grandprix: 'GrandPrix'
            The GrandPrix to be added.
        """
        self.grand_prix.append(grandprix)
        for _race_result in grandprix.results:
            self.get_driver_by_name(_race_result.driver).add_race(_race_result)

    def get_driver_by_name(self, name: str, create: bool = True) -> Driver:
        '''
        Returns a driver by name, creates one if it does not exist

        Parameters
        ------------
        name: 'str'
            The name of the driver to be returned.
        create: 'bool', default None
            Optional parameter to create a new driver if it does not exist.

        Returns
        ------------
        Driver
            Driver object if found, otherwise None.

        '''
        if not isinstance(name, str):
            raise ValueError("Driver name must be a string")
        for driver in self.drivers:
            if driver.name == name:
                return driver
        if create:
            new_driver = Driver(name)
            self.drivers.append(new_driver)
            return new_driver
        else:
            return None

    def get_driver_result(self) -> List[Driver]:
        '''
        Returns the best result of all drivers
        
        Returns
        ------------
        list
            List of Driver objects sorted by best grand prix results.
        '''
        print(len(self.drivers))
        if not self.drivers:
            return []
        sorted_drivers = sorted(self.drivers, key=lambda d: (-d.best_grand_prix.laps, d.best_grand_prix.time))
        return sorted_drivers

    def get_race_result(self) -> List[RaceResult]:
        '''
        Returns the best result of all drivers
        
        Returns
        ------------
        list
            List of sorted RaceResult objects by laps and time.
        '''
        print(len(self.drivers))
        if not self.drivers:
            return []
        drivers_best_results = [d.get_best_race() for d in self.drivers]
        sorted_drivers = sorted(drivers_best_results, key=lambda d: (-d.laps, d.time))
        return sorted_drivers

    def get_grand_prix_index(self) -> int:
        '''
        Returns the index of the grand prix in the list.
        
        Returns
        ------------
        int
            Index of the grand prix. If no grand prix exists, returns 1.
        '''
        return len(self.grand_prix) + 1

    def create_grand_prix(self) -> GrandPrix:
        '''
        Creates a grand prix and returns it.
        
        Returns
        ------------
        GrandPrix
            A new GrandPrix object.
        '''
        grand_prix = GrandPrix(f"Grand Prix {self.get_grand_prix_index()}", self.date, "Location")
        return grand_prix

    def get_grand_prix(self, index:int) -> GrandPrix:
        '''
        Returns the grand prix to the given index
        
        Parameters
        ------------
        index: 'int'
            The index of the grand prix to be returned.

        Returns
        ------------
        GrandPrix
            GrandPrix object at the specified index.
        '''
        if not self.grand_prix:
            return None
        if index < 1 or index > len(self.grand_prix):
            raise ValueError("Index out of range")
        return self.grand_prix[index - 1]
