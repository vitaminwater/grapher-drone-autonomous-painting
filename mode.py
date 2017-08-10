from dronekit import connect, VehicleMode

banksy = connect('/dev/ttyAMA0', wait_ready=True, baud=921600)

print "connected"

banksy.mode = VehicleMode("STABILIZE")
banksy.armed = True
while not banksy.mode.name=='STABILIZE' and not banksy.armed:
    print " Getting ready to take off ..."
    time.sleep(1)

print "Ready"
