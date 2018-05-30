FROM python:3.6.5-slim

RUN mkdir /app

WORKDIR /app

ADD requirement.txt .

RUN pip install -r requirement.txt

ADD . .

EXPOSE 80


<<<<<<< HEAD
CMD ["gunicorn", "flaskblog:app", "-b", "0.0.0.0:80", "--workers", "4", "--reload"]
=======
CMD ["gunicorn", "flask_blog:app", "-b", "0.0.0.0:80", "--workers", "4", "--reload"]
>>>>>>> 46565f3b3981b52e57684b7c301c7bb5a0813d8a
