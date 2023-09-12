FROM python:3.11

ENV PYTHONNUNBUFFERED=1

WORKDIR /code

COPY requirement.txt .

RUN pip install -r requirement.txt

COPY . .

EXPOSE 3066


CMD ["python3", "manage.py", "runserver"]