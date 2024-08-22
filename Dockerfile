FROM python
COPY . /app/
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD ["python3", "-m", "flask", "--app", "app", "run", "--host=0.0.0.0", "--port=8080"]