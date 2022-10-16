FROM python:3.9.15-slim-buster
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN  apt-get update && apt-get install ffmpeg libsm6 libxext6 tesseract-ocr -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /app/
ENTRYPOINT [ "python" ]
CMD ["app.py" ]