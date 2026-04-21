*** Settings ***
Library  SeleniumLibrary
Resource  ../../locators/home_page_locators.robot

*** Keywords ***
ACCOUNT
    [Documentation]  Opens account info
    Click Element    ${ACCOUNT}

Search
    [Documentation]  Opens search bar
    Click Element    ${SEARCH}
