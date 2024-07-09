FROM ubuntu:latest

# Install necessary libraries
RUN apt-get update && apt-get install -y \
    libc6 \
    libstdc++6 \
    && rm -rf /var/lib/apt/lists/*

# Copy the IfcConvert executable to the container
COPY IfcConvert /usr/local/bin/IfcConvert

# Set the entrypoint to allow dynamic command execution
ENTRYPOINT ["/usr/local/bin/IfcConvert"]
