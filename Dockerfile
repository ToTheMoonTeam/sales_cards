FROM python:3.7-slim

WORKDIR /sales_cards
COPY  . /sales_cards

COPY web/requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt



ENTRYPOINT ["python web/app.py"]
