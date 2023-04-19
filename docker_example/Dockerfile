FROM registry.access.redhat.com/ubi8/python-38

USER root

RUN mkdir /vdsml
WORKDIR /vdsml

COPY vdsml.py /vdsml
COPY requirements.txt /vdsml

RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

CMD ["python", "vdsml.py"]