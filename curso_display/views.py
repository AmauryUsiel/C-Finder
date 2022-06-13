from django.shortcuts import render
import requests
import json

#from curso_display.models import Curso

#Function Search on YT
def get_video_info(query, limit=10):
  API_KEY = "AIzaSyChTidnjz4vGKoG6_L8DqCDGrhoUFuEx8I"
  url = "https://www.googleapis.com/youtube/v3/search"
  data = {
      "key": API_KEY,
      "part": "id,snippet",
      "q": query,
      "max_results": limit
  }
  r = requests.get(url, params=data)
  j = r.json()

  # Retorna la lista simplificada
  return [ (v["id"]["videoId"], v["snippet"]["title"], v["snippet"]["channelTitle"], v["snippet"]["description"], v["snippet"]["thumbnails"]["medium"]["url"]) for v in j["items"] ]
# Create your views here.

def cursos(request):
    busqueda = request.GET.get("buscar")
    #cursos = Curso.objects.all()
    resultados = get_video_info(busqueda)
    dicgen = {}
    
    for i in range(10):
        dicgen [i] = {
            'url': "https://www.youtube.com/watch?v={}".format(resultados[i][0]),
            'titulo': "{}".format(resultados[i][1]), 
            'autor': "{}".format(resultados[i][2]),
            'descripcion': "{}".format(resultados[i][3]), 
            'thumbnail': "{}".format(resultados[i][4])}
   
    return render(request, 'cursos_display/v_cursos.html', context = {'infoVid': dicgen})





