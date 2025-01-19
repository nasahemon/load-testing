from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    @task
    def test_api(self):
        # Replace with your API endpoint and payload
        self.client.get("/api/v1/resource")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)  # Simulates user think time (1 to 5 seconds)

