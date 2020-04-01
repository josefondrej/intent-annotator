FROM python:3

MAINTAINER Your Name "josef.ondrej@outlook.com"

RUN apt-get update -y

RUN mkdir /app
RUN mkdir /app/intent-annotator
WORKDIR /app/intent-annotator
COPY intent_annotator /app/intent-annotator/intent_annotator
COPY requirements.txt /app/intent-annotator/requirements.txt

RUN pip3 install -r /app/intent-annotator/requirements.txt

ENV FLASK_APP=/app/intent-annotator/intent_annotator/web/app.py
EXPOSE 5000

ENTRYPOINT ["/bin/bash", "-c"]
CMD ["python3 -m flask run --host=0.0.0.0"]