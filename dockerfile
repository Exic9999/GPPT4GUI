FROM python:3.10.13-alpine3.19
WORKDIR /app

COPY requirements.txt gpt4web.py ./
COPY templates ./templates
RUN pip install -r ./requirements.txt
RUN pip install gunicorn
ENV FLASK_ENV production

EXPOSE 5000
CMD ["gunicorn", "-b", ":5000", "--timeout", "90", "gpt4web:app"]