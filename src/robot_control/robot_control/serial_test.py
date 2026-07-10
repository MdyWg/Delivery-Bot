import serial 
import time

ser = serial.Serial('/dev/ttyAMA0', baudrate=115200, timeout=1)
while True: 
    line = ser.readline().decode('utf-8', errors='ignore').strip()
    if line:
        print(f"Received: {line}")
        parse_encoder_line(line)

def parse_encoder_line(line):
    parts = line.split()
    if len(parts) == 5 and parts[0] == 'E':
        try:
            fl, fr, rl, rr = float(parts[1]), float(parts[2]), \
                             float(parts[3]), float(parts[4])
            return [fl, fr, rl, rr]
        except ValueError:
            print(f'Could not parse encoder line: {line}')
    return None
# time.sleep(1)

# ser.write(b"STOP\n")
# print("Sent STOP")