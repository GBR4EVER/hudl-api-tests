Feature: Unsuccessful API Schedule Requests

  Scenario: Unsuccessful Schedule Posting of inputted fields
    Given a Schedule Post with inputted fields entered
    When I call to post to the API
    Then a unsuccessful response of 400 Bad Request will be returned

  Scenario Outline: Unsuccessful Schedule Posting
    Given a Schedule post with the Date: <date>, Opponent Id: <opponent id>, Opponent: <opponent>, Is Home: <is home>, and Game Type <game type>
    When I call to post to the API
    Then a unsuccessful response of 400 Bad Request will be returned

    Examples:
    | date | opponent id | opponent | is home | game type |
    | 2022-01-01T19:00:00 | abc | @#$% | yes | reg |
    | 2019-01T19:00:00 | xyz | null | no | practice |

  Scenario: Unsuccessful Schedule Get with all inputted fields
    Given a Schedule Get with all inputted fields entered
    When I call to get from the API
    Then a unsuccessful response of 404 Not Found will be returned

  Scenario: Unsuccessful Schedule Update with all inputted fields
    Given a Schedule update with inputted fields entered
    When I call to update to the API
    Then a unsuccessful response of 400 Bad Request will be returned

  Scenario: Unsuccessful Schedule Delete with all inputted fields
    Given a Schedule delete with inputted fields entered
    When I call to delete to the API
    Then a unsuccessful response of 400 Bad Request will be returned