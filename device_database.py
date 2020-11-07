'''
Handle database interactions.
Read and write discovered Bluetooth LE devices.
'''

import sqlite3
from app_logger import AppLogger


logger = AppLogger(__name__)


class BluetoothDeviceDatabase:
    def __init__(self, name='ble_devices.db'):
        logger.logger.info("Connecting to database: {}...".format(name))
        self.conn = sqlite3.connect(name) # Sqlite auto-creates DB if it doesn't exist
        self.cursor = self.conn.cursor()
        
        if not self._device_table_exists():
            logger.logger.debug("`devices` table does not exist. Creating...")
            self._create_device_table()
        

    def add_device(self, ble_address, local_name, signal_strength):
        # Add a discovered Bluetooth LE device to the database
        self.cursor.execute("INSERT INTO devices VALUES (?,?,?,?)",
                            ([None, ble_address, local_name, signal_strength]))
        self.conn.commit()
    
    def _device_table_exists(self):
        # Check if the table for Bluetooth devices exists. If SELECT fails, it does not.
        try:
            self.cursor.execute("SELECT * FROM devices")
        except sqlite3.OperationalError as e:
            logger.logger.error(e)
            return False
        except Error as e:
            logger.logger.error(e)
            return False
        return True
    
    def _create_device_table(self):
        # Create a table to store scanned Bluetooth devices in
        try:
            self.cursor.execute(''' CREATE TABLE devices
                                    (device_id INTEGER PRIMARY KEY,
                                    ble_address varchar(17) NOT NULL ,
                                    local_name varchar(20),
                                    signal_strength_dbm INTEGER)''')
        except sqlite3.OperationalError as e:
            logger.logger.error(e)
    
        
        