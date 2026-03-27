# Quiz AR Project

## Description

Application de quiz contrôlée par hand tracking (AR).

## Installation

### 1. Cloner le projet

git clone https://github.com/ton-username/quiz-ar-project.git

### 2. Installer les dépendances

#### Vision

cd vision
pip install -r requirements.txt

#### Web

cd ../web
pip install -r requirements.txt

## Lancer le projet

### 1. Lancer le hand tracking

cd vision
python hand_tracking.py

### 2. Lancer le serveur web

cd ../web
python app.py

## Accès

http://127.0.0.1:5000
