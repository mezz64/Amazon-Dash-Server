FROM python:3.6

EXPOSE 443

# Copy files into image
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . .

# Start server
RUN chmod +x /usr/src/app/dockerStart.sh
CMD [ "python", "dash_server.py" ]
