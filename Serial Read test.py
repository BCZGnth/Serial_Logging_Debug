#This code is Ai except for a little of Raj's work

import serial
from time import sleep

# Serial Configuration
serial_port = "COM5"  # Replace with the appropriate serial port
baud_rate = 9615

# Create a serial connection
ser = serial.Serial(serial_port, baud_rate, timeout=1)

def send_command(command):
    ser.write(command)

def read_data():
    #print(ser)
    return ser.readline().decode()

def is_keyboard_interrupt():
    if KeyboardInterrupt:
        return True
    return False
        
if __name__ == "__main__":
    reading = True
    n = 0

    try:
        with open(f"log{n}.txt", "w") as logfile:
            while True:
                try:
                    # Example: Sending a command to the ToF module
                    # send_command(b"\x55\xAA\x81\x00\xFA")
                    # Reading and printing the received data

                    data = read_data()

                    if not data: continue
                    print(data)

                    logfile.write(data + "\n")

                    # Optional: Pause for a moment
                    # sleep(.001)

                except UnicodeDecodeError:
                    continue

    except KeyboardInterrupt:
        # Close the serial connection when the script is interrupted with "ctrl+c"
        ser.close()
        print("Serial connection closed.")