# FDS-No-Code-AI Tool
## Requirements
- Package requirements specified in /FDS-AI-Tool/requirements.txt
- Environment requirements
    - Node.js < 16.0.0

## Environment setup
### Backend
```shell
cd MEDAI/FDS-AI-Tool
make install
```

### Frontend
```shell
cd MEDAI/FDS-AI-Tool/frontend
npm install
npm run build
```

## Access
- run backend
```shell
cd MEDAI/FDS-AI-Tool
streamlit run Home.py
```

- run frontend
```shell
cd MEDAI/FDS-AI-Tool/frontend
npm start
```

Then the webpage can be accessed through http://172.17.0.2:8501