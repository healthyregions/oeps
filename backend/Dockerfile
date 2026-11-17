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

ENV FLASK_APP=oeps
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8080"]
