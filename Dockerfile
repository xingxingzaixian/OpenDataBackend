FROM ubuntu:20.04

ADD . /backend

WORKDIR /backend

RUN cp config/sources.list /etc/apt && \
    apt-get update && \
    apt-get install -y vim cron wget && \
    mkdir -p /usr/share/zoneinfo/Asia && \
    rm -f /etc/localtime && \
    cp config/Shanghai /usr/share/zoneinfo/Asia/Shanghai && \
    ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    apt-get -y install python3.8 python3.8-dev && \
    apt-get -y install python3-distutils && \
    apt-get -y install python3-pip && \
    pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && \
    pip3 config set install.trusted-host pypi.tuna.tsinghua.edu.cn && \
    python3 -m pip install pipenv && \
    pipenv install && \
    apt-get -y autoremove && \
    apt-get -y autoclean  && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 7654

ENTRYPOINT ["pipenv", "run", "dev"]