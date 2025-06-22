from model.project import Project
import random

def test_delete_project(app):
    if len (app.soap.get_list_project()) == 0:
        app.project.create(Project(name="Test6"))
    projects = app.soap.get_list_project()
    project = random.choice(projects)
    app.project.delete(project)
    new_project = app.soap.get_list_project()
    projects.remove(project)
    assert projects == new_project

