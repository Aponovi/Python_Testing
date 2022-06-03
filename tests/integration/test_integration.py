import server


class TestIntegration:
    def test_login_to_logout(self, client, mock_competitions_and_clubs):
        input_value_login = {"email": "test@club.com"}
        response = client.post('/showSummary', data=input_value_login)
        assert response.status_code == 200
        assert f"Welcome, " in response.data.decode()
        expected_club_value = 13 - (2 * server.POINTS_FOR_A_PLACE)
        expected_competition_value = 25 - 2
        input_value_purchase_places = {'club': 'Test Club',
                                       'competition': 'Spring Festival',
                                       'places': 2
                                       }
        response = client.post('/purchasePlaces', data=input_value_purchase_places)
        assert response.status_code == 200
        assert "Great-booking complete" in response.data.decode()
        assert f"Points available: {expected_club_value}"
        assert f"Number of Places: {expected_competition_value} Book Places"
        response = client.get("/logout", follow_redirects=True)
        assert response.status_code == 200
