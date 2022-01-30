*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command

*** Test Cases ***
Login With Correct Credentials
    Input Credentials  kalle  kallemannisto
    Output Should Contain  Logged in


Login With Incorrect Password
    Input Credentials  kalle  vaarapassu
    Output Should Contain  Invalid username or password


Login With Nonexistent Username
    Input Credentials  kallu  kalletalonen
    Output Should Contain  Invalid username or password


*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kallemannisto
    Input Login Command
