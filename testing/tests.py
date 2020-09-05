import os
import subprocess
import yaml
from shutil import copyfile

if not os.path.isfile('./env.yml'):
  copyfile('./example.env.yml', './env.yml')

config = yaml.safe_load(open("./env.yml"))

executable = config['executable']
testsDir = config['testsDirectory']
inputExtension = config['inputExtension']
outputExtension = config['outputExtension']


class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'

allFiles = [os.path.join(testsDir, f) for f in os.listdir(testsDir)]

inputFiles = [f for f in allFiles if os.path.splitext(f)[1] == inputExtension]
outputFiles = [f for f in allFiles if os.path.splitext(f)[1] == outputExtension]

if len(inputFiles) != len(outputFiles):
  # not all input files have output or vice versa
  exit(-1)

inputFiles.sort()
outputFiles.sort()

for (inp, out) in zip(inputFiles, outputFiles):
  handle = open(inp, mode='r')
  procInp = handle.read()
  handle.close()

  result = subprocess.run(executable, stdout=subprocess.PIPE, input=procInp.encode('utf-8')) 
  result = result.stdout.decode('utf-8')
  
  handle = open(out, mode='r')
  expected = handle.read()
  handle.close()
  
  if expected != result:
    print(f'{bcolors.FAIL}{bcolors.UNDERLINE}Test {inp} failed!{bcolors.ENDC}')
    print('Expected: \n```')
    print(expected)
    print('```\nActual: \n```')
    print(result)
    print('```')
    exit(-1)

print(f'{bcolors.OKBLUE}{bcolors.BOLD}OK{bcolors.ENDC}')

