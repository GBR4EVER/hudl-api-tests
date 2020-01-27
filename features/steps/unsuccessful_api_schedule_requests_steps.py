import json
from hamcrest import assert_that, equal_to
from behave import given, then

from features.steps.schedule import get_valid_schedule


@given('a Schedule Post with all inputted fields entered')
def a_valid_schedule_post_with_all_inputted_fields_entered(context):
    schedule = get_valid_schedule()
    context.valid_schedule = schedule
    context.json_request = get_schedule_json(schedule)


@given('a Schedule post with the Date: {date}, '
       'Opponent Id: {opponent_id}, Opponent: {opponent}, '
       'Is Home: {is_home}, and Game Type {game_type}')
def step_impl(context, date, opponent_id, opponent, is_home, game_type):
    schedule = get_valid_schedule()
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
    context.json_request = get_schedule_json(schedule)


@then('a unsuccessful response of 400 Bad Request will be returned')
def a_successful_response_of_200_accepted_will_be_returned(context):
    result = context.result
    assert_that(result.status_code, equal_to(400))


def get_schedule_json(schedule):
    return json.dumps(schedule, default=lambda x: x.__dict__)
