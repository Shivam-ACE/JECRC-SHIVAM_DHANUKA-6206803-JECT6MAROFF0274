*** Settings ***
Resource  ../../resources/pages/search_page.robot
Resource  ../../resources/common_resources.robot

Suite Setup  Load Environment
Test Setup  Open Application
Test Teardown  Close Application

*** Test Cases ***
TC003
    [Documentation]  Search product
    [Tags]  functional

    Search Prod    sneakers