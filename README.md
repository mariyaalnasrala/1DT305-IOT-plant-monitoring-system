# **Green Guardian: Smart Plant Monitoring System**

Mariya Al Nasrala (ID: ma227ji)

The project involves creating a simple IoT (Internet of Things) solution to monitor the environment of your plants.

The device developed in this project will be capable of monitoring various aspects of the plants environment, such as soil moisture and sunlight levels.

The project is relatively short and easy to complete, provided you have obtained all the necessary hardware components required to bring it to fruition. The creation process should not be unduly lengthy. Ideally, after following this tutorial, the project should be completable within a maximum timeframe of 5 - 10 hours.

## **Objective**

There are several reasons behind this device. The first reason is that my mom loves plants and has many at home, so I want to create something that can make her happy. The second reason is that I also like plants, but I'm very bad at taking care of them and I don't know when they need to be watered or how much water they need, I don't know also if the plants need sunlight or not.

I don't want my plants to die, so this device can help me know if they need water or not, and if they need sunlight or not. Another reason is that this course is interesting, and I want to have some understanding of how things work in the machines we use.

With this project tutorial, you will learn the basics of setting up sensors with a microcontroller. You will also learn some very basic electronics in order to monitor your plants. The device will help you understand your plants and their needs, as you will be able to see how often they need water and sunlight. You can also add more sensors or use a water pump to water the plants when they need it.


## **Material**


| Material |Link| Price in Kr|
| -------- |----- |-------- |
|Addon Kit - Applied IoT at Linnaeus University (2024)|[Link](https://www.electrokit.com/en/addon-kit-applied-iot-at-linnaeus-university-2023)| 349 |
|Light sensor|[Link](https://www.electrokit.com/en/ljussensor) | 39|
|soil moisture sensor|[Link](https://www.electrokit.com/en/jordfuktighetssensor) | 29|

*Table1*

In Table 1 will provide a list of the materials needed to complete the project. Some are additional, and the project can be completed without them, while others are necessary.

### **Necessary material**

| Material |Description|Link|Price in kr|
|----------|-----------|----|-----------|
|Breadboard|A platform for building and testing electronic circuits without soldering.|[Link](https://www.electrokit.com/kopplingsdack-840-anslutningar)|69
Raspberry Pi Pico WH|A microcontroller with Wi-Fi that processes sensor data and sends it to the internet.|[Link](https://www.electrokit.com/raspberry-pi-pico-wh)|109
| Light Sensor|Measures light intensity to monitor the amount of sunlight your plant receives.|[Link](https://www.electrokit.com/ljussensor)|39| 
Soil Moisture Sensor|Measures soil moisture levels to determine if the plant needs watering.|[Link](https://www.electrokit.com/jordfuktighetssensor)|29|
Wires| Connect components on the breadboard and to the Raspberry Pi Pico W, allowing signals to travel between them.|[Link](https://www.electrokit.com/labsladd-1-pin-hane-hona-150mm-10-pack)|29|
Jumper wires 1-pin male-male|Connecting sensors to the microcontroller for measuring parameters such as soil moisture, light and temperature.|[Link](https://www.electrokit.com/en/labsladd-1-pin-hane-hane-150mm-10-pack)|29|
USB cable A male - micro B male|The cable would enable data transfer between the microcontroller and the computer for programming, updating and transfer of measurement data.|[Link](https://www.electrokit.com/usb-kabel-a-hane-micro-b-hane-15cm?gad_source=1&gclid=CjwKCAjwyo60BhBiEiwAHmVLJcHxvpHLnz3UbNrhxQrmy2rmxYSukOvyhDYlSCtpJebukK6dY_RLfhoCh6wQAvD_BwE)|19

*Table2*






The price changes depending on order quantity and quality.

All items in the table above has been bought from [Electrokit](https://www.electrokit.com/).
You can also buy just the hardware shown in the picture below/ table 2. That will be enough to complete this project.
![iot-hardware](https://hackmd.io/_uploads/Bk5HtrvI0.jpg)



## **Computer setup**

For this project, the development environment used was [Visual Studio Code](https://code.visualstudio.com/). To transfer the code to the Pico WH, the [pymakr](https://github.com/sg-wireless/pymakr-vsc/blob/HEAD/GET_STARTED.md) extension within VSCode was utilized.

The operating system should not be a factor in this project, so any OS will work just fine.

### **Step-by-step**

* Get VSCode if you don't already have it installed.
* Install Python if it's not already on your system.
* Acquire the PyMakr extension within VSCode.
* Update the firmware on the microcontroller. If you're using a Raspberry Pi Pico, follow these steps:

    I. Download the MicroPython [firmware](https://micropython.org/download/RPI_PICO_W/). Use the latest version under "Releases" and not "Preview Builds".

    II. Connect the Micro-USB cable to the Pico.

    III. While holding down the BOOTSEL button on the RPi Pico, plug the other end of the cable into your computer.

    IV. A new device named RPI-RP2 should now appear in your file system. Copy the file from step 1 into its storage.

    V. Wait patiently. The board should automatically disconnect and then reconnect to your computer. This process may take some time.
* The setup is complete! You can now start coding.

You can  found more information [here](https://hackmd.io/@lnu-iot/rkFw7gao_).

## **Putting everything together**

The circuit diagram for the project can be seen below:
![circuit diagram](https://hackmd.io/_uploads/B1NXp8_LC.jpg)


The Pico WH microcontroller powers the breadboard via the 3v3 pin (pin 36) and connects the breadboard to ground via pin 38.

Breadboard:
A breadboard is used to easily connect all components without the need for soldering. It makes it easy to experiment and build prototypes. All sensors are powered via the breadboard's power and ground lines.

Light sensor (connected to GP26):
It is connected to the analog input GP26 (pin 31) on the Raspberry Pi Pico.

Soil moisture sensor (connected to GP27):
It is connected to the analog input GP27 (pin 32) of the Raspberry Pi Pico.

Light sensor:
VCC <----to----> 3.3V on Pico, 
GND <----to----> GND on Pico, 
Signal <----to----> GP26 (ADC0, pin 31)


Soil moisture sensor:
VCC <----to----> 3.3V on Pico, 
GND <----to----> GND on Pico, 
Signal <----to----> GP27 (ADC1, pin 32)


In this [repository](https://github.com/iot-lnu/pico-w?tab=readme-ov-file) contains sensor code and network examples for pico-w. 


When everything is connected together it will look like this:
![put everything ](https://hackmd.io/_uploads/By3NacbvR.jpg)


## **Platform**
[Adafruit IO](https://io.adafruit.com/) was uses as the platform in this project.

Adafruit IO is free to use, but can be enhanced through payment and can be a great starting point for data visualization and MQTT connectivity, offering an easy-to-use platform that eliminates the need to set up your own broker and interface. The ability to access data remotely and create custom dashboards makes it convenient, especially for beginners.

However, Adafruit has limitations, such as restrictions on MQTT topics and message volume, as well as a lack of control over the broker configuration and data ownership. While suitable for initial testing, users may need to explore other solutions that provide more flexibility and control as their project requirements become more advanced.


## **The code**

The first step is to connect to the network. In this project, I connected it to Wi-Fi.

#### **Code to download**
For this code, you need to download the code for Wi-Fi connection from [github](https://github.com/iot-lnu/pico-w/blob/main/network-examples/N1_WiFi_Connection/boot.py)  and the umqttsimple library from [github](https://github.com/iot-lnu/pico-w/blob/main/network-examples/N2_WiFi_MQTT_Webhook_Adafruit/main.py).

In the [main](https://github.com/mariyaalnasrala/1DT305-IOT-plant-monitoring-system) file, you need to initialize two ADC (Analog-to-Digital Converter) objects for reading analog values from sensors connected to the respective GPIO (General-Purpose Input/Output) pins on the microcontroller. Use the MQTT protocol to connect to Adafruit IO and implement functions to collect and send data.

necessary libraries and configure the Adafruit IO connection:

```
import time
import keys
import ubinascii
import machine
from mqtt import MQTTClient
from machine import ADC, Pin

# Adafruit IO (AIO) configuration
AIO_SERVER = "io.adafruit.com"
AIO_PORT = 1883
AIO_USER = keys.AIO_USER
AIO_KEY = keys.AIO_KEY
AIO_CLIENT_ID = ubinascii.hexlify(machine.unique_id()).decode()
AIO_SOIL_FEED = keys.AIO_SOIL_FEED
AIO_LIGHTS_FEED = keys.AIO_LIGHTS_FEED
RANDOMS_INTERVAL = 900  # milliseconds
```

Setting up the network and MQTT client for connecting to Adafruit IO:
````
client = MQTTClient(AIO_CLIENT_ID, AIO_SERVER, AIO_PORT, AIO_USER, AIO_KEY)
client.connect()
client.subscribe(AIO_SOIL_FEED)
client.subscribe(AIO_LIGHTS_FEED)

def sub_cb(topic, msg):
    print((topic, msg))

client.set_callback(sub_cb)
````

## **Transmitting the data**

The data is transmitted to the Adafruit IO platform using the MQTT protocol over a WiFi connection. The data is sent every 15 minutes.

An MQTT client is configured with the Adafruit IO server details and credentials. The sensor data, including soil moisture and light intensity, is measured using analog-to-digital converter (ADC) objects.

The sensor readings are published to the corresponding Adafruit IO feeds using the MQTT client. A callback function is set up to handle any messages received from the Adafruit IO platform.

The main program loop checks for incoming MQTT messages and periodically transmits the sensor data, with a delay to avoid excessive network traffic.

The choice of WiFi provides a balance between range, data rate, and power consumption for this indoor/short-range application. MQTT was selected as the transport protocol for its efficiency and reliability in IoT scenarios.

## **Presenting the data**
To adapt the environment for different plants, we can set min and max values for soil moisture and sunlight. Each plant has specific needs for sunlight and soil moisture, and based on these we can change the values in the Adafruit code to show the correct values for each plant.

Some plants need many hours of sun per day, while others need less. With the data provided, you can check how many hours your plants have been in the sun and the soil moisture level.

For example, a succulent plant may need 6-8 hours of sunlight per day and a soil moisture level of 20-50%. An indoor plant may need 4-8 hours of sunlight and 40-70% soil moisture. By monitoring the values from your Adafruit setup, you can ensure your plants are getting the optimal environment they require.

The data presented on Adafruit IO dashboard.

Results for several plant varieties according to their needs from humidity and light.

![new data result](https://hackmd.io/_uploads/rJdMC3Gv0.png)


The value of soil moisture and light sensors, presented as a graph.

![sunlight graph new](https://hackmd.io/_uploads/ByKylaWw0.png)



## **Finalizing the design**

The final result is good and as wanted. The project went well, and it was interesting to create something from scratch and see the result in the end.

At the start of the course, I had wanted to create something more advanced than this, so I bought a temperature sensor, water pump, and a relay module. However, things didn't go as planned, and I couldn't make the project work as I had envisioned.

But now that I have finished the course, I want to work more on the project and connect the water pump to have the ability to turn it on and off when I want. I'm excited to continue improving and expanding the project now that I have a stronger foundational knowledge.

![result](https://hackmd.io/_uploads/HJzREvnLR.jpg)



