from utilities_dir.passwords.passwords import passwords
from utilities_dir.classes.Jira_class import Jira
from utilities_dir.classes.Jira_rest_api import Jira_rest_api
from .models import Quality_rating


def handle_request(data):
	
	print(passwords['jira_db_production'])
	data['Jira'] = Jira

	data['jira_instance'] = data['Jira'](passwords['jira_db_production'])
	jira_api = Jira_rest_api(passwords['jira_rest_api'])
	if data['jira_instance'].check_resolution_uniqueness(data['ticket_id'],data['user_id'], data['time']) == 302:
		return 302
	else:
		print('here')
		## save to local db 

		rating_local_db = Quality_rating(	
											ticket_id=data['ticket_id'], 
											rating=data['rating'],
											comment=data['comment'],
											user=data['user_id'],
											resolution_time=data['time']
										)

		rating_local_db.save()

	 	## save to jira db

		data['jira_instance'].save_comment( data['rating'], 
											data['comment'], 
											data['ticket_id'],
											data['user_id'],
											data['time'])

		data['ticket_sd_num'] = data['jira_instance'].get_sd_number(data['ticket_id'])

		## add comment to jiraissue
		if data['ticket_sd_num']:

			
			result = jira_api.add_comment(data['comment'],
													   data['rating'],
										  	  		   data['ticket_sd_num']
										  	  		   )

			if result.status_code != 201:
				print(f'Exception occurred: {result}')
				data['logger'].critical(f'{result.text}')

			return result.status_code