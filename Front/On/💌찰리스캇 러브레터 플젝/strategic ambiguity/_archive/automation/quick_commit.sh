#!/bin/bash
# 🚀 빠른 실행: 전투일지 저장 후 바로 실행
# 사용법: ./quick_commit.sh

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo "🤖 전투일지 자동 커밋..."
echo ""

python3 "$SCRIPT_DIR/auto_commit.py"

echo ""
echo "✅ 완료! GitHub에서 확인하세요."
