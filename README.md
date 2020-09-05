
# ejudge-kit

## Configuration
First of all, in root directory of repository, there is `example.config.yml` file. You need to copy it into `config.yml`:
```bash
cp example.config.yml config.yml
```
This file contains required configuration dependent on contest. 
## /get-inside
To get inside, solve first problem inside `Source.cpp` and place your RSA-key instead of `my-rsa-key`. Then just hand over this problem and you will have acces to server with `ejudge` user.

After that, you will have to connect to the server and clean up your source file you handed.

## /gain-tests 

1. Copy configuration file (optional):
```bash
cp example.env.yml env.yml
```
2. Edit your configurations (optional):
```bash
nano env.yml
```
3. Run `gain.py`:
```
python3 gain.py
```
All gained tests will be inside `problems` folder.

## /gain-statements
1. Copy configuration file (optional):
```bash
cp example.env.yml env.yml
```
2. Edit your configurations (optional):
```bash
nano env.yml
```
3. Run `gain.py`:
```
python3 gain.py
```
All gained statements will be inside `statements` folder.

## /testing
To conveniently use gained tests, you can use this testing package.
First of all, copy whole `testing` directory somewhere else:
```
cp -r ./testing/ ~/Desktop/problems/A/
cd ~/Desktop/problems/A/testing/
```
1. Copy configuration file (optional):
```bash
cp example.env.yml env.yml
```
2. Configure your testing environment (optional):
```bash
nano env.yml
```
3. Copy all gained tests for this particular problem into `tests` directory.
4. Compile your source file and run tests:
```bash
g++ -o a.out Source.cpp
python3 tests.py
```
If tests passed, you will see `OK` message, else expected and actual values will be shown.

