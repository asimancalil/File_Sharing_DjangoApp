FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/



#FROM python:3.8-alpine
#ENV PYTHONUNBUFFERED=1
#
#COPY .requirements.txt /requirements.txt
#RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
#RUN pip install -r /requirements.txt
#RUN apk del .tmp -d
#RUN mkdir /app
#COPY .app /app
#WORKDIR /app
#COPY ./scripts /scripts
#
#RUN chmod +x /scripts/*
#
#RUN mkdir -p /vol/web/media
#RUN mkdir -p /vol/web/
#
#RUN adduser -D user
#RUN chown -R user:user /vol
#RUN chmod -R 755 /vol/web
#
#USER user
#
#CMD ["entrypoint.sh"]
#
