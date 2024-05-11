# ESP32 WiFi LED Control

This project demonstrates how to control an LED connected to an ESP32 board over WiFi using HTTP requests. It includes a Python script for the ESP32 and instructions for setting up a simple Kotlin Android app to interact with the ESP32.

## Related
- [Kotlin Simple Client for ESP32]([https://github.com/Cabzla/ESP32-Simple-Com-for-Android](https://github.com/Cabzla/AndroidClientESP32)): Counterpart ESP32 project for this ESP32 Code.

## Features

- Connects to a specified WiFi network.
- Initializes a simple HTTP server on the ESP32 board.
- Controls an LED based on incoming HTTP requests (turning the LED on/off).

## Requirements

- ESP32 board with MicroPython firmware flashed.
- Access to a WiFi network.
- Kotlin IDE for Android app development (e.g., Android Studio).

## Setup

1. Flash the MicroPython firmware to your ESP32 board.
2. Modify the Python script to specify your WiFi network credentials.
3. Upload the Python script to your ESP32 board using a tool like `ampy` or Thonny IDE.
4. Open the Kotlin Android app project in Android Studio.
5. Modify the app code to specify the IP address of your ESP32 board.
6. Build and run the Android app on your device.

## Usage

1. Ensure that both the ESP32 board and the Android device are connected to the same WiFi network.
2. Open the Android app on your device.
3. Use the app interface to send HTTP requests to control the LED on the ESP32 board.

## License

This project is licensed under the [MIT License](LICENSE).
