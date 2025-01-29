#!/bin/bash
cd cv_backend
pip install --no-cache-dir -r requirements.txt
sh pipeline.sh
gunicorn cv_backend.wsgi:application --log-file -