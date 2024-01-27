FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt-get install -y xpra python3 python3-tk python3-dev python3-pip
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY GPT4GUI.py .
CMD xpra start --start="python3 GPT4GUI.py" --bind-tcp=0.0.0.0:8080 --html=on && tail -f /dev/null