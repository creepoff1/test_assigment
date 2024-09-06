# Базовый образ с Python
FROM python:3.9-slim

# Установка зависимостей для Chrome и ChromeDriver
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    wget \
    xvfb \
    libxi6 \
    libgconf-2-4 \
    && rm -rf /var/lib/apt/lists/*

# Установка конкретной версии Google Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && dpkg -i google-chrome-stable_current_amd64.deb || true \
    && apt-get update \
    && apt-get install -y --no-install-recommends -f \
    && rm google-chrome-stable_current_amd64.deb

# Установка соответствующей версии ChromeDriver
RUN wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip -d /usr/local/bin/ \
    && rm /tmp/chromedriver.zip

# Установка виртуального дисплея для headless-тестов
RUN apt-get update && apt-get install -y xvfb

# Установка зависимостей Python
COPY requirements.txt .
RUN pip install -r requirements.txt

# Копируем проект внутрь контейнера
WORKDIR /app
COPY . /app

# Установка переменной окружения для headless Chrome
ENV DISPLAY=:99

# Запуск Xvfb перед запуском тестов
CMD ["sh", "-c", "Xvfb :99 -screen 0 1920x1080x16 & pytest"]