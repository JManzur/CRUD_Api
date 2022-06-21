#!/bin/bash
echo "[INFO] Starting CRUD API"
uvicorn app:app --reload --log-config log_conf.yml