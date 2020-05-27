# Import(s)

from os import getenv

from teslajson import Connection

# Constant(s)

LIST_VEHICLES_ACTION = 'LIST_VEHICLES'
SUPPORTED_TESLA_ACTIONS = {LIST_VEHICLES_ACTION}

# Input validation

TESLA_EMAIL = getenv('TESLA_EMAIL')
assert TESLA_EMAIL

TESLA_PASSWORD = getenv('TESLA_PASSWORD')
assert TESLA_PASSWORD

TESLA_ACTION = getenv('TESLA_ACTION') or LIST_VEHICLES_ACTION
assert TESLA_ACTION in SUPPORTED_TESLA_ACTIONS

# Action processing

connection = Connection(TESLA_EMAIL, TESLA_PASSWORD)
if TESLA_ACTION == LIST_VEHICLES_ACTION:
    print(connection.vehicles or 'No vehicles found :*(')
