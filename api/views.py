import imp
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Dog

# Create your views here.


class DogView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id > 0):
            dogs = list(Dog.objects.filter(id=id).values())
            if len(dogs) > 0:
                dog = dogs[0]
                data = {'message': 'Success', 'dog': dog}
            else:
                data = {'message': 'Dogs not found ...'}
            return JsonResponse(data)
        else:
            dogs = list(Dog.objects.values())
            if len(dogs) > 0:
                data = {'message': 'Success', 'dogs': dogs}
            else:
                data = {'message': 'Dogs not found ...'}
            return JsonResponse(data)
