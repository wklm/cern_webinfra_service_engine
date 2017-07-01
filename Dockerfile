FROM python

ADD . /engine

WORKDIR /engine

RUN pip install --upgrade --quiet pip && \
    pip install -r requirements.txt && \
    pip install -e .

ENTRYPOINT python cern_webinfra_service_engine/cli.py
