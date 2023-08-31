from lib import CONN, CURSOR
from lib.classes.castle import Castle

class Vampire:

    def __init__(self, name, year_born, castle_id, id=None):
        self.name = name
        self.year_born = year_born
        self.castle_id = castle_id

    def __repr__(self):
        return f"Vampire identifier {self.id}, name {self.name}, alive since {self.year_born}, belongs to {self.castle_id}"

    # THIS METHOD WILL CREATE THE SQL TABLE #
    @classmethod
    def create_table(cls):
        # pass

    # ADD YOUR CODE BELOW #
        query = """CREATE TABLE IF NOT EXISTS vampires 
        ( id INTEGER PRIMARY KEY, name TEXT, year_born INTEGER, castle_id INTEGER)"""

        CURSOR.execute(query)

    # Property return the value itself (_) non mutable by the user input
    @property
    def year_born(self):
        return self._year_born

    #The property setter gives the sistem and user the expected input values
    @year_born.setter
    def year_born(self, value):
        if value >= 1430 and value <= 2003:
            self._year_born = value
        else:
            raise ValueError("Year must be a number between 1431 and 2002")
