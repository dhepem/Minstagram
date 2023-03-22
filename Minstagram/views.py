from rest_framework.views import APIView
from django.shortcuts import render

class Sub(APIView):
    def get(self, request):
        print("get으로 호출")
        return render(request, "Minstagram/main.html")

    def post(self, request):
        print("post로 호출")
        return render(request, "Minstagram/main.html")