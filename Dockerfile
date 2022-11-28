# FROM ubuntu

# RUN apt update
# RUN apt install python3-pip -y
# RUN pip3 install Flask
# WORKDIR /app
# ENTRYPOINT [ "python3" ]
# COPY . .
# CMD ["/app.py", "python3", "-m", "flask", "run"]

FROM python:3.10-slim-buster
ADD . /app
WORKDIR /app
RUN pip install -r requirement.txt
CMD [ "python", "./myapp.py" ]
# docker build -t flask .    //to build docker image
# docker run -d -p 5000:5000 flask    //to run docker image on port
# 