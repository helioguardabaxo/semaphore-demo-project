# import sys

# name = str(sys.argv[1])

# print('Hello, {0}! Welcome to Semaphore with Python!'.format(name))

import json
import sys

cmdstr = dict(json.loads(sys.argv[1].replace("'", '"'))) 
print(json.dumps(cmdstr))