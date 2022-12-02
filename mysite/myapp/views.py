from urllib import request
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from myapp.forms import InputForm       # Llamo a la clase "InputForm"
from datetime import date

# Create your views here.

# def index_view(request):
#     return HttpResponse(str(request.method))  # .META
    
# def index_view(request):
#     if request.method == "GET":
#         print("GET")
#         return HttpResponse("Metodo Index")
#     elif request.method == "POST":
#         print("POST")
#     return HttpResponse("Index")


class index_view(View):             # templateview
    template = "index.html"
    contexto={}
    contexto['name']='Juan'
    contexto['last_name']='Perez'
    def get(self, request):
        print("GET")
        #return HttpResponse("Index")
        return render(
            request = request,
            template_name = self.template,
            context=self.contexto
            )

    def post(self, request):
        print("POST")
        return HttpResponse("Index Post")


## TAREA 2_1

def calcular_edad(dia, mes, anio):
    fecha_actual = date.today()
    fecha_nacimiento = date(anio, mes, dia )
    edad = fecha_actual.year - fecha_nacimiento.year
    # esta re asicnacion a resultado nos comprueba la edad exacta contando los meses
    edad -= ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    print("La edad es: ", str(edad))
    return edad

class vista1_view(View):             # templateview
    template = "vista1.html"

    edad = calcular_edad(30,12,1998)

    contexto={}
    contexto['name'] = 'Juan'
    contexto['edad'] = edad
    fecha_actual = date.today()

    def get(self, request):
        print("GET")
        return render(
            request = request,
            template_name = self.template,
            context=self.contexto
            )

## TAREA 2_2

class vista2_view(View):             # templateview
    template = "vista2.html"
    contexto={}
    contexto['name']='la vista 2'
    contexto['lista_numeros']=[1,2,3,4]
    def get(self, request):
        print("GET")
        return render(
            request = request,
            template_name = self.template,
            context=self.contexto
            )


# class form_view(View):
#     template = "form.html"
#     contexto = {}

#     def get(self, request):
#         form_get = InputForm(request.GET)
#         form_post = InputForm(request.POST)
#         self.contexto['form_get'] = form_get
#         self.contexto['form_post'] = form_post
#         return render(
#             request=request,
#             template_name=self.template,
#             context=self.contexto
#             )

#     def post(self, request):
#         print("POST")
#         form_get = InputForm(request.GET)
#         form_post = InputForm(request.POST)
#         self.contexto['form_get'] = form_get
#         self.contexto['form_post'] = form_post
#         print(form_post.cleaned_data['aula'])
#         return render(
#             request=request,
#             template_name=self.template,
#             context=self.contexto
#             )

def aula_view(request, aula, horario):
    return HttpResponse(f"El parámetro enviado por URL es {aula}, {horario}")

# def form_view(request):
#     if request.method == "POST":
#         form = InputForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data["aula"])
#             return redirect(aula_view, aula= form.cleaned_data["aula"], horario=form.cleaned_data["hora_entrada"])

#     context = {}
#     context['form']= InputForm()
#     return render(request, "form.html", context)

def form_view(request):
    context = {}
    context['form']= InputForm()
    return render(request, "form.html", context)