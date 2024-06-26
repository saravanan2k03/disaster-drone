import time
import database

def logData(vehicle):

    isStarted=database.isDroneStarted()

    while not isStarted:
        time.sleep(2)
        isStarted = database.isDroneStarted()

    while isStarted:
        voltage = vehicle.battery.voltage
        speed = float("{:.1f}".format(vehicle.airspeed))
        altitude = vehicle.location.global_relative_frame.alt
        latitude = vehicle.location.global_relative_frame.lat
        longitude = vehicle.location.global_relative_frame.lon
        database.setVehicleData(voltage=voltage, altitude=altitude,
                                latitude=latitude, longitude=longitude, speed=speed)
        time.sleep(3)
        isStarted = database.isDroneStarted()

    voltage = vehicle.battery.voltage
    altitude = vehicle.location.global_relative_frame.alt
    latitude = vehicle.location.global_relative_frame.lat
    longitude = vehicle.location.global_relative_frame.lon
    database.setVehicleData(voltage=voltage, altitude=altitude,
                                latitude=latitude, longitude=longitude, speed=0)
