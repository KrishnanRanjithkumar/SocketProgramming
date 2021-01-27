*** Settings ***
Library           ${EXECDIR}\\ServerSocket.py

*** Test Cases ***
TCPserver
    Connect to the server

*** Keywords ***
Connect to the server
    [Documentation]    Connect to the DB Server using given Host name, Port and Timeout
    start
