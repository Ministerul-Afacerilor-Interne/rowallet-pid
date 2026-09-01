FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends nodejs npm && rm -rf /var/lib/apt/lists/*
RUN npm install -g markdownlint-cli2

WORKDIR /workspace

RUN pip install --no-cache-dir cbor2 cryptography pyyaml requests

CMD ["markdownlint-cli2", "**/*.md"]
