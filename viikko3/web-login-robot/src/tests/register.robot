*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Register Username  kalletius
    Register Password  kallemanni
    Register Confirmation Password  kallemanni
    Submit Register Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Register Username  ka
    Register Password  passutius
    Register Confirmation Password  passutius
    Submit Register Credentials
    Register Should Fail With Message  Username is too short

Register With Valid Username And Too Short password
    Register Username  kalletius
    Register Password  pass
    Register Confirmation Password  pass
    Submit Register Credentials
    Register Should Fail With Message  Password is too short


Register With Nonmatching Password And Password Confirmation
    Register Username  kalletius
    Register Password  passkalle
    Register Confirmation Password  passkeri
    Submit Register Credentials
    Register Should Fail With Message  Password and Confirmation does not match
    

Login After Successful Registration
    Register Username  kaputius
    Register Password  kalkkunamaakari
    Register Confirmation Password  kalkkunamaakari
    Submit Register Credentials
    Register Should Succeed
    Go To Login Page
    Set Username  kaputius
    Set Password  kalkkunamaakari
    Submit Credentials
    Login Should Succeed



Login After Failed Registration
    Register Username  kaputius
    Register Password  kalki
    Register Confirmation Password  kalki
    Submit Register Credentials
    Go To Login Page
    Set Username  kaputius
    Set Password  kalki
    Submit Credentials
    Login Should Fail With Message  Invalid username or password


