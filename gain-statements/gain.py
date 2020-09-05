import yaml
import os
from shutil import copyfile

globalConfig = yaml.safe_load(open("../config.yml"))

userName = globalConfig['userName']
hostName = globalConfig['hostName']
contestId = ('000000' + str(globalConfig['contestId']))[-6:]
connectionTemplate = globalConfig['connection']

if not os.path.isfile('./env.yml'):
  copyfile('./example.env.yml', './env.yml')

config = yaml.safe_load(open("./env.yml"))

sourceTemplate = config['paths']['source']
destination = config['paths']['destination']

commandTemplate = config['command']

sourcePath = sourceTemplate.format(contest=contestId)
connection = connectionTemplate.format(user=userName, host=hostName, sourcePath=sourcePath)

command = commandTemplate.format(connection=connection, destination=destination)

print(command)
os.system(command)
# or use just `scp -pr ejudge@198.43.26.28:/home/judges2/000123/problems/ ./`
