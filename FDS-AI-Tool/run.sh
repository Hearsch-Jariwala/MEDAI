#! /bin/bash


mkdir data
mkdir data/db
export OPENAI_API_KEY=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
mongod --dbpath data/db &
streamlit run Home.py --server.port 8888 --server.maxUploadSize 16
