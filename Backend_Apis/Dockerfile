FROM python:3.7-slim

RUN apt-get update && apt-get install -y python3-dev
RUN mkdir -p /usr/src/
WORKDIR /usr/src/

# Installing requirements
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

# Adding remaining files
ADD . .

ENV PYTHONPATH "${PYTHONPATH}:/usr/src/"

CMD ["python","./app/main.py"]
