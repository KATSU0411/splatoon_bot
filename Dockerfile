FROM python:3.9
WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install discord
RUN pip install pyyaml
RUN pip install ahk
RUN pip install pysimplegui
RUN pip install mss
RUN pip install ctypes

CMD ["python3", "src/main.py"]

