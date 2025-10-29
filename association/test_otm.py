import one_to_many as otm
def test_one_to_many():
    proj = otm.Project("proj1")
    issue = otm.Issue() # create a new issue
    proj.add_issue(issue) # add issue to the project
    print(issue.project.name) # print the project nam via issue
