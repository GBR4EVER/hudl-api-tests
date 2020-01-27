import json
from hamcrest import assert_that, equal_to
from behave import given, then

from features.steps.schedule import get_valid_schedule, post_valid_schedule


@given('a Schedule Post with inputted fields entered')
def a_schedule_post_with_inputted_fields_entered(context):
    schedule = post_valid_schedule()
    schedule.opponent = ""
    context.valid_schedule = schedule
    context.json_request = dump_schedule_json(schedule)


@given('a Schedule Get with all inputted fields entered')
def a_schedule_get_with_all_inputted_fields_entered(context):
    schedule = get_valid_schedule()
    schedule.gameId = ""
    context.valid_schedule = schedule
    context.json_request = dump_schedule_json()


@given('a Schedule Update with inputted fields entered')
def a_schedule_post_with_inputted_fields_entered(context):
    schedule = post_valid_schedule()
    schedule.opponent = ""
    context.valid_schedule = schedule
    context.json_request = dump_schedule_json(schedule)

@given('a Schedule update with inputted fields entered')
def a_schedule_update_with_inputted_fields_entered(context):
    schedule = post_valid_schedule()
    schedule.gameId = None
    context.valid_schedule = schedule
    context.json_request = dump_schedule_json(schedule)


@given('a Schedule delete with inputted fields entered')
def a_schedule_delete_with_inputted_fields_entered(context):
    schedule = post_valid_schedule()
    schedule.opponentId = "~1234"
    context.valid_schedule = schedule
    context.json_reuest = dump_schedule_json(schedule)


@given('a Schedule post with the Date: {date}, '
       'Opponent Id: {opponent_id}, Opponent: {opponent}, '
       'Is Home: {is_home}, and Game Type {game_type}')
def step_impl(context, date, opponent_id, opponent, is_home, game_type):
    schedule = post_valid_schedule()
    if opponent == 'null':
        schedule.opponent = None
    else:
        schedule.opponent = opponent
    schedule.date = date
    schedule.opponentId = opponent_id
    schedule.opponent = opponent
    schedule.isHome = is_home
    schedule.gameType = game_type
    context.valid_schedule = schedule
    context.json_request = dump_schedule_json(schedule)


@then('a unsuccessful response of 400 Bad Request will be returned')
def a_unsuccessful_response_of_400_bad_request_will_be_returned(context):
    result = context.result
    assert_that(result.status_code, equal_to(400))


@then('a unsuccessful response of 404 Not Found will be returned')
def a_unsuccessful_response_of_404_not_found_will_be_returned(context):
    result = context.result
    assert_that(result.status_code, equal_to(404))


def dump_schedule_json(schedule):
    return json.dumps(schedule, default=lambda x: x.__dict__)
