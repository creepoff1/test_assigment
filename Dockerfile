FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    wget \
    xvfb \
    libxi6 \
    libgconf-2-4 \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && dpkg -i google-chrome-stable_current_amd64.deb || true \
    && apt-get install -f \
    && rm google-chrome-stable_current_amd64.deb


RUN CHROME_VERSION=$(google-chrome --version | grep -oP '\d+\.\d+\.\d+') && \
    wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/$CHROME_VERSION/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
    rm /tmp/chromedriver.zip

RUN apt-get update && apt-get install -y xvfb

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app
COPY . /app

ENV DISPLAY=:99

CMD ["sh", "-c", "Xvfb :99 -screen 0 1920x1080x16 & pytest"]