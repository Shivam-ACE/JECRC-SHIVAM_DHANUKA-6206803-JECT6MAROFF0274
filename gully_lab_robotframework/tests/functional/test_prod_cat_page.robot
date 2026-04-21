*** Settings ***
Resource  ../../resources/common_resources.robot
Resource  ../../resources/pages/prod_cat_page.robot

Suite Setup  Load Environment
Test Setup  Open Application
Test Teardown  Close Application

*** Test Cases ***
TC004
    [Documentation]  Add product to cart
    [Tags]  functional
    
    Search Product    sneakers
    Click Product
    Select Gender Male
    Select Size7
    Quantity Increase
    Add To Cart