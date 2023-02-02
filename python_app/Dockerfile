FROM python

WORKDIR /usr/app

COPY . /usr/app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

EXPOSE 8001

CMD ["python3", "app.py"]
