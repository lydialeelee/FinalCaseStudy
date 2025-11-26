#!/usr/bin/env bash
set -e

echo "Starting app..."
python3 src/app.py &

APP_PID=$!
sleep 2

echo "Running smoke test..."
response=$(curl -s -X POST http://localhost:8080/tip \
    -H "Content-Type: application/json" \
    -d '{"total_bill": 50, "tip": 10}')

echo "Response: $response"

echo "$response" | grep -q '"tip_pct": 0.2'

echo "Smoke test passed!"
kill $APP_PID
