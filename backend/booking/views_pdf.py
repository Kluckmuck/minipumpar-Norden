from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage, BadHeaderError
from reportlab.pdfgen import canvas

from .models import Bokning
import json

x = 75
y = 800
size = 12
lineHeight = 25
lineWidth = 145

def createPdf(bokning, response=None):
    if (response != None):
        # Create the HttpResponse object with the appropriate PDF headers.
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

        # Create the PDF object, using the response object as its "file."
        c = canvas.Canvas(response)
    else :
        c = canvas.Canvas("bookning.pdf")
    #Font
    c.setFont("Courier", 12)
    drawHeader(c)
    drawFields(c, bokning)

    # Close the PDF object cleanly, and we're done.
    c.showPage()
    c.save()

def drawHeader(c):
    #Header for PDF
    global x,y
    c.drawString(x,y, "Telefon: 070-557 66 38 - info@minipumpar - orgnr 556851-2809")
    y = y - 40

def drawFields(c, bokning):
    #Body of PDF
    global x,y
    #Stores all field names in a list
    fields = [f.name for f in bokning._meta.get_fields()]
    for i,n in enumerate(fields):
        #Draws each field name in bold text & capitalizes the first letter
        c.setFont("Courier-Bold", size)
        c.drawString(x,y,fields[i].title())
        #Draw total time draw
        #if fields[i] is
        #Draws each field value to the right of field name
        c.setFont("Courier", size)
        value = str(getattr(bokning,fields[i]))
        if (value == "None"):
            #If the field value is None, dont draw
            pass
        else:
            c.drawString(x+lineWidth,y, value)
        y = y - lineHeight

# Create your views here.
@login_required
def mailBokning(request):
    if request.method == 'POST':
        try:
            bokning = json.loads(request.body.decode())['bokning']
            recipient = json.loads(request.body.decode())['recipient']
            sender = json.loads(request.body.decode())['sender']
        except KeyError:
            return HttpResponse(status=400)
        if bokning and recipient and sender:
            try:
                bokning = Bokning.objects.get(id=bokning)
            except Bokning.DoesNotExist:
                return HttpResponseNotFound()
            createPdf(bokning)
            try:
                email = EmailMessage(
                    subject='subject',
                    body='message',
                    from_email= sender,
                    to=[recipient]
                )
                email.attach_file('bookning.pdf')
                email.send(fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)
    else:
        return HttpResponseNotAllowed(['POST'])

@login_required
def createLocalPdfView(request, bokningId):
    if request.method == 'GET':
        id = int(bokningId)
        try:
            bokning = Bokning.objects.get(id=id)
        except Bokning.DoesNotExist:
            return HttpResponseNotFound()
        # Skapar pdf lokalt
        # Används för tester eller om vi ska spara på server i framtiden.
        createPdf(bokning)
        return HttpResponse(status=201)
    else:
        return HttpResponseNotAllowed(['GET'])
