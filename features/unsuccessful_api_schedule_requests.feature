Feature: Unsuccessful API Schedule Requests

  Scenario: Unsuccessful Schedule Posting of inputted fields
    Given a Schedule Post with all inputted fields entered
    When I post to the API
    Then a unsuccessful response of 400 Bad Request will be returned

  Scenario Outline: Unsuccessful Schedule Posting
    Given a Schedule post with the Date: <date>, Opponent Id: <opponent id>, Opponent: <opponent>, Is Home: <is home>, and Game Type <game type>
    When I post to the API
    Then a unsuccessful response of 400 Bad Request will be returned

    Examples:
    | date | opponent id | opponent | is home | game type |
    | 2022-01-01T19:00:00 | abc | @#$% | yes | reg |
    | 2019-01T19:00:00 | xyz | null | no | practice |