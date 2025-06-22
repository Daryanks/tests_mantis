from model.project import Project


def test_add_project(app):
    projects = app.soap.get_list_project()
    project = Project(name="Test5")
    app.project.create(project)
    new_projects = app.soap.get_list_project()
    projects.append(project)
    assert projects == new_projects