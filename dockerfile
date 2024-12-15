FROM python:3.12-slim

COPY  frontend.py .

RUN pip install flask

EXPOSE 5001
CMD ["python", "frontend.py"]
