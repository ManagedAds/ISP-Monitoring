FROM python:3.6

WORKDIR /usr/src/app
COPY ./monitoring/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python", "-u", "./monitoring/run.py" ]
