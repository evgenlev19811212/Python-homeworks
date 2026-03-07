import requests
from dotenv import load_dotenv
import os


class YouGile:
    def __init__(self):
        load_dotenv()
        self.url = os.getenv('base_url')

    def get_companies(self):
        load_dotenv()
        login = os.getenv('login')
        password = os.getenv('password')
        body = {
                "login": login,
                "password": password
                }
        resp = requests.post(self.url+'/api-v2/auth/companies', json=body)
        IdCompany = resp.json()['content'][0]['id']
        # запись в .env
        env_lines = []
        with open('lesson_08/.env', 'r') as env_file:
            env_lines = env_file.readlines()

        with open('lesson_08/.env', 'w') as env_file:
            for line in env_lines:
                if line.startswith("IdCompany = "):
                    env_file.write(f"IdCompany = '{IdCompany}'\n")
                else:
                    env_file.write(line)
        return IdCompany

    def get_keys(self, IdCompany):
        load_dotenv()
        login = os.getenv('login')
        password = os.getenv('password')
        body = {
                "login": login,
                "password": password,
                "companyId": IdCompany
                }
        resp = requests.post(self.url+'/api-v2/auth/keys/get', json=body)
        API_key = resp.json()[0]['key']
        # запись в .env
        env_lines = []
        with open('lesson_08/.env', 'r') as env_file:
            env_lines = env_file.readlines()

        with open('lesson_08/.env', 'w') as env_file:
            for line in env_lines:
                if line.startswith("API_key = "):
                    env_file.write(f"API_key = '{API_key}'\n")
                else:
                    env_file.write(line)
        return API_key

    def create_project(self, API_key, title="Best Of Project"):
        body = {
                "title": title,
                "users": {"0c895364-f956-4810-a0e0-4011d09f603b": "admin"}
                }
        headers = {
                    "Authorization": f"Bearer {API_key}"
                    }
        resp = requests.post(f"{self.url}/api-v2/projects", json=body, headers=headers) # noqa
        return resp

    def edit_project(self, API_key, project_Id, title="Best Project Of My Company"): # noqa
        body = {
                "title": title
                }
        headers = {
                    "Authorization": f"Bearer {API_key}"
                    }
        resp = requests.put(f"{self.url}/api-v2/projects/{project_Id}", json=body, headers=headers) # noqa
        return resp

    def get_for_id(self, API_key, project_Id):
        headers = {
                    "Authorization": f"Bearer {API_key}"
                    }
        resp = requests.get(f"{self.url}/api-v2/projects/{project_Id}", headers=headers) # noqa
        return resp

    def delete_project(self, API_key, project_Id):
        headers = {
                    "Authorization": f"Bearer {API_key}"
                    }
        body = {
                "deleted": True
                }
        resp = requests.put(f"{self.url}/api-v2/projects/{project_Id}", json=body, headers=headers) # noqa
        del_Id = resp.json()['id']
        return del_Id
