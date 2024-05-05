import threading

from vidstream import StreamingServer

receiver = StreamingServer('192.168.1.38', 9999)  # Your IP address (currently local)
t = threading.Thread(target=receiver.start_server)
t.start()

print('Server is online now!')
while input('') != 'STOP':
    try:
        command = input("Type 'STOP' to stop the server: ")
        if command == 'STOP':
            receiver.stop_server()
            break  # Exit the loop when 'STOP' command is received
    except OSError and ConnectionResetError as e:
        print('Error', e)
print('Server is offline!')

receiver.stop_server()
