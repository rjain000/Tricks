from pynotifier import Notification
import psutil

battery=psutil.sensors_battery()
percent=battery.percent
Notification("Battery per",str(percent)+"%percent remaining", duration=10).send()