import time
import control
import database
import drone_servo
from dronekit import LocationGlobalRelative
from detect import detectHumans





def deliverPackage(vehicle, model, enableEdgeTPU):

    homeLat , homeLon = database.getHomeLocation()
    targetLat, targetLon = database.getTargetLocation()
    isStarted = database.isDroneStarted()

    while not isStarted:
        print('Waiting for app to start..')
        time.sleep(2)
        isStarted = database.isDroneStarted()

    homeLat , homeLon = database.getHomeLocation()
    targetLat, targetLon = database.getTargetLocation()

    control.arm_and_takeoff(vehicle,targetAltitude=3)


    print("Set default/target airspeed to 3")
    vehicle.airspeed = 3
    print("Going towards target ...")

    targetPoint = LocationGlobalRelative(targetLat, targetLon, 3)
    vehicle.simple_goto(targetPoint)
    time.sleep(30)
    database.setVehicleMode('hold')

    # Search for humans
    detectHumans(vehicle, model, enableEdgeTPU)

    print('Dropping package..')
    drone_servo.dropPackage()
    database.setPackageDropStatus(True)


    database.setVehicleMode('fly')
    print("Going towards home ...")
    homePoint = LocationGlobalRelative(homeLat,homeLon, 3)
    vehicle.simple_goto(homePoint)

    time.sleep(30)


    control.land(vehicle)

    
