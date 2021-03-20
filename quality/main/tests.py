from django.test import TestCase
from .business_logics import handle_request

class BusinessLogicTestCase(TestCase):
	"""checking if business logic work correctly"""
	def test_handle_request(self):
		data = {
			'passwords_dict': None,
			'Jira': None,
			'rating': 5,
			'comment': 'test comment',
			'ticket_id': 0,
			'jira_instance': None,
			'ticket_sd_num': None,
			'user_id': 'Some user'
		}

		result = handle_request(data)

		self.assertEqual(201, result)
		