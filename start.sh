#!/bin/bash
pip install --no-cache-dir -r /cv_backend/cv_backend/requirements.txt
gunicorn cv_backend.cv_backend.wsgi:application --log-file -