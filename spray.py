import time
from dronekit import connect, VehicleMode

banksy = connect('/dev/ttyAMA0', wait_ready=True, baud=921600)

print "connected"

while True:
    if banksy.channels['6'] > 1500: break
    banksy.channels.overrides['8'] = 1934
    time.sleep(5)
    banksy.channels.overrides['8'] = 1094
    time.sleep(5)

banksy.channels.overrides['8'] = None

print "Ready"
