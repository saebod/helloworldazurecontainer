import time
from dotenv import load_dotenv
load_dotenv()
import os
name = os.environ.get("NAME")
for i in range(1,4):
    print(f"Hello {name} {i}")
    time.sleep(1)
