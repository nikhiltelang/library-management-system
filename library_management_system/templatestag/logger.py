from datetime import datetime
import logging
class App_Logger:
    def __init__(self):
        self.logger = logging.basicConfig(level=logging.INFO,filename='library.log', filemode='w', format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',)

    def log(self, file_object, log_message):
        self.now = datetime.now()
        self.date = self.now.date()
        self.current_time = self.now.strftime("%H:%M:%S")
        file_object.write(
            str(self.date) + "/" + str(self.current_time) + "\t\t" + log_message +"\n")

    def info(self,log_message,username=None):
        logging.info(str(username) + "  " + log_message)

    def error(self,log_message,username=None):
        logging.error(str(username) + "  " + log_message)
