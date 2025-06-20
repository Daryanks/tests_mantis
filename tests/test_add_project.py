from model.project import Project


def test_add_project(app):
    projects = app.project.get_projects_list()
    project = Project(name="Test3")
    app.project.create(project)
    new_projects = app.project.get_projects_list()
    projects.append(project)
    assert sorted(projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)