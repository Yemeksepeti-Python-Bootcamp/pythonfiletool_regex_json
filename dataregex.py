import sqlite3 as sql
from users import Users
from datetime import datetime

class CreateDB:
    '''
    Created "CreateDB" class for db operations.
    '''
    def __init__(self, path_):
        self.path_ = path_
    
    def date(self):
        '''
        This function give to us date as "yymmdd" format
        '''
        return datetime.now().strftime('%y%m%d')
    
    def __exit__(self):
        '''
        This func for exit all db operations
        '''
        self.cursor.close()
        self.connection.close()
    
    def db_create(self):
        '''
        
        '''
        query = f"""CREATE TABLE İF NOT EXISTS dataregex_table{self.date()}(
            email TEXT NOT NULL,
            username TEXT NOT NULL,
            fullname TEXT NOT NULL,
            emailuserlk TEXT NOT NULL,
            usernamelk TEXT NOT NULL,
            year_of_birth TEXT NOT NULL,
            month_of_birth TEXT NOT NULL,
            day_of_birth TEXT NOT NULL,
            country TEXT NOT NULL,
            ap INTEGER NOT NULL)
        """
        self.connection = sql.connect(self.path_)
        self.cur = self.connection.cursor()
        self.cur.execute(query)
        self.connection.commit()
        self.__exit__()
    
    def db_insert(self):
        query = f"""INSERT INTO dataregex_table{self.date()} VALUES(
            "{Users.email}",
            "{Users.username}",
            "{Users.fullname}",
            "{Users.emailuserlk}",
            "{Users.year_of_birth}",
            "{Users.month_of_birth}",
            "{Users.day_of_birth}",
            "{Users.country}",
            "{Users.ap}"
        )
        """
        self.connection = sql.connect(self.path_)
        self.cur = self.connection.cursor()
        self.cur.execute(query)
        self.__exit__()