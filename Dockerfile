FROM python:3.8.3-alpine

WORKDIR /src

ENV FLASK_APP index.py

COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

# CMD ["flask", "run"]
