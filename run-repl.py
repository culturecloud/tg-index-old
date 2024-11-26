import os
import runpy
import requests
from dotenv import load_dotenv

load_dotenv()

os.system("alias python3=python")

def is_alive():
  repl_slug = os.environ.get("REPL_SLUG")
  repl_owner = os.environ.get("REPL_OWNER")
  try:
    resp = requests.get(f"https://{repl_slug}.{repl_owner}.repl.co", timeout=15)
  except Exception as e:
    print("Server response wait timed out!")
    return False
  return resp.ok

def run_setup():
    if not is_alive():
        print("Starting a new instance...")
        def alert(missing):
            print(
                f"\nCopy your {missing} and save it into Secrets (Environment variables) Sidebar!\n"
            )
        req_env_vars = ["API_ID", "API_HASH", "INDEX_SETTINGS"]
        for env_var in req_env_vars:
            env_value = os.getenv(env_var)
            if env_value is None:
                alert(env_var)
                return
        if os.getenv("SESSION_STRING") is None:
            print("Generating session string ...")
            os.system("python app/genss.py")
            return
        os.system("python -m app")
    else:
        print("Server is already running...")


if __name__ == "__main__":
    run_setup()
