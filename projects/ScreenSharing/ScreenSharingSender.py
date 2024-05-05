import threading

from vidstream import ScreenShareClient

sender = ScreenShareClient('192.168.1.38', 9999)  # IP address of the server
t = threading.Thread(target=sender.start_stream)
t.start()

print('Connection is successful!')
while input('') != 'STOP':
    try:
        command = input("Type 'STOP' to disconnect: ")
        if command == 'STOP':
            sender.stop_stream()
            break  # # Exit the loop when 'STOP' command is received
    except ConnectionRefusedError as e:
        print('Error', e)
print("You're disconnected!")

sender.stop_stream()
