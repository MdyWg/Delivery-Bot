import serial


def parse_encoder_line(line):
    # firmware format: "CCR1,CCR2,left_count,right_count,left_speed,right_speed"
    parts = line.split(',')
    if len(parts) == 6:
        try:
            ccr1, ccr2 = int(parts[0]), int(parts[1])
            left_count, right_count = int(parts[2]), int(parts[3])
            left_speed, right_speed = int(parts[4]), int(parts[5])
            return [ccr1, ccr2, left_count, right_count, left_speed, right_speed]
        except ValueError:
            print(f'Could not parse encoder line: {line}')
    return None


ser = serial.Serial('/dev/ttyAMA0', baudrate=115200, timeout=1)
while True:
    line = ser.readline().decode('utf-8', errors='ignore').strip()
    if line:
        print(f"Received: {line}")
        parse_encoder_line(line)
