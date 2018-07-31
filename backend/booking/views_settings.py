from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.forms.models import model_to_dict
import json

# Create your views here.
def targetMail(request):
    if request.method == 'POST':
        try:
            targetMail = json.loads(request.body.decode())['email']
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
    else:
        return HttpResponseNotAllowed(['POST'])

def getUserInfo(request, id):
    if request.method == 'GET':
        try:
            id = int(id)
        except ValueError as e:
            return HttpResponseBadRequest(json.dumps({'error': 'Invalid request: {0}'.format(str(e))}), content_type="application/json")
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return HttpResponse(status=404)
        return JsonResponse([{'username': user.username, 'last_login': user.last_login, 'first_name': user.first_name,
            'last_name': user.last_name, 'email': user.email, 'date_joined': user.date_joined,
            'targetMail': user.profile.targetMail}], safe=False)
    else:
        return HttpResponseNotAllowed(['GET'])
