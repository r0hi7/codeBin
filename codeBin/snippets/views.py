from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import  JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

#Allow the clien to make the posst request with out CSRF token
@csrf_exempt

#Request is a stream of JSON text from api call
def snippet_list(request):
    if request.method == 'POST':
        data = data.JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)

    elif request.method == 'GET':
        snippets = Snippet.objects.all()
        serializers = SnippetSerializer(snippets,many=True)
        return JsonResponse(serializers.data,safe=False)

def snippet_details(request,pk):
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesnotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(204)
        
