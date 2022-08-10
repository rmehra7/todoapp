FROM python:3.6-stretch
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
ENV PORT 5000
EXPOSE 5000
RUN chmod 777 /app
ENTRYPOINT [ "python" ]
CMD [ "./src/app.py" ]
