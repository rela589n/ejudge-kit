import yaml
import os

config = yaml.safe_load(open("./env.yml"))
locals().update(config)

contestId = ('000000' + str(contestId))[-6:]

for problem in problems:   
    builtSource = paths['source'].format(contest=contestId, problem=problem)
    builtConnection = connection.format(user=userName, host=hostName, source=builtSource)
    destination = paths['destination'].format(problem=problem) 
    
    if onlyNotFound and os.path.exists(destination):
        continue
    
    executable = command.format(connection=builtConnection, destination=destination)

    print(executable)
    os.system(executable)

# or use just `scp -r ejudge@198.43.26.28:/home/judges2/000123/problems/ ./`
