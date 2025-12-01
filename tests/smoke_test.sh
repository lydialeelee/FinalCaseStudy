#!/bin/bash

echo "Running smoke test..."

# Test health endpoint
HEALTH_RESPONSE=$(curl -s http://localhost:8080/health)

if [[ "$HEALTH_RESPONSE" != *"ok"* ]]; then
  echo "Health endpoint failed"
  exit 1
fi

# Test tip endpoint
TIP_RESPONSE=$(curl -s -X POST http://localhost:8080/tip \
  -H "Content-Type: application/json" \
  -d '{"total_bill": 50, "tip": 10}')

if [[ "$TIP_RESPONSE" != *"0.2"* ]]; then
  echo "Tip endpoint failed"
  exit 1
fi

echo "Smoke test passed!"
exit 0
