FROM python:3.9
WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install discord
RUN pip install pyyaml
RUN pip install ahk
RUN pip install pysimplegui

CMD ["python3", "main.py"]

