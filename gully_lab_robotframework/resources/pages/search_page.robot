*** Settings ***
Library  SeleniumLibrary
Resource  ../../locators/search_page_locators.robot
Resource    ../../locators/home_page_locators.robot

*** Keywords ***
search prod
    [Documentation]  To search a product
    
    [Arguments]    ${prod}
    
    Click Element    ${SEARCH}

    Input Text    ${search_text_field}  ${prod}
    Press Keys    ${search_text_field}  ENTER
    Sleep    1s
    Page Should Not Contain    No results