#!/usr/bin/env python3

from public.main import app
from sonja.config import connect_to_database, log_config
from sonja.database import create_initial_user, create_initial_ecosystem, create_initial_configuration
from sonja.demo import populate_initial_data

import os
import uvicorn

initial_user = os.environ.get('SONJA_INITIAL_USER', 'user')
initial_password = os.environ.get('SONJA_INITIAL_PASSWORD', 'password')
initial_ecosystem = os.environ.get('SONJA_INITIAL_ECOSYSTEM', 'MyEcosystem')


def setup_initial_data():
    create_initial_configuration()
    create_initial_user(initial_user, initial_password)

    if initial_ecosystem:
        ecosystem_id = create_initial_ecosystem(initial_ecosystem)
        if ecosystem_id:
            populate_initial_data(ecosystem_id)


if __name__ == '__main__':
    connect_to_database()
    setup_initial_data()
    uvicorn.run(app, host="0.0.0.0", port=8080, log_config=log_config)
