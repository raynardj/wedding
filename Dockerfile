FROM python:3.6.10-stretch
WORKDIR /root
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8080
COPY wed /root/wed

RUN ln -s /root/wed /usr/local/lib/python3.6/site-packages/wed

CMD python wed/run.py