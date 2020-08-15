import psutil                  #pip install psutil
import time 
from plyer import notification #pip install plyer

battery = psutil.sensors_battery()
percent = battery.percent

if __name__=="__main__":
    notification.notify(
        title="**Battery Percent",
        message=str(percent)+ " % Battery",
        app_icon="battery.ico",
        timeout=10
    )



