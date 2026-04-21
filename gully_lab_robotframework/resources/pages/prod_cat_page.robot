*** Settings ***
Library  SeleniumLibrary
Resource    ../../locators/prod_cat_page_locators.robot
Resource    ../../resources/pages/search_page.robot

*** Keywords ***
search product
    [Arguments]    ${prod}
    Search Prod    ${prod}
click product
    Click Element    ${PRODUCT}
select size7
    Click Element    ${SIZE_7}
select gender male
    ${class}=    Get Element Attribute    ${GENDER_MALE}    class
    IF    'gender-btn' == '${class}'
        Click Element    ${GENDER_MALE}
    ELSE
        No Operation
    END
quantity increase
    Click Element    ${QUANTITY_INC}
quantity decrease
    Click Element    ${QUANTITY_DEC}
add to cart
    Wait Until Element Is Visible    ${ADD_TO_CART}  10s
    Click Element    ${ADD_TO_CART}
    Sleep    5s

    
    
