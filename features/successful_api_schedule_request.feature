Feature: Successful API Schedule Requests

  Scenario: Successful Schedule Posting of all inputted fields
    Given a valid Schedule Post with all inputted fields entered
    When I post to the API
    Then a successful response of 200 Success will be returned
    Then all fields are entered into the database

  Scenario Outline: Successful Schedule Posting
    Given a valid Schedule post with the Date: <date>, Opponent Id: <opponent id>, Opponent: <opponent>, Is Home: <is home>, and Game Type <game type>
    When I post to the API
    Then a successful response of 200 Success will be returned
    Then all fields Date: <date>, Opponent Id: <opponent id>, Opponent: <opponent>, Is Home: <is home>, and Game Type <game type> to the database

    Examples:
    | date | opponent id | opponent | is home | game type |
    | 2020-01-01T19:00:00 | 12 | iowa | False | 1 |
    | 2019-01-01T19:00:00 | 77 | oklahoma | True | 0 |