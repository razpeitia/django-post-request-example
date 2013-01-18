
from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
	context = RequestContext(request)
	data = {}
	if request.method == "POST":
		template_name = "respuesta.html"
		if request.POST.get("nombre").lower() == "hola":
			data['result'] = True
	elif request.method == "GET":
		template_name = "formulario.html"
	return render_to_response(template_name, data, context_instance=context)