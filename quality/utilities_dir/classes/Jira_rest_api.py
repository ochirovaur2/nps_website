from requests.auth import HTTPBasicAuth
import json
import requests


class Jira_rest_api:
	"""docstring for Jira_rest_api"""
	def __init__(self, jira_rest_api):
		self.jira_rest_api = jira_rest_api
		
	def add_comment(self, msg, rating, issuenum ):

		msg = f'Оценка пользователя:\n\n \t{rating}\n\n  Отзыв пользователя:\n\n \t{msg}'
		headers = {
		   "Accept": "application/json",
		   "Content-Type": "application/json"
		}
		
		
		url = f"https://jira.cdek.ru/rest/api/2/issue/{issuenum}/comment"


		auth = HTTPBasicAuth(self.jira_rest_api['user'], 
							 self.jira_rest_api['password'])

		
		payload = json.dumps({
			"body": msg,
			"visibility": {
			    "type": "role",
			    "value": "Support"
			  }
		
		})

		response = requests.request(
		   "POST",
		   url,
		   data=payload,
		   headers=headers,
		   auth=auth
		)
		
		return response
	