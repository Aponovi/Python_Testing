from server import POINTS_FOR_A_PLACE


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
        response = client.post('/purchasePlaces', data={'club': 'Test Club',
                                                        'competition': 'Spring Festival',
                                                        'places': 2
                                                        }
                               )
        expected_value = 13-(2 * POINTS_FOR_A_PLACE)
        assert response.status_code == 200
        assert "Great-booking complete" in response.data.decode()
        assert f"Points available: {expected_value}"

    def test_purchase_more_than_the_points(self, client, mock_competitions_and_clubs):
        response = client.post('/purchasePlaces', data={'club': 'Last Test Club',
                                                        'competition': 'Spring Festival',
                                                        'places': 5
                                                        }
                               )
        assert response.status_code == 200
        assert "cannot book" in response.data.decode()
