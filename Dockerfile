FROM shunianchen/fds:base
LABEL MAINTAINER=sc765@duke.edu

WORKDIR /FDS-AI-Tool/
COPY ./FDS-AI-Tool ./

RUN make install
RUN chmod +x run.sh

EXPOSE 8888 6006

CMD ["bash", "run.sh"]
