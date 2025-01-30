from locust import HttpUser, TaskSet, task, between

# class UserBehavior(TaskSet):
#     @task
#     def test_api(self):
#         # Replace with your API endpoint and payload
#         self.client.get("/api/v1/resource")

# # class WebsiteUser(HttpUser):
# #     tasks = [UserBehavior]
# #     wait_time = between(1, 5)  # Simulates user think time (1 to 5 seconds)

# class WebsiteUser(HttpUser):
#     # wait_time = between(0,0.001)  # User waits between 1-2 seconds between requests

#     @task
#     def test_api(self):
#         # Log start of the request
#         print("Sending GET request to /api/v1/resource...")
        
#         # Send the request and wait for the response
#         response = self.client.get("/api/v1/resource")

#         # Log the response to confirm it's received before the next request
#         if response.status_code == 200:
#             print(f"GET Response received: {response.json()}")
#         else:
#             print(f"GET failed with status code: {response.status_code}")



class UserBehavior(TaskSet):
    @task
    def face_detect(self):
        self.client.get(
            url='/face/detect',
            params={
                'filePath': '/mnt/012_19922617289000218_P.jpg',
                'location': 'true',
                'compare': 'true'
            },
            headers={'accept': 'application/json'}
        )

    # @task
    # def face_detect_post(self):
    #     with open('/home/hasan/Downloads/test1.jpg', 'rb') as file:
    #         self.client.post(
    #             url='/face/detect/v2',
    #             headers={
    #                 'accept': 'application/json',
    #                 # 'Content-Type': 'multipart/form-data'
    #             },
    #             files={'file': ('test1.jpg', file, 'image/jpeg')}
    #         )
class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    # wait_time = between(1, 5)
    host = 'http://172.16.7.82:4102'