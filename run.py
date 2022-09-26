import os
if __name__ == "__main__":
   try:
       os.system("git pull")
       __import__("NewIGproRyd").login_kamu()
   except Exception as e:
       exit(str(e))
