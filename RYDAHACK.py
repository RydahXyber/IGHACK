import os
if __name__ == "__main__":
   try:
       __import__("RYDAHACK").login_kamu()
   except Exception as e:
       exit(str(e))
