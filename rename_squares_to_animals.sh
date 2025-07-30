#!/bin/bash
# Edge Commons 파일명 변경 스크립트

cd "/Users/hyunjimoon/MIT Dropbox/Angie.H Moon/tolzul/🔴sun/thesis/📜"

# 🟧 → 🐅 변경
for file in 📜🟧_*.md; do
    if [ -e "$file" ]; then
        newname="${file/🟧/🐅}"
        mv "$file" "$newname"
        echo "변경: $file → $newname"
    fi
done

# 🟩 → 🐢 변경
for file in 📜🟩_*.md; do
    if [ -e "$file" ]; then
        newname="${file/🟩/🐢}"
        mv "$file" "$newname"
        echo "변경: $file → $newname"
    fi
done

# 🟪 → 👾 변경
for file in 📜🟪_*.md; do
    if [ -e "$file" ]; then
        newname="${file/🟪/👾}"
        mv "$file" "$newname"
        echo "변경: $file → $newname"
    fi
done

echo "모든 파일 변경 완료!"