install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	python3 -m spacy download en_core_web_sm

deploy:
	docker login fluiddatastream.azurecr.io
	docker build -t fds .
	docker tag fds:latest fluiddatastream.azurecr.io/fds:latest
	docker push fluiddatastream.azurecr.io/fds:latest