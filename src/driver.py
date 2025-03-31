'''all race results of a driver'''
from typing import List
from src.race import RaceResult

class Driver:
    '''Driver class assignes races.'''
    def __init__(self, name: str):
        self._name = name
        self.race_results: List[RaceResult] = []

    def add_race(self, race_result:RaceResult) -> None:
        '''
        Adds a race to the driver.
        
        Parameters
        ------------
        race_result: RaceResult
            The RaceResult to be added.
        '''
        self.race_results.append(race_result)

    @property
    def name(self) -> str:
        '''returns the name of the driver'''
        return self._name

    @property
    def total_laps(self) -> int:
        '''returns the total number of laps of the driver'''
        return sum(r.laps for r in self.race_results)

    @property
    def total_time(self) -> int:
        '''returns the total time of the driver'''
        return sum(r.time for r in self.race_results)

    @property
    def number_of_grands_prix(self) -> int:
        '''returns number of races'''
        return len(self.race_results)

    @property
    def best_grand_prix(self) -> RaceResult:
        '''
        Returns the best grand prix of the driver.
        The best grand prix is the one with the most laps completed.'
        '''
        if not self.race_results:
            return None
        # Max rounds, then min time
        best_race = min(self.race_results, key=lambda r: (-r.laps, r.time))
        return best_race

    @property
    def fastest_lap_race_result(self) -> RaceResult:
        '''
        Returns race result with the fastest lap of the driver.

        Returns
        ------------
        result: RaceResult
            RaceResult with the fastest lap of the driver.
        '''
        if not self.race_results:
            return None
        best_race = min(self.race_results, key=lambda r: (r.best_lap_time))
        return best_race

    @property
    def fastest_lap(self) -> int:
        '''returns the time of the fastest lap of the driver'''
        return self.fastest_lap_race_result.best_lap_time
