import datetime

from server import POINTS_FOR_A_PLACE, MAX_PLACES_PER_COMPETITION


class TestLoginClass:
    def test_login_email_known(self, client, mock_competitions_and_clubs):
        response = client.post('/showSummary', data={"email": "test@club.com"})
        assert response.status_code == 200
        assert f"Welcome, " in response.data.decode()

    def test_login_email_unknown(self, client, mock_competitions_and_clubs):
        response = client.post('/showSummary', data={"email": "unkown@email.com"})
        assert response.status_code == 200
        assert "Sorry, that email wasn&#39;t found." in response.data.decode()


class TestPurchaseClass:
    def test_purchase_places(self, client, mock_competitions_and_clubs):
        expected_club_value = 13 - (2 * POINTS_FOR_A_PLACE)
        expected_competition_value = 25 - 2
        input_value = {'club': 'Test Club',
                       'competition': 'Spring Festival',
                       'places': 2
                       }
        response = client.post('/purchasePlaces', data=input_value)
        assert response.status_code == 200
        assert "Great-booking complete" in response.data.decode()
        assert f"Points available: {expected_club_value}"
        assert f"Number of Places: {expected_competition_value} Book Places"

    def test_purchase_more_than_the_points(self, client, mock_competitions_and_clubs):
        response = client.post('/purchasePlaces', data={'club': 'Last Test Club',
                                                        'competition': 'Spring Festival',
                                                        'places': 5
                                                        }
                               )
        assert response.status_code == 200
        assert "cannot book" in response.data.decode()

    def test_purchase_more_than_twelve_places(self, client, mock_competitions_and_clubs):
        input_value = {'club': 'Second Test Club',
                       'competition': 'Spring Festival',
                       'places': 13
                       }
        response = client.post('/purchasePlaces', data=input_value)
        assert response.status_code == 200
        assert f"You cannot book more than {MAX_PLACES_PER_COMPETITION} places per competition" in response.data.decode()

    def test_purchase_more_places_than_available_in_competition(self, client, mock_competitions_and_clubs):
        input_value = {'club': 'Second Test Club',
                       'competition': 'Little Competition',
                       'places': 5
                       }
        response = client.post('/purchasePlaces', data=input_value)
        assert response.status_code == 200
        assert f"You cannot reserve more places than are available in the competition" in response.data.decode()

    def test_purchase_places_for_a_past_competition(self, client, mock_competitions_and_clubs):
        input_value = {'club': 'Second Test Club',
                       'competition': 'An Old Competition',
                       'places': 2
                       }
        response = client.post('/purchasePlaces', data=input_value)
        assert response.status_code == 200
        assert f"past competition" in response.data.decode()
