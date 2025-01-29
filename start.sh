#!/bin/bash
cd cv_backend
pip install --no-cache-dir -r requirements.txt
sh pipeline.sh
cd ..
gunicorn cv_backend.cv_backend.wsgi:application --log-file -