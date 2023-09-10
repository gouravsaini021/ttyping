FROM ubuntu:22.04

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt ./

RUN apt update && apt -y upgrade && apt install python3.10 -y && apt install python3-pip -y  && apt install python3-venv -y

RUN python3 -m venv venv

RUN . venv/bin/activate

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "python3" ]

CMD ["main.py" ]