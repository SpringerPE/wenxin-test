import os
from lib.app import app

myport = os.getenv("PORT")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=myport)