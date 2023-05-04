install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	python3 -m spacy download en_core_web_sm

deploy:
	docker login hapiweb.azurecr.io
	docker build -t fds .
	docker tag fds:latest hapiweb.azurecr.io/fds:latest
	docker push hapiweb.azurecr.io/fds:latest
