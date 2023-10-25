from django.shortcuts import render
from django.http import HttpResponse
import pdfkit

def generate_pdf(request):
    # Render the HTML template
    context = {}  # Define your context data

    # Use the template name directly, without the path
    html_template = 'pdf.html'

    html = render(request, html_template, context).content

    # Configure PDF options
    options = {
        'page-size': 'A4',
        'margin-top': '0mm',
        'margin-right': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm',
    }

    # Specify the path to wkhtmltopdf executable
    config = pdfkit.configuration(wkhtmltopdf='/path/to/wkhtmltopdf')

    # Convert HTML to PDF using the specified configuration
    pdf = pdfkit.from_string(html, False, configuration=config, options=options)

    # Return the PDF as a response
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="cotizacion.pdf"'
    return response
