FROM python:3.11.2-alpine 

WORKDIR /app

COPY . ./app

RUN pip install -r app/requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "app/app.py" ]