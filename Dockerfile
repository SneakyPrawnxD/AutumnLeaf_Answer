FROM python:3.8

RUN pip install --upgrade pip
RUN pip install requests
RUN pip install python-dotenv 

COPY Main2.py .
ENV site=http://api.open-notify.org/astros.json
ENV times=5

CMD [ "python", "./Main2.py"]
