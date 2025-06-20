from model.project import Project
from urllib.parse import urlparse, parse_qs

class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def get_projects_list(self):
        wd = self.app.wd
        self.open_project_page()
        projects = []
        for element in wd.find_elements_by_css_selector('a[href*="manage_proj_edit_page.php?project_id="]'):
            text = element.text
            href = element.get_attribute("href")
            parsed_url = urlparse(href)
            project_id = parse_qs(parsed_url.query).get("project_id", [None])[0]
            projects.append(Project(id=project_id, name=text))
        #print(projects)
        return projects


    def create(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_xpath("//button[@type='submit']").click()
        wd.find_element_by_id("project-name").click()
        wd.find_element_by_id("project-name").clear()
        wd.find_element_by_id("project-name").send_keys(u"%s" % project.name)
        wd.find_element_by_xpath(u"//input[@value='Добавить проект']").click()


    def delete(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_xpath("//a[contains(@href, 'manage_proj_edit_page.php?project_id=%s')]" % project.id).click()
        wd.find_element_by_xpath("//button[2]").click()
        wd.find_element_by_css_selector("div.alert.alert-warning.center").click()
        wd.find_element_by_xpath(u"//input[@value='Удалить проект']").click()


    def open_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text(u"Управление").click()
        wd.find_element_by_link_text(u"Проекты").click()


