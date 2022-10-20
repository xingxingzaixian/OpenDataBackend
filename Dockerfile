FROM ubuntu:20.04

ENV DB_HOST localhost
ENV DB_PORT 5432
ENV DB_NAME opendata
ENV DB_NAME root
ENV DB_PASSWD 123456
ENV QINIU_AK Jx3wQMD1
ENV QINIU_SK d68397c4fb671bc024e24e1964b067cc35388818
ENV QINIU_BUCKET data
ENV QINIU_URL http://image.xingxingzaixian.fun/

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
    apt-get -y autoremove && \
    apt-get -y autoclean  && \
    rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install pipenv && pipenv install

EXPOSE 7654

ENTRYPOINT ["pipenv", "run", "dev"]