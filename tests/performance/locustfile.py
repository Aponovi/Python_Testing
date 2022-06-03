from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def show_summary(self):
        self.client.post("/showSummary",
                         {"email": "john@simplylift.co"})

    @task
    def display_points_board(self):
        self.client.get("/points_board")

    @task
    def purchase_places(self):
        self.client.post("/purchasePlaces",
                         {"competition": "Fall Classic",
                          "club": "Simply Lift",
                          "places": "1"
                          })

    @task
    def logout(self):
        self.client.get("/logout")
