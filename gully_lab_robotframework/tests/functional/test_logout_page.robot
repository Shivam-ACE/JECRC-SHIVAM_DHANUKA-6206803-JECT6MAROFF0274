*** Settings ***
Resource  ../../resources/pages/home_page.robot
Resource  ../../resources/pages/logout_page.robot
Resource  ../../resources/common_resources.robot
Resource    ../../resources/pages/login_page.robot

Suite Setup  Load Environment
Test Setup  Open Application
Test Teardown  Close Application

*** Test Cases ***
TC002
    [Documentation]  Logout functionality
    [Tags]  functional

    ACCOUNT
    
    Login    ${USER_EMAIL}  ${USER_PWD}
    
    Logout