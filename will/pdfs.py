from django.template.loader import get_template
from xhtml2pdf import pisa
from cStringIO import StringIO
from django.template.context import Context

# def render_to_pdf(template_src, context_dict):
#     """Function to render html template into a pdf file"""
#     template = get_template(template_src)
#     context = Context(context_dict)
#     html = template.render(context)
#     result = StringIO()
#
#     pdf = pisa.pisaDocument(StringIO(html.encode("UTF-8")),
#                                             dest=result,
#                                             encoding='UTF-8',
#                                             link_callback=fetch_resources)
#     if not pdf.err:
#         response = HttpResponse(result.getvalue(),
#                                                     mimetype='application/pdf')
#
#         return response
#
#     return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))
    
