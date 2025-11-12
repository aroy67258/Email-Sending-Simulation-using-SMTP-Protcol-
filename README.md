# Low-Level SMTP Email Sending Simulation

This project is a simple, low-level simulation of the **SMTP (Simple Mail Transfer Protocol)** used for sending email. It is built using Python's `socket` and `ssl` libraries to demonstrate the raw command-and-response flow between an email client and a mail server.

## Purpose

The primary goal of this script is **educational**. It is designed to show the fundamental SMTP commands (like `EHLO`, `MAIL FROM`, `RCPT TO`, `DATA`) that are used in the background every time you send an email. It is **not** a fully-functional email client, but a simulation of the protocol's logic.

## How It Works

The script follows the standard SMTP communication sequence:

1.  **Establish Connection:** A TCP connection is established with the mail server (e.g., `smtp.example.com`) on port 587 (the standard submission port).
2.  **Secure the Connection:** The script initiates a secure connection using `ssl` (simulating the `STARTTLS` command) because modern mail servers require encryption.
3.  **Server Greeting:** The server sends a "220" greeting to indicate it's ready.
4.  **Client Handshake (EHLO):** The client introduces itself using the `EHLO` (Extended Hello) command.
5.  **Identify Sender:** The client specifies the sender's address using the `MAIL FROM:` command.
6.  **Identify Recipient:** The client specifies the recipient's address using the `RCPT TO:` command.
7.  **Initiate Data Transfer:** The client sends the `DATA` command to signal it's ready to send the email's content.
8.  **Send Message Content:** The client sends the email headers (e.g., `From`, `To`, `Subject`) and the `Body`, separated by a blank line.
9.  **End Data Transfer:** The client sends a single period (`.`) on a new line to signify the end of the message data.
10. **Quit Connection:** The client sends the `QUIT` command to terminate the session, and the server closes the connection.

## How to Run

1.  Ensure you have Python 3 installed.
2.  Save the code as `EmailSendingSimulationSMTPProtocol.py`.
3.  Run the script from your terminal:

    ```sh
    python EmailSendingSimulationSMTPProtocol.py
    ```

You will see the [CLIENT COMMAND] and [SERVER RESPONSE] printed to the console, showing the step-by-step conversation.

## Important Note: This is a Simulation

This script uses placeholder values (e.g., `smtp.example.com`, `user@example.com`). It is **intentionally designed to fail** the connection (`socket.error`) because it is not authenticating with a real mail server.

To connect to a real-world mail server (like `smtp.gmail.com`), you would need to implement:
* **Authentication:** Sending username and password credentials (e.g., using `AUTH LOGIN` and base64 encoding).
* **App Passwords:** Services like Gmail require generating an "App Password" for low-level scripts like this, as they block simple password logins for security reasons.

This script omits authentication to keep the focus purely on the **SMTP protocol commands**.

## Technologies Used

* **Python**
* **`socket`:** For low-level network connections.

## Team Members
1. Ankit Kumar (Roll No: 2023021110)
2. Anupam Kumar (Roll No: 2023021116)
3. Adil Mustaq (Roll No: 2023021102
* **`ssl`:** For creating a secure (SSL/TLS) socket wrapper.
* **`sys`:** For error handling and exiting.
* **`time`:** For generating the `Date` header in the email.
