from __future__ import division
from django.template.loader import get_template
from django.utils.html import escape
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.template.context import Context
import StringIO
from xhtml2pdf import pisa
from will.models import Testator, Relationships, Inheritors
from django.conf import settings
import os
# from pdfs import render_to_pdf

def calcEds(person):
    edList = ["Son", "Daughter", "Grandchild"]
    eds = person.inheritors_set.filter(relationType__type__in=edList).count()
    return eds

def fetch_resources(uri, rel):
    """
    Callback to allow xhtml2pdf/reportlab to retrieve Images,Stylesheets, etc.
    `uri` is the href attribute from the html link element.
    `rel` gives a relative path, but it's not used here.

    """
    if uri.startswith(settings.MEDIA_URL):
        path = os.path.join(settings.MEDIA_ROOT,
                            uri.replace(settings.MEDIA_URL, ""))
    elif uri.startswith(settings.STATIC_URL):
        path = os.path.join(settings.STATIC_ROOT,
                            uri.replace(settings.STATIC_URL, ""))
    else:
        path = os.path.join(settings.STATIC_ROOT,
                            uri.replace(settings.STATIC_URL, ""))

        if not os.path.isfile(path):
            path = os.path.join(settings.MEDIA_ROOT,
                                uri.replace(settings.MEDIA_URL, ""))

            if not os.path.isfile(path):
                raise UnsupportedMediaPathException(
                                    'media urls must start with %s or %s' % (
                                    settings.MEDIA_ROOT, settings.STATIC_ROOT))

    return path
    
def download_pdf(request):
    """Build briefing packages format and export as HTML and PDF."""
    response = HttpResponse(content_type='application/pdf')
    return generate_pdf('will/will.html', file_object=response)
    
##commented out because importing this from pdfs
def render_to_pdf(template_src, context_dict):
    """Function to render html template into a pdf file"""
    template = get_template(template_src)
    context = Context(context_dict)
    html = template.render(context)
    result = StringIO.StringIO()
    print fetch_resources

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")),
                                            dest=result,
                                            encoding='UTF-8',
                                            link_callback=fetch_resources)
    if not pdf.err:
        response = HttpResponse(result.getvalue(),
                                                    content_type ='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Last will of %s dated.pdf"' %context['person'].name #include this to make a download, otherwise delete
        return response

    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

def createPDF(request, context):
    pdf = create_pdf(render(request, 'will/results.html', context))
    return pdf
    
def download_pdf(request):
    """Build briefing packages format and export as HTML and PDF."""
    response = HttpResponse(content_type='application/pdf')
    return generate_pdf('will/results.html', file_object=response)
    
def calcSpouse(person, results):
    try:
        # spouse = Inheritors.objects.get(testator=testator_id, relationType__type__in=["Wife", "Husband"])
        spouse = person.inheritors_set.get(relationType__type__in=["Wife", "Husband"])
    except Inheritors.DoesNotExist:
        spouse = None
    if spouse and spouse.alive:
        if calcEds(person) == 0:
            if person.gender=="Female":
                results["spShare"] = 1/2
            else:
                results["spShare"] = 1/4
        else:
            if person.gender == "Female":
                results["spShare"] = 1/4
            elif person.gender =="Male":
                results["spShare"] = 1/8
        results["residue"] -= results["spShare"]
    return results
    
def calcChildren(person, results):
    numBoys = person.inheritors_set.filter(relationType__type="Son").count()
    numGirls = person.inheritors_set.filter(relationType__type="Daughter").count()
    if numBoys and numGirls:
        numKids = (numBoys*2) + numGirls
        results["sShare"] = (results["residue"]*(2 / numKids))*numBoys
        results["dShare"] = (results["residue"]*(1 / numKids))*numGirls
        results["residue"] = results["residue"] - results["sShare"] - results["dShare"]
    elif numBoys and not numGirls:
        results["sShare"] = results["residue"]
        results["residue"] = 0
    elif numGirls and not numBoys:
        if numGirls == 1:
            results["residue"] -= 1/2
            results["dShare"] = 1/2
        if numGirls>=2:
            results["residue"] -= 2/3
            results["dShare"] = 2/3
            if results["residue"] >=0:
                 results["dShare"] += results["residue"]
    return results

def calcParents(person, results):
    try:
        father = person.inheritors_set.get(relationType__type="Father")
    except:
        father = None
    try:
        mother = person.inheritors_set.get(relationType__type="Mother")
    except:
        mother = None
    if father and father.alive and mother and mother.alive and person.inheritors_set.filter(relationType__type__in=["Son", "Daughter"]).count()==0:
        results["mShare"]=results["residue"]/3
        results["fShare"]=2*results["residue"]/3
        results["residue"]=0
    elif father and father.alive and mother and mother.alive:
        if calcEds(person)>=1:
            results["fShare"], results["mShare"] = 1/6, 1/6
            results["residue"] -= 1/3
            results = calcChildren(person, results)
            if results["residue"] >= 0:
                results["fShare"] += results["residue"]
                results["residue"] = 0
        else:
            results["mShare"] = 1/6
            results["residue"] -= 1/6
            results["fShare"] = results["residue"]
            results["residue"] = 0
    elif father and father.alive:
        results["fShare"] = 1/6
        results["residue"] -= 1/6
        results = calcChildren(person, results)
    elif mother and mother.alive:
        results["mShare"] = 1/6
        results["residue"] -= 1/6
        results = calcChildren(person, results)
    else:
        results = calcChildren(person, results)
    return results
    
def calculate(testator_id):
    results = {}
    results["residue"]=1
    results["spShare"]=0
    person = Testator.objects.get(pk=testator_id)
    results = calcSpouse(person, results)
    results = calcParents(person, results)
    total = 0
    for i, j in results.iteritems():
        if i !="residue":
            total +=j
    if total <= 1:
        for i, j in results.iteritems():
            if i != "spShare":
                results[i] += (1-total)*(j/(total-results["spShare"]))
    if total >= 1:
        for i, j in results.iteritems():
            results[i] += (1-total)*(j/(total))
    results["residue"]=0
    for i, j in results.iteritems():
        results[i] = round(j, 4)
    return results

def relIdByName(relType):
    rel = Relationships.objects.get(type=relType)
    return rel.id

def index(request):
    people = Testator.objects.all()
    context = {"people": people}
    return render(request, 'will/index.html', context)
        
def newperson(request, action, testator_id):
    if action=="new":
        return render(request, 'will/newperson.html')
    if action=="delete":
        d = Testator.objects.get(pk=testator_id)
        d.delete()
        return HttpResponseRedirect(reverse('will:index'))
    if request.method=="POST":
        if action=="add":
            a = Testator(
                name = request.POST["name"],
                gender = request.POST["gender"]
                )
            a.save()
        return HttpResponseRedirect(reverse('will:index'))

def detail(request, testator_id):
    relTypes = Relationships.objects.all()
    person = Testator.objects.get(pk=testator_id)
    context = {"relatives": relTypes, "person": person}
    return render(request, 'will/detail.html', context)
    
def results(request, testator_id):
    results = calculate(testator_id)
    person = Testator.objects.get(pk=testator_id)
    context = {"results": results, "person": person}
    return render_to_pdf('will/will.html', context) #switch to download
    # return render(request, 'will/will.html', context) #switch to show text
    
def edit(request, testator_id, relID, action):
    person = Testator.objects.get(pk=testator_id)
    if action =="delete":
        d = Inheritors.objects.get(pk=relID)
        d.delete()
    elif action =="edit":
        pass
    elif action =="add":
        a = person.inheritors_set.create(
            name = request.POST["name"],
            gender = request.POST["gender"],
            alive = request.POST["alive"],
            relationType = Relationships.objects.get(pk=request.POST["relType"])
            )
    return HttpResponseRedirect(reverse('will:detail', args=(person.id,)))
    
    
def input(request):
    people = Testator.objects.all()
    context = {"people": people}
    #switch from old template to testing new jquery template
    #return render(request, 'will/jquery.html', context)
    return render(request, 'will/jqueryv2.html', context)