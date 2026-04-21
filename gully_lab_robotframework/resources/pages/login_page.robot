*** Settings ***
Library  SeleniumLibrary
Resource  ../../locators/login_page_locators.robot

*** Keywords ***
Login
    [Documentation]  Login user
    [Arguments]  ${email}  ${pwd}

    Input Text    ${EMAIL_FIELD}    ${email}

    Input Text    ${PASSWORD_FIELD}    ${pwd}

    Click Element    ${SIGN_IN_BTN}

    Page Should Not Contain    Incorrect email or password
    Page Should Contain    ACCOUNT
    Page Should Contain Link    xpath=//a[@href="/account/logout"]