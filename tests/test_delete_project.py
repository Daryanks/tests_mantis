from model.project import Project
import random

def test_delete_project(app):
    projects = app.project.get_projects_list()
    project = random.choice(projects)
    app.project.delete(project)
    new_project = app.project.get_projects_list()
    projects.remove(project)
    assert sorted(projects, key=Project.id_or_max) == sorted(new_project, key=Project.id_or_max)