import sys
from time import sleep, localtime, strftime
from helper import Helper
import json
from weather import Weather


class App:
    def __init__(self):
        self.run()

    def run(self):
        """main daemon logic"""
        try:
            Helper.cls()
            alarms_list = self.load_alarms('alarms.json')
            weather = Weather()

            while True:
                current_time = strftime("%H:%M:%S", localtime())
                current_seconds = int(strftime("%S", localtime()))

                Helper.cls()
                print('Current Time in {}: {}'.format(weather.location, current_time))
                for alarm in alarms_list:
                    """loop through alarms in loaded json file"""
                    if str(alarm['time']) + ":00" == current_time:
                        print('BEEP BEEP, the time is {}'.format(alarm['time']))
                        if input("Do you want to snooze? N/y ").lower() == "y":
                            print('Snoozing for a minute... Enjoy!')
                            sleep(59)

                if current_seconds == 0:
                    alarms_list = self.load_alarms('alarms.json')

                sleep(1)
        except KeyboardInterrupt:
            Helper.cls()
            print('Good boo!')

    def load_alarms(self, filename):
        try:
            alarms_file = open(filename)
        except FileNotFoundError:
            open(filename, 'a').close()
            self.load_alarms(filename)
        finally:
            alarms_json = json.load(alarms_file)
            try:
                alarms = alarms_json['alarms']
            except KeyError:
                print('Invalid alarm file format. Exiting.')
                sys.exit(1)

            Helper.logger('Alarm list successfully reloaded', 'info')
            return alarms


conditional_alarm = App()
