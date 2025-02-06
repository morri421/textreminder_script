import os
# import getpass
# USER_NAME = getpass.getuser()
import datetime
from dotenv import load_dotenv, dotenv_values
from write_startup import add_to_startup

#? Adds script to windows startup
#add_to_startup()

#? Retrieves system date for storage and comparison
now = datetime.datetime.now()
current_date = now.date()
print(current_date)

load_dotenv() 
print(os.getenv("MY_KEY"))

#os.system('start cmd')