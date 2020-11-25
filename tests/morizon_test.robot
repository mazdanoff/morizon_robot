*** Settings ***
Documentation     One test case using MorizonLibrary and Gherkin syntax.
Library           libraries.MorizonLibrary    ${BROWSER}


*** Variables ***
${SERVER}         morizon.pl
${HOME_URL}       https://${SERVER}/
${WROCLAW_URL}    https://${SERVER}/nieruchomosci/wroclaw/
${BROWSER}        Chrome
${LOCATION}       Wrocław
${MIN_VALUE}      ${200000}
${MAX_VALUE}      ${250000}

*** Test Cases ***

Morizon Search Results

    Given Morizon Main Page is Opened
    When User sets search criteria
    And User picks the first search result
    Then Price is matching the bracket criteria

*** Keywords ***
Morizon Main Page is Opened
    Open Main Page      ${HOME_URL}

User sets search criteria
    Set Location        ${LOCATION}
    Set Minimum Value   ${MIN_VALUE}
    Set Maximum Value   ${MAX_VALUE}
    Click Search Button

User picks the first search result
    Click First Result

Price is matching the bracket criteria
    Price Is Within Set Brackets    ${MIN_VALUE}    ${MAX_VALUE}