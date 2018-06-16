from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseNotFound
from reportlab.pdfgen import canvas

from .models import Bokning

x = 75
y = 800
size = 12

def drawHeader(c):
    global x,y
    c.drawString(x,y, "Telefon: 070-557 66 38 - info@minipumpar - orgnr 556851-2809")
    y = y - 40

def drawFields(c, bokning):
    global x,y
    fields = [f.name for f in bokning._meta.get_fields()]
    for i,n in enumerate(fields):
        c.setFont("Courier-Bold", size)
        c.drawString(x,y,fields[i].title())
        c.setFont("Courier", size)
        value = str(getattr(bokning,fields[i]))
        if (value == "None"):
            pass
        else:
            c.drawString(x+145,y, value)
        y = y - 25

# Create your views here.
def createPdf(request, bokningId):
    if request.method == 'GET':
        id = int(bokningId)
        try:
            bokning = Bokning.objects.get(id=id)
            #fields = [f.name for f in bokning._meta.get_fields()]
            #for i,n in enumerate(fields):
                #if bokning.name != None
                #Print name of field
                #print(fields[i])

                #Print value of that field
                #print(getattr(bokning,fields[i]))
        except Bokning.DoesNotExist:
            return HttpResponseNotFound()
        # Create the HttpResponse object with the appropriate PDF headers.
        # Användar ser pdf i webbläsaren.
        response = HttpResponse(content_type='application/pdf')
        #response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

        # Skapar pdf lokalt. Används för tester.
        # Create the PDF object, using the response object as its "file."
        c = canvas.Canvas("bookning.pdf")
        #Font
        c.setFont("Courier", 12)
        drawHeader(c)
        drawFields(c, bokning)

        # Close the PDF object cleanly, and we're done.
        c.showPage()
        c.save()
        return response
    else:
        return HttpResponseNotAllowed(['GET'])
