FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /opt/webapp
ADD requirements.txt /opt/webapp/
RUN pip install -r /opt/webapp/requirements.txt
ADD app/ /opt/webapp/
WORKDIR /opt/webapp/