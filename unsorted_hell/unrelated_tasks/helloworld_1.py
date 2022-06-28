# Hello World Example
#
# Welcome to the OpenMV IDE! Click on the green run arrow button below to run the script!

import sensor, image, time
from pyb import I2C
i2c = I2C(4, I2C.MASTER)             # create and init as a master
i2c.init(I2C.MASTER, baudrate=100000) # init as a master

sensor.reset()                      # Reset and initialize the sensor.
sensor.set_pixformat(sensor.RGB565) # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QVGA)   # Set frame size to QVGA (320x240)
sensor.skip_frames(time = 2000)     # Wait for settings take effect.
clock = time.clock()                # Create a clock object to track the FPS.

def safety_send(data):
    try:
        i2c.send(data, 0x10)
#        time.sleep(.01)
    except:
        pass

while(True):
    clock.tick()                    # Update the FPS clock.
    img = sensor.snapshot()         # Take a picture and return the image.
    img.to_grayscale(x_scale=0.20, y_scale=0.20)
    store = img.bytearray()
    print (len(store))
    x=img.width()
    y=img.height()

    print(clock.fps())              # Note: OpenMV Cam runs about half as fast when connected
                                    # to the IDE. The FPS should increase once disconnected.

    slave=i2c.scan()               # scan for slaves on the bus, returning
                                   #   a list of valid addresses
    print(slave)
    nom = 0
    if (i2c.is_ready(0x10)):

        for y1 in range(y):
            for x1 in range(x):
                #safety_send(store[nom])
                b=store[nom]
                if (b<128): safety_send('*')
                else: safety_send('.')
                nom=nom+1
            safety_send('\n')

#        safety_send('123'*10)
#        safety_send('info')
        safety_send('\n')
        time.sleep(2)
