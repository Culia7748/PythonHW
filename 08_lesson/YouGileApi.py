import requests

class YouGileApi:
    def __init__(self, url):
        self.url = url
        self.token = 'Подставить свой токен'
        self.project_id = 'da5b036a-139c-469e-aa9c-901f6423d25b'

    def new_project(self, title):
        my_headers = {}
        my_headers["Authorization"] = "Bearer " + self.token
        project = {
            "title": title,
            "users": {
                "da5b036a-139c-469e-aa9c-901f6423d25b": "admin"
            }
        }
        resp = requests.post(self.url + '/api-v2/projects', headers=my_headers, json=project)
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
        return resp

    def get_project_id(self, project_id):
        my_headers = {}
        my_headers["Authorization"] = "Bearer " + self.token
        #resp = requests.get(self.url + '/api-v2/projects/'+ self.project_id, headers=my_headers)
        resp = requests.get(f"{self.url}/api-v2/projects/{project_id}", headers=my_headers)
        return resp
