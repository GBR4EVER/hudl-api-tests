Feature: Successful API Schedule Requests

  Scenario: Successful Schedule Post of all inputted fields
    Given a valid Schedule Post with all inputted fields entered
    When I call to post to the API
    Then a successful response of 200 Success will be returned
    Then all fields are entered into the database

  Scenario Outline: Successful Schedule Posting
    Given a valid Schedule post with the Date: <date>, Opponent Id: <opponent id>, Opponent: <opponent>, Is Home: <is home>, and Game Type <game type>
    When I call to post to the API
    Then a successful response of 200 Success will be returned
    Then all fields Date: <date>, Opponent Id: <opponent id>, Opponent: <opponent>, Is Home: <is home>, and Game Type <game type> to the database

    Examples:
    | date | opponent id | opponent | is home | game type |
    | 2020-01-01T19:00:00 | 12 | Iowa | False | 1 |
    | 2019-01-01T19:00:00 | 77 | Oklahoma | True | 0 |

  Scenario: Successful Schedule Get with all inputted fields
    Given a valid Schedule Get with all inputted fields entered
    When I call to get from the API
    Then A successful response of 200 Success will be returned

  Scenario: Successful Schedule Update with all inputted fields
    Given a Schedule Update with opponent entered
    When I call to update to the API
    Then a successful response of 200 Success will be returned
    Then the opponent field is updated in the database for the given schedule

  Scenario: Successful Schedule Delete with all inputted fields
    Given a Schedule Delete with inputted fields entered
    When I call to delete to the API
    Then a Successful response of 200 Success will be returned
    Then the schedule cannot be found in the database