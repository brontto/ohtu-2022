*** Settings ***
Resource  resource.robot
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
    

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Register Credentials
    Click Button  Register

Register Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Register Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Register Confirmation Password
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}