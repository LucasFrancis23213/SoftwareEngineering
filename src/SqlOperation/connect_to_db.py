import os
import sys
# add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import mysql.connector
from db_config import config
import time
from logger import logger

class db_connection:
    
    _instance = None

    def __new__(cls, connect_attempt: int, connect_delay: int) -> 'db_connection':
        if cls._instance is None:
            cls._instance = super(db_connection, cls).__new__(cls)
            cls._instance.connect_attempt = connect_attempt
            cls._instance.connect_delay = connect_delay
            cls._instance.db_connector = None
        return cls._instance
        
    def connect_to_db(self) :
        attempt = 1
        while attempt < self.connect_attempt + 1 :
            try:
                self.db_connector = mysql.connector.connect(**config)
                logger.info("successfully connect to " + config['host'] + ":" + config['database'])
                return self.db_connector
            except (mysql.connector.Error, IOError) as err:
                if (self.connect_attempt is attempt):
                    # Attempts to reconnect failed; returning None
                    logger.info("Failed to connect, exiting without a connection: %s", err)
                    return None
                logger.info(
                    "Connection failed: %s. Retrying (%d/%d)...",
                    err,
                    attempt,
                    self.connect_attempt-1,
                )
                # progressive reconnect delay
                time.sleep(self.connect_delay ** attempt)
                attempt += 1
    
    def disconnect_from_db(self) -> bool:
        try:
            self.db_connector.close()
            logger.info("successfully disconnect from db")
            return True
        except Exception as e:
            logger.warning("can not disconnect from db")
            return False

# 测试通过
if __name__ == "__main__" :
    conn_1 = db_connection(connect_attempt=3, connect_delay=2)
    conn_2 = db_connection(connect_attempt=3, connect_delay=2)
    assert conn_2 is conn_1
    conn_2.connect_to_db()