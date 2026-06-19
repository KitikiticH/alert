#!/bin/bash

set -e

echo "=== Обновление системы ==="
sudo apt-get update

echo "=== Установка системных библиотек Chromium ==="
sudo apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    libglib2.0-0 \
    libnss3 \
    libnspr4 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libdbus-1-3 \
    libxcb1 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libasound2t64 \
    libatspi2.0-0 \
    libgtk-3-0 \
    wget \
    curl

echo "=== Создание виртуального окружения ==="
python3 -m venv venv

echo "=== Активация окружения ==="
source venv/bin/activate

echo "=== Обновление pip ==="
pip install --upgrade pip

echo "=== Установка зависимостей проекта ==="
pip install -r requirements.txt

echo "=== Установка Chromium для Playwright ==="
python -m playwright install chromium

echo "=== Проверка установки ==="
python -m playwright --version

echo ""
echo "========================================="
echo "Установка завершена успешно."
echo "Запуск бота:"
echo "source venv/bin/activate"
echo "python main.py"
echo "========================================="