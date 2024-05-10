ESP32 WiFi LED Control
This project demonstrates how to control an LED connected to an ESP32 board over WiFi using HTTP requests. It includes a Python script for the ESP32 and instructions for setting up a simple Kotlin Android app to interact with the ESP32.

Features
Connects to a specified WiFi network.
Initializes a simple HTTP server on the ESP32 board.
Controls an LED based on incoming HTTP requests (turning the LED on/off).
Requirements
ESP32 board with MicroPython firmware flashed.
Access to a WiFi network.
Kotlin IDE for Android app development (e.g., Android Studio).
Setup
Flash the MicroPython firmware to your ESP32 board.
Modify the Python script (esp32_led_control.py) to specify your WiFi network credentials.
Upload the Python script to your ESP32 board using a tool like ampy or Thonny IDE.
Open the Kotlin Android app project in Android Studio.
Modify the app code to specify the IP address of your ESP32 board.
Build and run the Android app on your device.
Usage
Ensure that both the ESP32 board and the Android device are connected to the same WiFi network.
Open the Android app on your device.
Use the app interface to send HTTP requests to control the LED on the ESP32 board.
License
This project is licensed under the MIT License.
