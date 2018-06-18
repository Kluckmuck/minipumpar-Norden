from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from reportlab.pdfgen import canvas

from .models import Bokning

x = 75
y = 800
size = 12

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
        #Draws each field value to the right of field name
        c.setFont("Courier", size)
        value = str(getattr(bokning,fields[i]))
        if (value == "None"):
            #If the field value is None, dont draw
            pass
        else:
            c.drawString(x+145,y, value)
        y = y - 25

# Create your views here.
@login_required
def mailBokning(request):
    if request.method == 'POST':
        bokning = request.POST.get('bokning', '')
        recipient = request.POST.get('recipient', '')
        from_email = request.POST.get('user', '')
        if subject and recipient and from_email:
            try:
                bokning = Bokning.objects.get(id=id)
            except Bokning.DoesNotExist:
                return HttpResponseNotFound()
            createPdf(bokning)
            try:
                send_mail('subject', 'message', from_email, [recipient])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponse(status=200)
    else:
        return HttpResponse('Make sure all fields are entered and valid.')

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
