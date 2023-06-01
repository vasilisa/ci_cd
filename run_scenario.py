import dataikuapi

host   = "http://localhost:12000"
apiKey = "L9hfiTrr8emZaPJIEujuTD47caueRhhu"

# initiate the client 
client = dataikuapi.DSSClient(host,apiKey)

# print(f'{client.list_project_keys()}\n',)
# print(f'{client.list_users()}\n')

projectKey = "CICD"
scenarioID = "GITAUTOMATION"

def run_scenario(projectKey,scenarioID,**kwargs):
    project   = client.get_project(projectKey)
    scenario_ = project.get_scenario(scenarioID)

    try:    
        scenario_.run_and_wait() # initiate the scenario 
        return "Scenario succesful"
    except: 
        raise ValueError("Error running the scenario")
   

run_scenario(projectKey,scenarioID)
