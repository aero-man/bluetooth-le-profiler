'''
Write logs to file specified in `settings.py`
Logfile name is specifies
'''
import logging
import settings


class AppLogger():
    def __init__(self, module_name):
        '''
        Creates two loggers. One for the logfile, one for command-line output.
        '''
        self.logger = logging.getLogger(module_name)
        self.logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler(settings.MAIN_LOG_FILENAME)
        fh.setLevel(logging.DEBUG)
        sh = logging.StreamHandler()
        sh.setLevel(logging.INFO)
        logfile_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        command_line_formatter = logging.Formatter('%(message)s')
        fh.setFormatter(logfile_formatter)
        sh.setFormatter(command_line_formatter)
        self.logger.addHandler(fh)
        self.logger.addHandler(sh)