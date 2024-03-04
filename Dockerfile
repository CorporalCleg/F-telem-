FROM python:3.12-slim

WORKDIR /usr/src/fourier

RUN pip install pandas
RUN pip install scipy
RUN pip install matplotlib