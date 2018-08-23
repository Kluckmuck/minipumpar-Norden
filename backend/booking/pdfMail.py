from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage, BadHeaderError
from reportlab.pdfgen import canvas

from .models import Bokning
from .pdf import Pdf
from datetime import datetime
import json

import sendgrid
import os
import base64
from sendgrid.helpers.mail import *

x = 75
y = 725
size = 12
lineHeight = 25
lineWidth = 145
font = 'Helvetica'
fontBold = 'Helvetica-Bold'
pdf = Pdf(x, y, size, lineHeight, lineWidth, font, fontBold)


def pdfThenMail(bokning, kundmail=False):
    filePath = createPdf(bokning) #Create PDF, returns filepath
    try:
        with open(filePath, 'rb') as f:
            data = f.read()

        # Encode contents of file as Base 64
        encoded = base64.b64encode(data).decode()

        # Build attachment
        attachment = Attachment()
        attachment.content = encoded
        attachment.type = "application/pdf"
        attachment.filename = str(bokning.datum) + "(" + str(bokning.id) + ").pdf"
        attachment.disposition = "attachment"
        attachment.content_id = "PDF Document file"

        sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
        from_email = Email("service@algit.se")
        subject = bokning.__str__()

        content = Content("text/html", "<p>Det här mailet går ej att svara på.</p><p>Vid frågor kan ni nå Älg IT på 070-656 68 05</p>")

        #Send mail to kundmail
        if kundmail is not False:
            to_email = Email(kundmail)
            mail = Mail(from_email, subject, to_email, content)
            mail.add_attachment(attachment)
            response = sg.client.mail.send.post(request_body=mail.get())
            content = Content("text/html", "<p>Det här mailet går ej att svara på.</p><p>Kopia skickades till: " + str(kundmail) + "</p><p>Vid frågor kan ni nå Älg IT på 070-656 68 05</p>")

        #Send mail to targetMail
        to_email = Email(bokning.maskinist.profile.targetMail)
        to_email = Email('kluckmucki@gmail.com')
        content = targetContentBuilder(bokning, kundmail)
        mail = Mail(from_email, subject, to_email, content)
        mail.add_attachment(attachment)
        response = sg.client.mail.send.post(request_body=mail.get())
        silentRemove(filePath)
    except Exception as e:
        return e
    return True

def createPdf(bokning, response=None):
    if (response != None):
        # Create the HttpResponse object with the appropriate PDF headers.
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

        # Create the PDF object, using the response object as its "file."
        c = canvas.Canvas(response)
    else :
        filePath = "pdf/" + str(bokning.datum) + "(" + str(bokning.id) + ").pdf"
        c = canvas.Canvas(filePath)
    #Font
    c.setFont(pdf.font, pdf.size)
    drawHeader(c)
    drawFields(c, bokning)
    drawFooter(c)

    # Close the PDF object cleanly, and we're done.
    c.showPage()
    c.save()
    resetPdf() #restores pdf values
    return filePath

def drawHeader(c):
    #Header for PDF
    c.setFont(pdf.font, pdf.size + 3)
    c.drawString(pdf.x, pdf.y, "Telefon: 070-557 66 38 - info@minipumpar.se - orgnr 556851-2809")
    pdf.y = pdf.y - 60

def drawFooter(c):
    #Footer for PDF
    c.setFont("Helvetica-Oblique", pdf.size)
    c.drawString(pdf.x+380, 25, "Utvecklad av Älg IT")
    c.drawString(pdf.x+380, 10, "070-656 68 05")
    logo = os.path.abspath('./static/images/Watercolor_Moose.jpg')
    c.drawImage(logo,x+330,50, 150, 150)

def getHourMinute(time):
    #Appends zero if minute is 0-9
    minute = str(time.minute)
    if len(minute) is 1:
        minute = '0' + minute
    time = str(time.hour) + ':' + minute
    return time

def drawValue(c,string, bold=False):
    if bold == True:
        c.setFont(pdf.fontBold, pdf.size)
        c.drawString(pdf.x, pdf.y,string)
    else:
        c.setFont(pdf.font, pdf.size)
        c.drawString(pdf.x+pdf.lineWidth, pdf.y,string)

def drawFields(c, bokning):
    #Body of PDF
    #Stores field names in a list
    fields = [f.name for f in bokning._meta.get_fields()]
    for i,n in enumerate(fields):
        #Draws each field name in bold text & capitalizes the first letter
        if fields[i] is 'id':
            drawValue(c, 'Följesedels nr:', True)
        elif fields[i] is 'slangStr':
            drawValue(c, 'Slang längd:', True)
        elif fields[i] is 'pumpMng':
            drawValue(c, 'Pump mängd:', True)
        elif fields[i] is 'littNr':
            drawValue(c, 'Litt nr:', True)
        elif fields[i] is 'pumpStart':
            drawValue(c, 'Pump start:', True)
            #Special case because of date
            drawValue(c,getHourMinute(getattr(bokning,fields[i])))
        elif fields[i] is 'pumpSlut':
            drawValue(c, 'Pump slut:', True)
            #Special case because of date
            drawValue(c,getHourMinute(getattr(bokning,fields[i])))
        #Draw total time draw
        elif fields[i] is 'ovrigInfo':
            c.setFont(fontBold, size)
            c.drawString(pdf.x,pdf.y, 'Total tid')
            c.setFont(font, size)
            startTime = getattr(bokning,fields[i-2])
            endTime = getattr(bokning,fields[i-1])
            drawValue(c,str(endTime-startTime)[:-3])
            pdf.y = pdf.y - pdf.lineHeight
            drawValue(c, 'Övrig info:', True)
        #Draws each field value that is not caught before
        else:
            c.setFont(fontBold, size)
            c.drawString(pdf.x,pdf.y,fields[i].title() + ':')
        value = getattr(bokning,fields[i])
        if fields[i] is 'grundavgift':
            value = str(value) + ' kr'
        if fields[i] is 'resTid':
            value = str(value) + ' timmar'
        if fields[i] is 'pumpMng':
            int(value)
            value = str(value) + ' m3'
        if fields[i] is 'slangStr':
            value = str(value) + ' meter'
        if (value == None or isinstance(value, datetime)):
            #If the field value is None or date(date is drawed before), dont draw
            pass
        else:
            drawValue(c,str(value))
        pdf.y = pdf.y - pdf.lineHeight

def resetPdf():
    pdf.x = x
    pdf.y = y
    pdf.size = size
    pdf.lineHeight = lineHeight
    pdf.lineWidth = lineWidth
    pdf.font = font
    pdf.fontBold = fontBold

def silentRemove(filePath):
    try:
        os.remove(filePath)
    except OSError as e:
        print ('Could not remove file: ' + filePath)
        print(e)

def targetContentBuilder(b, k):
    if k is not False:
        return Content("text/html", "<p>Det här mailet går ej att svara på.</p><p>Kopia skickades till: " + str(k) + "</p><p>Vid frågor kan ni nå Älg IT på 070-656 68 05</p>")
    return Content("text/html", "<p>Det här mailet går ej att svara på.</p><p>Vid frågor kan ni nå Älg IT på 070-656 68 05</p>")
