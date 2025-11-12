import socket
import ssl
import sys
import time

MAIL_SERVER = "smtp.example.com"
MAIL_PORT = 587
SENDER = "user@example.com"
RECIPIENT = "friend@example.org"
SUBJECT = "Computer Networks Project: SMTP Simulation"
BODY = "This is a low-level simulation of the SMTP protocol using Python sockets to demonstrate command-response flow."

def receive_response(s):
    response = s.recv(4096).decode('ascii')
    print(f"\n[SERVER RESPONSE] {response.strip()}")
    if not response.startswith(('2', '3')):
        print("\n--- ERROR DETECTED ---")
        print(f"Server returned an error status code: {response[:3]}")
        sys.exit(1)
    return response

def send_command(s, command):
    print(f"\n[CLIENT COMMAND] {command.strip()}")
    s.sendall(command.encode('ascii'))

def simulate_smtp():
    print("--- 1. PROJECT: SMTP EMAIL SENDING SIMULATION ---")
    print(f"Connecting to {MAIL_SERVER}:{MAIL_PORT}...")

    try:
        client_socket = socket.create_connection((MAIL_SERVER, MAIL_PORT), timeout=10)
        
        context = ssl.create_default_context()
        secure_socket = context.wrap_socket(client_socket, server_hostname=MAIL_SERVER)
        
        print(f"Connection established (TCP Handshake complete).")

        receive_response(secure_socket)
        
        send_command(secure_socket, f"EHLO {MAIL_SERVER}\r\n")
        receive_response(secure_socket)
        
        send_command(secure_socket, f"MAIL FROM:<{SENDER}>\r\n")
        receive_response(secure_socket)
        
        send_command(secure_socket, f"RCPT TO:<{RECIPIENT}>\r\n")
        receive_response(secure_socket)

        send_command(secure_socket, "DATA\r\n")
        receive_response(secure_socket)
        
        message = (
            f"From: {SENDER}\r\n"
            f"To: {RECIPIENT}\r\n"
            f"Subject: {SUBJECT}\r\n"
            f"Date: {time.ctime(time.time())}\r\n"
            "\r\n"
            f"{BODY}\r\n"
        )
        print(f"\n[CLIENT SENDS MESSAGE CONTENT]\n{message.strip()}")
        send_command(secure_socket, message)
        
        send_command(secure_socket, ".\r\n")
        receive_response(secure_socket)
        
        send_command(secure_socket, "QUIT\r\n")
        receive_response(secure_socket)
        
        print("\n--- SIMULATION SUCCESSFUL ---")
        print("The SMTP command-response sequence was completed.")
        
    except socket.error as e:
        print(f"\n--- SOCKET ERROR ---")
        print(f"Could not connect or communicate with the server. Error: {e}")
        print("This is expected behavior for a simulation as we use a placeholder server. The command-response logic is demonstrated.")
        print("To run this for a real email, replace 'smtp.example.com' with a valid server (e.g., Gmail's smtp.gmail.com), but it will require full authentication.")
    except Exception as e:
        print(f"\n--- UNEXPECTED ERROR ---")
        print(f"An unexpected error occurred: {e}")
    finally:
        if 'client_socket' in locals():
            client_socket.close()

if _name_ == "_main_":
    simulate_smtp()