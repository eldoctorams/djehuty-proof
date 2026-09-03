FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN python -m pip install --no-cache-dir .
ENTRYPOINT ["djehuty"]
CMD ["samples/report.md", "--sources", "samples/sources", "--output", "/output/audit.json"]
