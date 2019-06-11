*** Settings ***
Documentation  test
Library  RequestsLibrary
Library  Collections
Library  ../Resources/getStagingIP_FF.py

*** Variables ***
${TEST_TARGET}=  www.samsung.com

*** Test Cases ***
Akamai Debug headers
    [Tags]    DEBUG
    ${edgeip}=  getedgeip  ${TEST_TARGET}
    Create session  sess01  https://${edgeip[0]}  disable_warnings=1
    ${headers}=  Create Dictionary  host=${TEST_TARGET}  Pragma=akamai-x-get-request-id,akamai-x-cache-on
    ${resp}=  Get Request  sess01  /  headers=${headers}
    Log  ${resp.headers}
    ${AkamaiDebugInfo_ReqInfo}=  get from dictionary  ${resp.headers}  X-Akamai-Request-ID
    ${AkamaiDebugInfo_CacheInfo}=  get from dictionary  ${resp.headers}  X-Cache
    Should not be empty  ${AkamaiDebugInfo_ReqInfo}  ${AkamaiDebugInfo_CacheInfo}

*** Keywords ***