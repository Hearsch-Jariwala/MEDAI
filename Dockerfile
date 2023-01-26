FROM node:15.14.0
LABEL MAINTAINER=sc765@duke.edu
# WORKDIR /FDS-AI-Tool/
# COPY ./FDS-AI-Tool ./

# Install Python
RUN apt update &&\
    apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget &&\
    curl -O https://www.python.org/ftp/python/3.8.12/Python-3.8.12.tgz &&\
    tar -xzf Python-3.8.12.tgz &&\
    cd Python-3.8.12 &&\
    ./configure --enable-optimizations &&\
    make &&\
    make install &&\
    update-alternatives --install /usr/bin/python python /usr/local/bin/python3.8 2

# Install pip
RUN apt install curl -y &&\
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py &&\
    python get-pip.py

RUN cd .. &&\
    rm -rf Python-3.8.12 &&\
    rm Python-3.8.12.tgz

# RUN make install 

# EXPOSE 8888

# CMD ["streamlit", "run", "Home.py", "--server.port", "8888"]