from sheetfu import SpreadsheetApp
import sched
import time
from time import sleep


from threading import Timer

#Setting up the Reapeated Timer class 
class RepeatedTimer():
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False


scheduler = sched.scheduler(time.time, time.sleep)
# Accessing the sheet 
sa = SpreadsheetApp('/Users/loicalix-brown/Documents/UniWork/HCR/HCR.json')
spreadsheet = sa.open_by_url(url='https://docs.google.com/spreadsheets/d/1s5Eu9foYRzJPQ9-k__CtCC0xfYES5D0h2s9j7a-iDuQ/edit?fbclid=IwAR3sGGrg41u9lMYpmeYZFFBBjc1Qr90PHP74ofCUEE_5VMgtDW74UC7u2Ls#gid=1211208218')
sheet1 = spreadsheet.get_sheet_by_name('Sample_for_analysis')

#Use of global variable to be able to change it asynchronously during the repeated tasks
global data_range_old 
data_range_old = sheet1.get_data_range()

#Gets the updated dimensions of the sheet 
def update_range(sheet1):
    global data_range_old
    data_range_old = sheet1.get_data_range()

#Check if the old dimensions ae equal to the new dimensions
def check_sheet(sheet1):
    global data_range_old
    data_range_new = sheet1.get_data_range()
    if data_range_new.get_max_row() != data_range_old.get_max_row():
        print('New entry')
        update_range(sheet1)
        #Call the data analysis script to analyse new data 
        import spreadsheet
    else:
        print("No entry")
        data_range_old = sheet1.get_data_range()

#Repeated task set with a delay of 5s
print ("starting...")
rt = RepeatedTimer(5, check_sheet, sheet1) # it auto-starts, no need of rt.start()
try:
    sleep(500) #Sets how long it should run for
     
finally:
    rt.stop()


