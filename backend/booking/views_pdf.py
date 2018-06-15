from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseNotFound
from reportlab.pdfgen import canvas

from .models import Bokning

# Create your views here.
def createPdf(request, bokningId):
    if request.method == 'GET':
        id = int(bokningId)
        try:
            bokning = Bokning.objects.get(id=id)
            fields = [f.name for f in bokning._meta.get_fields()]
            for n in fields:
                #if bokning.name != None
                print(bokning.n)

        except Bokning.DoesNotExist:
            return HttpResponseNotFound()
        # Create the HttpResponse object with the appropriate PDF headers.
        # Användar ser pdf i webbläsaren.
        response = HttpResponse(content_type='application/pdf')
        #response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

        # Skapar pdf lokalt. Används för tester.
        # Create the PDF object, using the response object as its "file."
        p = canvas.Canvas("bookning.pdf")

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        p.drawString(100, 100, "Hello world.")


        # Close the PDF object cleanly, and we're done.
        p.showPage()
        p.save()
        return response
    else:
        return HttpResponseNotAllowed(['GET'])
