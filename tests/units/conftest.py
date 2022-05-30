import pytest

import server
from tests.units.mocks import mock_loadCompetitions, mock_loadClubs


@pytest.fixture
def client():
    server.app.config['TESTING'] = True
    client = server.app.test_client()
    yield client


@pytest.fixture
def mock_competitions_and_clubs(mocker):
    mocker.patch.object(server, 'competitions', mock_loadCompetitions())
    mocker.patch.object(server, 'clubs', mock_loadClubs())
