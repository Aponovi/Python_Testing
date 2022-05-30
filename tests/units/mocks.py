def mock_loadClubs():
    clubs = [
        {
            "name": "Test Club",
            "email": "test@club.com",
            "points": "13"
        },
        {
            "name": "Second Test Club",
            "email": "secondtest@club.com",
            "points": "50"
        },
        {
            "name": "Last Test Club",
            "email": "lasttest@club.com",
            "points": "2"
        },
    ]
    return clubs


def mock_loadCompetitions():
    competitions = [
        {
            "name": "Spring Festival",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "25"
        },
        {
            "name": "Fall Classic",
            "date": "2020-10-22 13:30:00",
            "numberOfPlaces": "13"
        },{
            "name": "Little Competition",
            "date": "2020-10-22 13:30:00",
            "numberOfPlaces": "2"
        },
    ]
    return competitions
