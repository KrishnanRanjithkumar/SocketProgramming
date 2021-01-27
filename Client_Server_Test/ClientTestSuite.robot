*** Settings ***
Library           C:\\Users\\Ranjith\\Desktop\\New folder\\ClientSocket.py

*** Test Cases ***
StartClient
    Send Message to the server

*** Keywords ***
Send Message to the server
    send    "hello"
    receive
