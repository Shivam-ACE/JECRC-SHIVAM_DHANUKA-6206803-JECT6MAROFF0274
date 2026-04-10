*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://sauce-demo.myshopify.com/account/login

*** Test Cases ***
Login
    Open Browser    ${url}  chrome
    Sleep    2s
#    Login Success    cheeseburger@gmail.com
    Login Success    pwd=hiii  email=cheeseburger@gmail.com
    Sleep    2s


*** Keywords ***
Login Success
    [Arguments]    ${email}  ${pwd}=iamironman
    Input Text    id=customer_email  ${email}
    Input Text    id=customer_password  ${pwd}