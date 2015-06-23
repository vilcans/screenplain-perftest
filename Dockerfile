FROM ubuntu

RUN apt-get update && apt-get install -y build-essential libfreetype6-dev python-dev python-imaging python-pip
ADD screenplain/requirements.txt /requirements.txt    # Redundant, but improves Docker caching.
RUN pip install -r /requirements.txt

ADD . /src
ENV PYTHONPATH /src
WORKDIR /src

CMD ["python", "perftest.py"]
