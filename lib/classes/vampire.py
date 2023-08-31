from lib import CONN, CURSOR
from lib.classes.castle import Castle

class Vampire:

    # CLASS INITALIZER #
    def __init__(self, name, year_born, castle_id, id=None):
        self.name = name
        self.year_born = year_born
        self.castle_id = castle_id
        self.id = id

    # CLASS REPR #
    def __repr__(self):
        return f"Vampire identifier {self.id}, name {self.name}, on earth since {self.year_born}, belongs to castle {self.castle_id}"

    # THIS METHOD WILL CREATE THE SQL TABLE #
    @classmethod
    def create_table(cls):
        query = """CREATE TABLE IF NOT EXISTS vampires 
        ( id INTEGER PRIMARY KEY, name TEXT, year_born INTEGER, castle_id INTEGER)"""

        CURSOR.execute(query)

    # DELETE TABLE AND ITS CONTENT #
    @classmethod
    def drop_table(cls):
        query = "DROP TABLE vampires"

        CURSOR.execute(query)

    """PROPERTY RETURNS THE VALUE ITSELF 
    (THE `_` DOES NOT ALLOW THE VALUE TO MANIPULATED BY THE USER)"""
    @property
    def year_born(self):
        return self._year_born

    #The property setter gives the system and user the expected input values
    @year_born.setter
    def year_born(self, value):
        if value >= 1430 and value <= 2003:
            self._year_born = value
        else:
            raise ValueError("Year must be a number between 1431 and 2002")

    # Send new vampire to database
    def create(self):
        query = "INSERT INTO vampires (name, year_born, castle_id) VALUES (?,?,?)"

        # The (Create) uses the values passed in to the query to process
        # the information withing the CURSOR
        CURSOR.execute(query, [self.name, self.year_born, self.castle_id])
        
        # The CONN is required anytimme whe edit data on the database
        CONN.commit()
        
        # self.[value] works to get the id to the current query
        self.id = CURSOR.lastrowid
        return self

    # Send vampire most recent fact to database
    def update(self):
        query = """UPDATE vampires 
        SET name = ?, year_born = ?, castle_id = ?
        WHERE id = ?"""
        
        CURSOR.execute(query, [self.name, self.year_born, self.castle_id, self.id])
        
        CONN.commit()

    @classmethod
    def query_all(cls):
        query = "SELECT * FROM vampires"
        
        rows = CURSOR.execute(query).fetchall()
        
        # Select the properties of each column to map it into a list
        return [Vampire(row[1], row[2], row[3], row[0]) for row in rows]

    @property
    def castle(self):
        query = "SELECT * FROM castles WHERE id = ?"
        
        # Search by vampire and returns the respective castle for the vampire
        row = CURSOR.execute(query, [self.castle_id]).fetchone()

        if row :
            return Castle(row[1], row[0])
        
    #Sets the value for the catle and trow error if the castle type is wrong (id) 
    @castle.setter
    def castle (self, value):
        if isinstance(value, Castle):
            self.castle_id = value.id
        else:
            raise ValueError("Invalid castle try again with a different castle type")
