import time
from dronekit import connect, VehicleMode

banksy = connect('/dev/ttyAMA0', wait_ready=True, baud=921600)

print 'Waiting for channel 6'

while banksy.channels['6'] < 1500:
    time.sleep(1)

print 'Channel 6 down'
