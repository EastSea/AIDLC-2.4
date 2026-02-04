#!/bin/bash

echo "🚀 Table Order Service - 브라우저 테스트 시작"
echo "================================================"
echo ""

# Check if Mock API is running
if curl -s http://localhost:8001/docs > /dev/null 2>&1; then
    echo "✅ Mock API Server: Running on http://localhost:8001"
    echo "   📖 API Docs: http://localhost:8001/docs"
else
    echo "❌ Mock API Server: Not running"
    echo "   Starting Mock API Server..."
    cd "$(dirname "$0")"
    python3 mock/mock-server.py > /tmp/mock-server.log 2>&1 &
    sleep 2
    echo "✅ Mock API Server: Started on http://localhost:8001"
fi

echo ""
echo "🌐 Frontend 서버를 시작합니다..."
echo "   브라우저가 자동으로 열립니다: http://localhost:3000"
echo ""
echo "================================================"
echo "📝 테스트 가이드: BROWSER_TEST_GUIDE.md 참고"
echo "================================================"
echo ""

# Start Frontend
cd web
npm start
