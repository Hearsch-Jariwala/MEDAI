# FDS-No-Code-AI Tool
## Requirements
- Package requirements specified in /FDS-AI-Tool/requirements.txt
- Environment requirements
    - Node.js < 16.0.0
    - Python >= 3.8

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

## Reference
1. [st_ner_annotate](https://github.com/prasadchandan/st_ner_annotate)
