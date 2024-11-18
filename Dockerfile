FROM telegraf:latest

# Install Python 3
RUN apt-get update && apt-get install -y python3 python3-pip

# Copy configuration and script files
COPY telegraf.conf /etc/telegraf/telegraf.conf
COPY scripts /scripts

# Set permissions on scripts
RUN chmod +x /scripts/block_delay_ws.py

# Set the working directory
WORKDIR /scripts

# Start Telegraf
ENTRYPOINT ["telegraf"]