class Issue:
    def __init__(self):
        self.project = None

    def set_project(self, project):
        self.project = project

# one project can have many issues
class Project:
    def __init__(self, name=""):
        self.issues = []
        self.name = name
        

    def add_issue(self, issue: Issue):
        self.issues.append(issue)
        issue.set_project(self) # pass project object to set it in the issue object