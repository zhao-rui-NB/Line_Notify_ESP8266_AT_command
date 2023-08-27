import serial
import time
import os
#cls to clear screen
os.system('cls')

# Configure the serial port
ser = serial.Serial('COM3', 115200, timeout=1)  # Replace 'COMx' with your serial port
try:
    ser.close()
except:
    pass

# Function to send and receive AT commands
def send_at_command(command, delay=5):
    ser.write(command.encode())

    #wait intil find 'ok' or 'error' IF TIMEOUT RETURN
    start_time = time.time()

    response = ''
    while 'OK' not in response and 'ERROR' not in response:
        try:
            response += ser.read_all().decode()
        except:
            pass
        if time.time() - start_time > delay:
            print("---ERR , at timeout---")
            break
    time.sleep(.5)
    response += ser.read_all().decode()
    return response

# Open the serial port
ser.open()

if ser.is_open:
    print("Serial port is open. Sending AT commands...")

    response = send_at_command("AT\r\n")
    print("\n\tAT response:", response)

    response = send_at_command('''AT+CWJAP="DSL-6740C-849","12345678"\r\n''')
    print("\n\tAT response:", response)

    response = send_at_command('''AT+CIPSTART="SSL","notify-api.line.me",443\r\n''')
    print("\n\tAT response:", response)
#message=終於成功了老哥123

    msg = '終於成功了老哥真棒'
    len_msg = len(msg.encode())

    #post request for line notify api
    post = f'''\
POST /api/notify HTTP/1.1\r\n\
Host: notify-api.line.me\r\n\
Authorization: Bearer lKxdwgslXOi7fIN2tVhNeYG5HIBGvqIQk9G136pA4az\r\n\
Content-Type: application/x-www-form-urlencoded\r\n\
Content-Length: {len_msg+8}\r\n\r\n\
message={msg}\
'''
    print('+++++++++++++',len_msg)
    response = send_at_command(f'''AT+CIPSEND={str(len(post.encode()))}\r\n''')
    print("\n\tAT response:", response)

    response = send_at_command(post)
    print("\n\tAT response:", response)





    ser.close()
    print("Serial port is closed.")

else:
    print("Failed to open the serial port.")