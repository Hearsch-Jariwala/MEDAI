FROM shunianchen/fds:base
LABEL MAINTAINER=sc765@duke.edu

WORKDIR /FDS-AI-Tool/
COPY ./FDS-AI-Tool ./

RUN make install &&\
    chmod +x run.sh &&\
    sed -i 's/\r$//' run.sh

EXPOSE 8888 6006

CMD ["bash", "run.sh"]
