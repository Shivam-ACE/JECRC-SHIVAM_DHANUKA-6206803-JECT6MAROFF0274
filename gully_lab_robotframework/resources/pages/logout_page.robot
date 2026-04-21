*** Settings ***
Library  SeleniumLibrary
Resource  ../../locators/logout_page_locators.robot

*** Keywords ***
Logout
    [Documentation]  Logout user

    Page Should Contain    Log out

    Click Element    ${logout_btn}