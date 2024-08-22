FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV WORK_DIR /src

RUN apt-get -y update && apt-get -y upgrade

RUN python -m pip install --no-cache-dir --upgrade pip

COPY ../alembic.ini ${WORK_DIR}/alembic.ini

COPY ../requiremets.txt ${WORK_DIR}/requirements.txt

RUN pip install -r ${WORK_DIR}/requirements.txt

COPY ../src ${WORK_DIR}/src

WORKDIR ${WORK_DIR}
