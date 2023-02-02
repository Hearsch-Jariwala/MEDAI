#! /bin/bash


mkdir data
mkdir data/db
mongod --dbpath data/db &
streamlit run Home.py --server.port 8888 --server.maxUploadSize 16 &
cd frontend
npm start