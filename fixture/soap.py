from suds.client import Client
from suds import WebFault

from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        web_config = self.app.config['web']
        client = Client(f"{web_config['baseUrl']}/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_list_project(self):
        soap_config = self.app.config['webadmin']
        web_config = self.app.config['web']
        client = Client(f"{web_config['baseUrl']}/api/soap/mantisconnect.php?wsdl")
        projects = client.service.mc_projects_get_user_accessible(soap_config['username'], soap_config['password'])
        projects_list = []
        for project in projects:
            projects_list.append(Project(project.id, str(project.name)))
        return projects_list




