
FROM python:3.12.9


WORKDIR /code


COPY ./requirements.txt /code/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Install and Download NLTK Stopwords
RUN python -m nltk.downloader -d /usr/local/share/nltk_data wordnet omw-1.4
ENV NLTK_DATA=/usr/local/share/nltk_data


COPY ./app /code/app


CMD ["fastapi", "run", "app/main.py", "--port", "80"]