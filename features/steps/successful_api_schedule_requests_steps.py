import json
from hamcrest import assert_that, equal_to
from behave import given, then

from features.steps.schedule import post_valid_schedule, get_valid_schedule
from features.utils import test_utils


@given('a Schedule Post with all inputted fields entered')
def a_valid_schedule_post_with_all_inputted_fields_entered(context):
    valid_schedule = post_valid_schedule()
    context.valid_schedule = valid_schedule
    context.json_request = json.dumps(valid_schedule, default=lambda x: x.__dict__)


@given('a Schedule Get with all inputted fields entered')
def a_valid_schedule_get_with_all_inputted_fields_entered(context):
    valid_schedule = get_valid_schedule()
    context.valid_schedule = valid_schedule
    context.json_request = json.dumps(valid_schedule, default=lambda x: x.__dict__)


@given('a Schedule Update with all inputted fields entered')
def a_valid_schedule_update_with_all_inputted_fields_entered(context):
    valid_schedule = post_valid_schedule()
    valid_schedule.opponent = "LSU"
    context.valid_schedule = valid_schedule
    context.json_request = json.dumps(valid_schedule, default=lambda x: x.__dict__)


@given('a Schedule Delete with inputted fields entered')
def a_schedule_delete_with_inputted_fields_entered(context):
    valid_schedule = get_valid_schedule()
    valid_schedule.gameId = "1234568"
    context.valid_schedule = valid_schedule
    context.json_request = json.dumps(valid_schedule, default=lambda x: x.__dict__)


@given('a valid Schedule post with the Date: {date}, '
       'Opponent Id: {opponent_id}, Opponent: {opponent}, '
       'Is Home: {is_home}, and Game Type {game_type}')
def step_impl(context, date, opponent_id, opponent, is_home, game_type):
    valid_schedule = post_valid_schedule()
    valid_schedule.date = date
    valid_schedule.opponentId = opponent_id
    valid_schedule.opponent = opponent
    valid_schedule.isHome = is_home
    valid_schedule.gameType = game_type
    context.valid_schedule = valid_schedule
    context.json_request = json.dumps(valid_schedule, default=lambda x: x.__dict__)


@given('a valid Schedule Get with all inputted fields entered')
def a_valid_schedule_get_with_all_inputted_fields_entered(context):
    valid_schedule = get_valid_schedule()
    context.valid_schedule = valid_schedule
    context.json_request = json.dumps(valid_schedule, default=lambda x: x.__dict__)


@then('a successful response of 200 Success will be returned')
def a_successful_response_of_200_accepted_will_be_returned(context):
    result = context.result
    assert_that(result.status_code, equal_to(200))


@then('all fields are entered into the database')
def all_fields_are_entered_into_the_database(context):
    global schedule
    schedule = schedule[0][4]
    query = "SELECT * FROM schedule_db WHERE schedule = \"{}\"" \
        .format(schedule)
    results = test_utils.fetch_all_rows(query)
    assert_that(results.__len__() == 1)
    opponent = str(results[0][3])
    assert_that('Test Opponent' == opponent)
    opponentId = str(results[0][4])
    assert_that('445' == opponentId)
    isHome = str(results[0][5])
    assert_that('True' == isHome)
    gameType = str(results[0][6])
    assert_that('0' == gameType)


@then('all fields Date: {date}, Opponent Id: {opponent_id}, '
      'Opponent: {opponent}, Is Home: {is_home}, '
      'and Game Type {game_type} to the database')
def step_impl(context, date, opponent_id, opponent, is_home, game_type):
    global schedule
    schedule = schedule[0][4]
    query = "SELECT * FROM schedule_db WHERE schedule = \"{}\"" \
        .format(schedule)
    results = test_utils.fetch_all_rows(query)
    assert_that(results.__len__() == 1)
    date = str(results[0][2])
    assert_that(date == date)
    opponent = str(results[0][3])
    assert_that(opponent == opponent)
    opponentId = str(results[0][4])
    assert_that(opponentId == opponent_id)
    isHome = str(results[0][5])
    assert_that(isHome == is_home)
    gameType = str(results[0][6])
    assert_that(gameType == game_type)


@then('the opponent field is updated in the database for the given schedule')
def the_opponent_field_is_updated_in_the_database_for_the_given_schedule(context):
    global schedule
    schedule = schedule[0][4]
    query = "SELECT * FROM schedule_db WHERE schedule = \"{}\"" \
        .format(schedule)
    results = test_utils.fetch_all_rows(query)
    assert_that(results.__len__() == 1)
    opponent = str(results[0][4])
    assert_that('LSU' == opponent)


@then('the schedule cannot be found in the database')
def the_schedule_cannot_be_found_in_the_database(context):
    global schedule
    query = "SELECT * FROM schedule_db WHERE schedule = '1234568'"
    results = test_utils.fetch_all_rows(query)
    assert_that(results.__len__() == 0)