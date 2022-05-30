class TestLoginClass:
    def test_login_email_known(self, client, mock_competitions_and_clubs):
        response = client.post('/showSummary', data={"email": "test@club.com"})
        assert response.status_code == 200
        assert f"Welcome, " in response.data.decode()

    def test_login_email_unknown(self, client, mock_competitions_and_clubs):
        response = client.post('/showSummary', data={"email": "unkown@email.com"})
        assert response.status_code == 200
        assert "Sorry, that email wasn&#39;t found." in response.data.decode()
