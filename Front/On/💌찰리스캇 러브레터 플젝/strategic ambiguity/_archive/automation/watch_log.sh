#!/bin/bash
# 🔍 전투일지 변경 감지 및 자동 커밋
# 사용법: ./watch_log.sh

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
LOG_FILE="$SCRIPT_DIR/../전투일지.md"
PYTHON_SCRIPT="$SCRIPT_DIR/auto_commit.py"

echo "🔍 전투일지 변경 감지 시작..."
echo "📁 모니터링 중: $LOG_FILE"
echo "💡 Ctrl+C로 종료"
echo ""

# 마지막 수정 시간 추적
last_modified=$(stat -f "%m" "$LOG_FILE" 2>/dev/null || stat -c "%Y" "$LOG_FILE" 2>/dev/null)

while true; do
    # 현재 수정 시간
    current_modified=$(stat -f "%m" "$LOG_FILE" 2>/dev/null || stat -c "%Y" "$LOG_FILE" 2>/dev/null)
    
    # 변경 감지
    if [ "$current_modified" != "$last_modified" ]; then
        echo "📝 전투일지 변경 감지! ($(date '+%H:%M:%S'))"
        echo "⏳ 3초 대기 중 (추가 편집을 위해)..."
        sleep 3
        
        echo "🤖 자동 커밋 실행..."
        python3 "$PYTHON_SCRIPT"
        echo ""
        
        last_modified=$current_modified
    fi
    
    # 5초마다 체크
    sleep 5
done
