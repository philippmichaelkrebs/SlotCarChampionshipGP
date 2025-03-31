'''This module contains the RaceResult class and the RaceResultContainer class.'''

class RaceResult:
    '''RaceResult class stores a result of a race of a driver   '''
    def __init__(self, result: dict[str,any]) -> None:
        self._position = result['position']
        self._driver = result['driver']
        self._laps = result['laps']
        self._time = result['time']
        self._car = result['car']
        self._best_lap_time = result['best_lap_time']
        self._race_id = result['id']

    @property
    def position(self):
        '''return the position of the driver'''
        return self._position

    @position.setter
    def position(self, value):
        if value < 1:
            raise ValueError("Position must be at least 1")
        self._position = value

    @property
    def driver(self):
        '''return the name of the driver'''
        return self._driver

    @driver.setter
    def driver(self, value):
        if not isinstance(value, str):
            raise ValueError("Driver name must be a string")
        self._driver = value

    @property
    def laps(self):
        '''return the number of laps of the driver'''
        return self._laps

    @laps.setter
    def laps(self, value):
        if value < 0:
            raise ValueError("Laps cannot be negative")
        self._laps = value

    @property
    def time(self):
        '''return the time'''
        return self._time

    @time.setter
    def time(self, value):
        if value < 0:
            raise ValueError("Time cannot be negative")
        self._time = value

    @property
    def car(self):
        '''return the name of the car'''
        return self._car

    @car.setter
    def car(self, value):
        if not isinstance(value, str):
            raise ValueError("Car name must be a string")
        self._car = value

    @property
    def best_lap_time(self):
        '''return the best lap time'''
        return self._best_lap_time

    @best_lap_time.setter
    def best_lap_time(self, value):
        if value < 0:
            raise ValueError("Best lap time cannot be negative")
        self._best_lap_time = value

    @property
    def race_id(self):
        '''return the id of the race result'''
        return self._race_id

    @race_id.setter
    def race_id(self, value):
        if value < 0:
            raise ValueError("Race number cannot be negative")
        self._race_id = value

    def __str__(self):
        return (f"Race(Position: {self.position}, Driver: {self.driver}, Laps: {self.laps}, "
                f"Time: {self.time}, Car: {self.car}, Best Lap Time: {self.best_lap_time}, "
                f"Race Number: {self.race_id})")
