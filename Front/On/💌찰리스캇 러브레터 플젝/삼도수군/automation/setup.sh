#!/bin/bash
# 🔧 자동화 시스템 설치 스크립트
# 한 번만 실행하세요

echo "🔧 전투일지 자동화 시스템 설치 중..."
echo ""

# 현재 디렉토리 확인
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo "📁 설치 경로: $SCRIPT_DIR"

# 실행 권한 부여
echo "🔑 실행 권한 부여 중..."
chmod +x "$SCRIPT_DIR/quick_commit.sh"
chmod +x "$SCRIPT_DIR/watch_log.sh"

# Python 확인
echo ""
echo "🐍 Python 확인 중..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo "✅ $PYTHON_VERSION 발견"
else
    echo "❌ Python 3가 설치되어 있지 않습니다."
    echo "   설치: brew install python3"
    exit 1
fi

# Git 확인
echo ""
echo "📦 Git 확인 중..."
if command -v git &> /dev/null; then
    GIT_VERSION=$(git --version)
    echo "✅ $GIT_VERSION 발견"
else
    echo "❌ Git이 설치되어 있지 않습니다."
    exit 1
fi

# Git 설정 확인
echo ""
echo "⚙️  Git 설정 확인 중..."
GIT_NAME=$(git config user.name)
GIT_EMAIL=$(git config user.email)

if [ -z "$GIT_NAME" ] || [ -z "$GIT_EMAIL" ]; then
    echo "⚠️  Git 사용자 정보가 설정되어 있지 않습니다."
    echo "   다음 명령어로 설정하세요:"
    echo "   git config --global user.name \"Your Name\""
    echo "   git config --global user.email \"your@email.com\""
else
    echo "✅ Git 사용자: $GIT_NAME <$GIT_EMAIL>"
fi

# 테스트 실행
echo ""
echo "🧪 테스트 실행 중..."
python3 "$SCRIPT_DIR/auto_commit.py"

# 완료
echo ""
echo "✅ 설치 완료!"
echo ""
echo "📚 사용법:"
echo "   1. 즉시 커밋: ./quick_commit.sh"
echo "   2. 자동 감지: ./watch_log.sh"
echo ""
echo "📖 자세한 내용: README.md 참고"
