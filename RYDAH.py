import os
if __name__ == "__main__":
   try:
       __import__("RYDAH").login_kamu()
   except Exception as e:
       exit(str(e))
