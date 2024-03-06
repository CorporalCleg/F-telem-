FROM python:3.12-slim

WORKDIR /usr/src/fourier

RUN pip install --no-cache-dir pandas
RUN pip install --no-cache-dir scipy
RUN pip install --no-cache-dir matplotlib