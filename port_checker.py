import socket

def check_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)

        result = sock.connect_ex((host, port))

        if result == 0:
            print(f"Port {port} is OPEN on {host}")
        else:
            print(f"Port {port} is CLOSED on {host}")

        sock.close()

    except socket.gaierror:
        print("Invalid hostname or IP address.")

    except socket.error:
        print("Unable to connect to the server.")

    except ValueError:
        print("Please enter a valid port number.")

    except Exception as e:
        print(f"Error: {e}")


print("========== PORT STATUS CHECKER ==========")

host = input("Enter target IP address or website: ")

try:
    port = int(input("Enter port number: "))

    if port < 0 or port > 65535:
        print("Port number must be between 0 and 65535.")
    else:
        check_port(host, port)

except ValueError:
    print("Port number must be an integer.")

print("Program Finished.")