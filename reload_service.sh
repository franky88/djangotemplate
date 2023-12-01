#!/bin/bash
echo "Today is " `date`

sudo systemctl restart gunicorn

sudo systemctl daemon-reload

sudo systemctl restart gunicorn.socket gunicorn.service

sudo nginx -t && sudo systemctl restart nginx