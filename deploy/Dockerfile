FROM python:3.8

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && apt install -y netcat vim

RUN adduser yakubov
USER yakubov
WORKDIR /home/yakubov

COPY --chown=yakubov:yakubov requirements.txt requirements.txt

ENV PATH="/home/yakubov/.local/bin:/usr/local/bin:${PATH}"

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY --chown=yakubov:yakubov / /

COPY entrypoint.sh /home/yakubov/
RUN #chmod +x /home/yakubov/entrypoint.sh
ENTRYPOINT ["sh", "/entrypoint.sh"]

#RUN mkdir /code
#WORKDIR /code
#COPY requirements.txt /code/
#RUN pip install -r requirements.txt
## copy entrypoint.sh
##COPY . /code/
#CMD bash /code/deploy/entrypoint.sh
