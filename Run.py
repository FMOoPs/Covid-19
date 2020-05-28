import os
import subprocess
if os.path.exists('WORLD.sqlite'):
    os.remove('WORLD.sqlite')
    print('Old SQLite File Has Been Deleted..')
subprocess.call("scrapper.py", shell=True)
print('Script 1 finished')
subprocess.call("categorizing data.py", shell=True)
print('Script 2 finished')
print('Printing out figures..')
subprocess.call('visualizing.py', shell=True)

