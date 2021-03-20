from django.shortcuts import render, redirect
from .services import *
from django.conf import settings
from datetime import datetime
import dateutil.parser
from .decorators import check_recaptcha



def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


@check_recaptcha
def index(request, ticket_id=0, user_id='Some user', time='2000-01-01T23:27:54.2+0000'):


	if request.recaptcha_is_valid:
		
		

		if request.score > 0.6:
			if request.POST.get('rating'):
				data = {
					'passwords_dict': None,
					'Jira': None,
					'rating': request.POST.get('rating'),
					'comment': request.POST.get('comment'),
					'ticket_id': request.POST.get('ticket_id'),
					'jira_instance': None,
					'ticket_sd_num': None,
					'logger': request.custom_logger,
					'user_id': request.POST.get('user_id'),
					'time': request.POST.get('time')
				}

				if data['ticket_id'] is None:
					data['ticket_id'] = 0
				print(data)
				ip = get_client_ip(request)
				request.custom_logger.info(f"{ip}: {data['ticket_id']}, {data['user_id']}, {data['time']}")
				if handle_request(data) == 302:
					return redirect('dubble_comment')
				else:
					
					return redirect('response')
		else:
			return redirect('recaptcha_false')

		

	
	return render(request, 'main/index.html', { 'ticket_id' : ticket_id ,  'user_id': user_id, 'need_comment': False, 'time': time, 'site_key': settings.RECAPTCHA_SITE_KEY })
	
		


def response(request):
	return render(request, 'main/response.html', {})


def recaptcha_false(request):
	return render(request, 'main/recaptcha_false.html', {})

def dubble_comment(request):
	return render(request, 'main/dubble_comment.html', {})
	