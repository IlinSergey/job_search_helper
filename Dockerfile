FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY anketa.py /app/
COPY bot.py /app/
COPY config.py /app/
COPY data_base.py /app/
COPY hh.py /app/
COPY jobs.py /app/
COPY openai.py /app/
COPY yagpt.py / app/
COPY utils.py /app/

CMD ["python", "bot.py"]
