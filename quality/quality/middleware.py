from django.shortcuts import render
from utilities_dir.logger import setup_logger


### logging
setup_logger_func = setup_logger.get_logger()
logger = setup_logger_func('info_logger', 'utilities_dir/logs/new_logs.log')

class HandleExceptionsMiddleware:


	def __init__(self, get_response):
		self.get_response = get_response


	def __call__(self, request):
		
		

		request.custom_logger = logger

		response = self.get_response(request)
		
		return response

		
	# def process_exception(self, request, exception):

	# 	print(f'Exception occurred: {exception}')

	# 	request.custom_logger.critical(f'{exception}')

	# 	return render(request, 'main/index.html', { 'ticket_id' : 0})
