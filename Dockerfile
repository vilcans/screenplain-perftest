FROM ubuntu

RUN apt-get update && apt-get install -y build-essential libfreetype6-dev python-dev python-imaging python-pip
# Redundant, but improves Docker caching.
ADD screenplain/requirements.txt /
RUN pip install -r /requirements.txt

ADD . /src
ENV PYTHONPATH /src
WORKDIR /src

CMD ["python", "perftest.py"]
