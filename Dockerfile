FROM shunianchen/venture:base
LABEL MAINTAINER=sc765@duke.edu

WORKDIR /FDS-AI-Tool/
COPY ./FDS-AI-Tool ./
COPY ./Makefile ./
COPY ./requirements.txt ./

RUN make install &&\
    chmod +x run.sh &&\
    sed -i 's/\r$//' run.sh

EXPOSE 8888 6006

CMD ["bash", "run.sh"]
