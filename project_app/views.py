from django.shortcuts import render
from rest_framework import generics, status
from .models import Project
from .serializers import ProjectSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

class ListProject(generics.ListAPIView):
    queryset =  Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        project_set = list(Project.objects.all())
        mech = self.request.GET.get('sort_type')
        if (mech == 'oldest'):
            project_set.sort(key= lambda p : p.date_added)
        elif (mech == 'hits'):
            project_set.sort(key= lambda p : p.hits, reverse=True)
        elif (mech == 'newest'):
            project_set.sort(key= lambda p : p.date_added, reverse=True)
        else:
            project_set.sort(key= lambda p : p.relevance, reverse=True)
        return project_set


class IncreaseHitView(APIView):
    def post(self, request, project_id, format=None):
        try:
            project = Project.objects.get(id=project_id)
            project.hits += 1
            project.save()
            return Response(status=status.HTTP_200_OK)
        
        except Project.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
