from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.io import CheckiOReferee

from tests import TESTS
#import difflib

#def checker(right_result, user_result):
#    d = difflib.Differ()
#    return right_result == user_result, "".join(d.compare(right_result, user_result))

api.add_listener(
    ON_CONNECT,
    CheckiOReferee(tests=TESTS).on_ready)
