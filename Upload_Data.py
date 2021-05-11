

import subprocess
import time
import os

commit_message = 'Automtically Committed'
subprocess.call(['git','init'])
subprocess.call(['git', 'add', 'CryptoLocalData\LTC_File_LowDetail.csv'])
subprocess.call(['git', 'commit', '-m', '{}'.format(commit_message)])
subprocess.call(['git','branch', '-M', 'main'])
subprocess.call(['git', 'push','-f','--all', 'https://Your Repository address)])


commit_message = 'Automtically Committed'
subprocess.call(['git','init'])
subprocess.call(['git', 'add', 'CryptoLocalData\LTC_File.csv'])
subprocess.call(['git', 'commit', '-m', '{}'.format(commit_message)])
subprocess.call(['git','branch', '-M', 'main'])
subprocess.call(['git', 'push','-f','--all', 'your repository address')])

time.sleep(5)
os.system('python wait.py')
