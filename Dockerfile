FROM python:3.8

WORKDIR /app

COPY script.py /app/

RUN pip install requests beautifulsoup4

CMD ["python", "script.py"]
