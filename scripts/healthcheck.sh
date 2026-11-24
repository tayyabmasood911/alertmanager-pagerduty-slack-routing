#!/usr/bin/env bash
set -euo pipefail

ALERTMANAGER_HOST="${ALERTMANAGER_HOST:-localhost}"
ALERTMANAGER_PORT="${ALERTMANAGER_PORT:-9093}"
ENDPOINT="http://${ALERTMANAGER_HOST}:${ALERTMANAGER_PORT}/-/healthy"

echo "[*] Checking Alertmanager health status at ${ENDPOINT}..."
STATUS_CODE=$(curl -s -o /dev/null -w "%{http_code}" "${ENDPOINT}" || true)

if [ "${STATUS_CODE}" -eq 200 ]; then
  echo "[OK] Alertmanager service is healthy and routing alerts."
  exit 0
else
  echo "[ERROR] Alertmanager healthcheck failed with HTTP status ${STATUS_CODE}."
  exit 1
fi
