FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade setuptools
RUN pip install --no-cache-dir -r requirements.txt

COPY data_base/ /app/data_base/
COPY migrations/ /app/migrations/
COPY services /app/services/
COPY utils /app/utils/
COPY alembic.ini /app/
COPY bot.py /app/

CMD ["python", "bot.py"]
