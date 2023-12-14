from uvicorn import run
import os

if __name__ == '__main__':
    run("src.app:app", port=8000, reload=True)
