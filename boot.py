"""
Project: ESP32 WiFi LED Control
Author: Cabzla

This script establishes a connection to a WiFi network, initializes a simple HTTP server on an ESP32 board,
and controls an LED based on incoming requests.

Functions:
- connect_wifi(ssid, password): Establishes a connection to the specified WiFi network.
- led_on(): Turns the LED on.
- led_off(): Turns the LED off.
"""

import socket
import network
import machine

def connect_wifi(ssid, password):
    """
    Connects to the specified WiFi network.

    Args:
    - ssid (str): The SSID of the WiFi network.
    - password (str): The password of the WiFi network.

    Returns:
    None
    """
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('Connecting to the WiFi network...')
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print('Connected:', sta_if.ifconfig())

# LED initialization
led_pin = 12  # Pin for the LED (change if necessary)
led = machine.Pin(led_pin, machine.Pin.OUT)

# WiFi credentials
ssid = 'YOUR_SSID'
password = 'YOUR_PASSWORD'
connect_wifi(ssid, password)

# Server initialization
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 80))
server.listen(1)

print('Waiting for connection...')

while True:
    conn, addr = server.accept()
    print('Connected to', addr)
    request = conn.recv(1024)
    print('Request:', request)

    if b'/on' in request:
        print('Turning the LED on')
        led.on()
    elif b'/off' in request:
        print('Turning the LED off')
        led.off()

    response = 'HTTP/1.1 200 OK\nContent-Type: text/html\n\n'
    conn.send(response)
    conn.close()
