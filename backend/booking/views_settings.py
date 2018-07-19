from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import json

# Create your views here.
@csrf_exempt
def targetMail(request):
    if request.method == 'POST':
        try:
            targetMail = json.loads(request.body.decode())['mail']
        except Exception as e:
            return HttpResponseBadRequest(json.dumps({'error': 'Invalid request: {0}'.format(str(e))}), content_type="application/json")
        user = request.user
        try:
            user = User.objects.get(username=user)
        except User.DoesNotExist as e:
            return HttpResponseBadRequest(json.dumps({'error': 'Invalid request: {0}'.format(str(e))}), content_type="application/json")
        try:
            validate_email(targetMail)
        except ValidationError as e:
            return HttpResponseBadRequest(json.dumps({'error': 'Invalid request: {0}'.format(str(e))}), content_type="application/json")
        user.profile.targetMail = targetMail
        user.save()
        return HttpResponse(status=201)
