*** Settings ***
Library           WebSocketClient

*** Test Cases ***
Echo
    ${my_websocket}=    WebSocketClient.Connect    localhost:3443
    WebSocketClient.Send    ${my_websocket}    Hello
    ${result}=    WebSocketClient.Recv    ${my_websocket}
    Should Be Equal    Hello    olleH
    WebSocketClient.Close    ${my_websocket}
