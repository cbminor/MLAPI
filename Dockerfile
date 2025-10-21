
FROM python:3.12.9


WORKDIR /code


COPY ./requirements.txt /code/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN python -m spacy download en_core_web_sm

COPY ./app /code/app


CMD ["fastapi", "run", "app/main.py", "--port", "80"]