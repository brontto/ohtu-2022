*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Input New Command
    Input Credentials  jaska  pelkonentuutti
    Output Should Contain  New user registered


Register With Already Taken Username And Valid Password
    Create User  jaska  pelkonentuutti
    Input New Command
    Input Credentials  jaska  kallesaatana


Register With Too Short Username And Valid Password
    Input New Command
    Input Credentials  ja  pelkonentuutti
    Output Should Contain  Username is too short


Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  jaska  pelkon
    Output Should Contain  Password is too short


Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  jaska  pelkonentuutti
    Output Should Contain  New user registered

