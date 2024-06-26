import time
import utils
import database
import delivery
import threading
import log

from dronekit import connect
import argparse  

parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

#parser.add_argument('--connect', default='/dev/ttyAMA0')
parser.add_argument('--connect', default='udp:127.0.0.1:14551')

parser.add_argument(
    '--model',
    help='Path of the object detection model.',
    required=False,
    default='efficientdet_lite0.tflite')

parser.add_argument(
    '--enableEdgeTPU',
    help='Whether to run the model on EdgeTPU.',
    action='store_true',
    required=False,
    default=False)

args = parser.parse_args()

# Connect to the Vehicle
print ('Connecting to vehicle on: %s' % args.connect)
vehicle = connect(args.connect, baud=57600, wait_ready=True)

while not utils.isInternetAvailable():
    print('Waiting for internet connection...')
    time.sleep(5)



database.setConnectionState(True)

connectionState = database.getConnectionState()

while connectionState:

    
    delivery = threading.Thread(target=delivery.deliverPackage, args=(vehicle, args.model, bool(args.enableEdgeTPU)))
    logData = threading.Thread(target=log.logData, args=(vehicle,))


    delivery.start()
    logData.start()


    delivery.join()
    logData.join()

    time.sleep(40)
    connectionState = database.getConnectionState()

vehicle.close()
print('Shutting down')

