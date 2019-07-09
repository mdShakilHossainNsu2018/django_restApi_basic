from django.views.generic import View
from django.http import HttpResponse
from updates.models import Update


class UpdateModelDetailAPIView(View):
    def get(self, request, id, *args, **kwargs):
        obj = Update.objects.get(id=id)
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        pass

    def put(self, request, *args, **kwargs):
        pass

    def delete(self, request, *args, **kwargs):
        pass


class UpdateModelListAPIView(View):
    def get(self, request, id, *args, **kwargs):
        obj = Update.objects.all()
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        pass

    def put(self, request, *args, **kwargs):
        pass

    def delete(self, request, *args, **kwargs):
        pass

