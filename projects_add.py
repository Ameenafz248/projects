import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projects.settings")
django.setup()

from project_app.models import Project

with open("project_list.txt", "r") as file:
    gen_list = file.readlines()
    list_len = len(gen_list)
    j = 0
    for i in range(0, int(list_len / 3)):
        project = Project(name=gen_list[j].strip(), link=gen_list[j + 1].strip(), description=gen_list[j + 2].strip())
        project.save()
        j = j + 3
    file.close()