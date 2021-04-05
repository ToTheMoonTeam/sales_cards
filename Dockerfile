FROM python:3.8-slim-buster

WORKDIR /sales_cards

COPY requirements.txt requirements.txt
CMD ["python3", "-m", "venv", "env"]

CMD ["source", "env/bin/activate"]
RUN pip3 install -r requirements.txt

COPY . .
ENV FLASK_APP sales_cards/app.py
CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0"]
