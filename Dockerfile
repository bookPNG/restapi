FROM python:3.9.5
COPY .  /app
WORKDIR /app
RUN pip3 install flask
RUN pip3 install waitress
RUN pip3 install requests
EXPOSE  5100
CMD ["python3", "app.py"]
