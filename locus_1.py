# from locust import HttpUser, TaskSet, task, between
# from locust.user import wait_time
# import random
#
#
# class UserBehavior(TaskSet):
#     # tasks = {index: 2, profile: 1}
#
#     def on_start(self):
#         self.login()
#
#     def on_stop(self):
#         self.logout()
#
#     def login(self):
#         self.client.post("/api/public/core/login",{"username":"admin","password":"123"})
#
#     def logout(self):
#         self.client.post("/api/public/core/logout", {"username":"admin", "password":"123"})
#
#     @task(1)
#     def index(self):
#         l.client.get("/")
#
#     @task(2)
#     def profile(self):
#         l.client.get("/profile")
#
#
# class WebsiteUser(HttpUser):
#     task_creat = UserBehavior
#     wait_time = between(5, 9)
#     # wait_time = lambda self : random.expovariate(1)*1000

from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):

    def login(self):

        self.client.post("/api/public/core/login", {"username":"admin", "password":"123"})
        # assert r.status_code == 200

    def logout(self):
        self.client.post("/api/public/core/logout", {"username":"admin", "password":"123"})
        # assert r.status_code == 200

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        self.logout()

    @task(2)
    def index(self):
        self.client.get("/")
        # assert r.status_code == 200

    @task(1)
    def profile(self):
        self.client.get("/profile")
        # assert r.status_code == 200

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    # task_set = UserBehavior
    wait_time = between(5, 8)
