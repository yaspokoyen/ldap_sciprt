FROM python:3.9.7-alpine3.14

RUN apk update && apk upgrade && apk add bash
WORKDIR /home/app
COPY ldap.py /home/app/
RUN pip install ldap3
ENTRYPOINT ["python", "/home/app/ldap.py"]