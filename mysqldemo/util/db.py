import pymysql
import pymysql.cursors
from config import *

class DB:
    '''
    同步数据库操作类 TODO
    '''

    @classmethod
    def connect(cls, cursorclass=pymysql.cursors.DictCursor):
        '''
        
        '''
        return pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS,
            cursorclass=cursorclass
        )

    @classmethod
    def db_exec(cls, sql, params):
        '''
        
        '''

        with cls.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql, params)
            conn.commit()

    @classmethod
    def db_find(cls, sql, params):
        '''
        
        '''


    