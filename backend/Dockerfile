FROM --platform=linux/amd64 python:3.12-slim

# Switch to new user "herop"
RUN useradd -m herop
USER herop
ENV PATH="/home/herop/.local/bin:$PATH"
WORKDIR /home/herop

VOLUME /home/explorer

# Setup Python app
COPY --chown=herop:herop . .
RUN pip3 install . --no-cache-dir
