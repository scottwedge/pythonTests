import requests

class BaseHttp:

    def __init__(self):
        self.session = requests.session()

    def get(self, url):
        return self.session.get(url)


class SomethingLikePageObjectForApi:

    def __init__(self):
        self.http = BaseHttp()

    def get_users(self, url):
        return self.http.get(url)

    def get_specific_user(self, url):
        return self.http.get(url)

    def get_number_of_posts_by_user(self, url):
        return self.http.get(url)

    def get_id_of_second_post(self, url):
        return self.http.get(url)

    def get_post_by_id(self, url):
        return self.http.get(url)
    

class Test:

    api = SomethingLikePageObjectForApi()

    def test_get_number_of_posts_by_user(self):
        response = self.api.get_number_of_posts_by_user("https://jsonplaceholder.typicode.com/posts?userId=3").json()
        
        assert len(response) is 10
        
    def test_get_id_of_second_post(self):
        response = self.api.get_number_of_posts_by_user("https://jsonplaceholder.typicode.com/posts?userId=3").json()

        assert response[1]['id'] is 22

    def test_get_post_by_id(self):
        response = self.api.get_post_by_id("https://jsonplaceholder.typicode.com/posts/22").json()

        expectedTitle = "dolor sint quo a velit explicabo quia nam"
        
        assert response['title'] == expectedTitle