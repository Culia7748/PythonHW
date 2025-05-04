import requests

class YouGileApi:
    def __init__(self, url):
        self.url = url
        self.token = 'Cvp3faLCEVUqz+wnTckiAfe0f8xWOIg+KmLKw8y9GyAuc4VoMzM6DQOI-xCezfB+'
        self.project_id = 'da5b036a-139c-469e-aa9c-901f6423d25b'

    def get_token(self, login='164ast@gmail.com', password='7cucBao-Io',
                  companyId='36463eda-b086-4629-aee2-9004e171a820'):
        creds = {
            "login": login,
            "password": password,
            "companyId": companyId
        }
        resp = requests.post(self.url + '/api-v2/auth/keys', json=creds)
        return resp.json()["key"]

    def new_project(self, title):
        my_headers = {}
        my_headers["Authorization"] = "Bearer " + self.token
        project = {
            "title": title,
            "users": {
                "da5b036a-139c-469e-aa9c-901f6423d25b": "admin"
            }
        }
        print(my_headers["Authorization"])
        resp = requests.post(self.url + '/api-v2/projects', headers=my_headers, json=project)
        print(resp.json()['id'])
        return resp
        # project_id = project.json()['id']

    def change_project(self, id, new_title):
        my_headers = {}
        my_headers["Authorization"] = "Bearer " + self.token
        project = {
            "title": new_title
        }
        project_add_point = self.url + '/api-v2/projects/'+ str(id)
        resp = requests.put(project_add_point, headers=my_headers, json=project)
        print(project_add_point)
        return resp


    def get_project_id(self, project_id):
        my_headers = {}
        my_headers["Authorization"] = "Bearer " + self.token
        #resp = requests.get(self.url + '/api-v2/projects/'+ self.project_id, headers=my_headers)
        resp = requests.get(f"{self.url}/api-v2/projects/{project_id}", headers=my_headers)
        return resp
