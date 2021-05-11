

import subprocess
import time
import os

commit_message = 'Automtically Committed'
subprocess.call(['git','init'])
subprocess.call(['git', 'add', 'CryptoLocalData\LTC_File_LowDetail.csv'])
subprocess.call(['git', 'commit', '-m', '{}'.format(commit_message)])
subprocess.call(['git','branch', '-M', 'main'])
subprocess.call(['git', 'push','-f','--all', 'https://Mackenzie1215:Mack12231998@github.com/Mackenzie1215/Crypto'.format('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')])


commit_message = 'Automtically Committed'
subprocess.call(['git','init'])
subprocess.call(['git', 'add', 'CryptoLocalData\LTC_File.csv'])
subprocess.call(['git', 'commit', '-m', '{}'.format(commit_message)])
subprocess.call(['git','branch', '-M', 'main'])
subprocess.call(['git', 'push','-f','--all', 'https://Mackenzie1215:Mack12231998@github.com/Mackenzie1215/Crypto'.format('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')])

time.sleep(5)
os.system('python wait.py')