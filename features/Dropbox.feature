Feature: DropboxAPI

    Scenario: Valid request
    Given dropbox url "https://content.dropboxapi.com/2/files/upload"
    And we want to upload file "/features/lib/img/nebo.jpg" to dropbox with path "/webApi/nebo.jpg"
    When we consume the endpoint
    Then json response is retrieved with right data and 200 as status code

    Scenario: Request existing file
    Given dropbox url "https://api.dropboxapi.com/2/sharing/get_file_metadata"
    And we want to request file "nebo.jpg" from directory "/webApi/"
    When we consume the endpoint
    Then json response is retrieved with right data and 200 as status code

    Scenario: Requesting existing file
    Given dropbox url "https://api.dropboxapi.com/2/files/delete_v2"
    And we want to delete file "/webApi/nebo.jpg"
    When we consume the endpoint
    Then json response is retrieved with right data and 200 as status code
