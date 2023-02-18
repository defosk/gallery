1. pip3 install -r requirements.txt
2. edit `config.py` file and set `IMAGE_DIR`
3. run from src folder: `uvicorn run:app --host 0.0.0.0 --workers={NUM_KERNEL+1}`
4. browse at: `{SERVER_IP}:8000`
