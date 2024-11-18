FROM telegraf:latest

RUN apt-get update && apt-get install -y python3 python3-pip

COPY requirements.txt /scripts/requirements.txt
RUN pip3 install --no-cache-dir --break-system-packages -r /scripts/requirements.txt

COPY telegraf.conf /etc/telegraf/telegraf.conf
COPY scripts /scripts

RUN chmod +x /scripts/block_delay_ws.py

WORKDIR /scripts

ENTRYPOINT ["telegraf"]