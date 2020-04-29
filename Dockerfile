FROM python:3.7.7-buster

RUN pip install --upgrade pip && \
    pip install numpy && \
    pip install scipy && \
    pip install typing && \
    pip install PyPubSub
    
VOLUME /app
COPY . /app
WORKDIR /app
CMD python simulate.py
