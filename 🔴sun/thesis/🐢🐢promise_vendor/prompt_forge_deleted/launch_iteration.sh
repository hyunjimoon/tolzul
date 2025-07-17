#!/bin/bash
# 🚀 Launch Master Prompt Iteration

# Creates timestamped iteration folder and prepares evaluation templates

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
ITERATION_NUM=$(ls -1 iterations | wc -l | xargs)
NEXT_ITERATION=$((ITERATION_NUM + 1))
ITERATION_DIR="iterations/iteration_$(printf "%03d" $NEXT_ITERATION)_$TIMESTAMP"

echo "🎯 Creating iteration folder: $ITERATION_DIR"
mkdir -p "$ITERATION_DIR"

# Copy evaluation template
cp "📊evaluation_tracker.md" "$ITERATION_DIR/evaluation.md"

# Create response folders
mkdir -p "$ITERATION_DIR/responses"
touch "$ITERATION_DIR/responses/claude_response.md"
touch "$ITERATION_DIR/responses/chatgpt_response.md"
touch "$ITERATION_DIR/responses/gemini_response.md"

# Create iteration log
cat > "$ITERATION_DIR/iteration_log.md" << EOF
# Iteration #$NEXT_ITERATION - $TIMESTAMP

## Task Tested
[Fill in the specific task/concept tested]

## Deployed Prompt
\`\`\`
[Paste the exact prompt used]
\`\`\`

## Three Holes Identified
1. **Hole #1**: 
   - Evidence: 
   - Fix: 

2. **Hole #2**: 
   - Evidence: 
   - Fix: 

3. **Hole #3**: 
   - Evidence: 
   - Fix: 

## Master Prompt Updates
- [ ] Update 1: 
- [ ] Update 2: 
- [ ] Update 3: 

## Lessons Learned
- 

## Next Focus
- 
EOF

echo "✅ Iteration folder created!"
echo "📋 Next steps:"
echo "1. Copy your prompt from 💡master_prompt_template.md"
echo "2. Deploy to all three AIs"
echo "3. Save responses in $ITERATION_DIR/responses/"
echo "4. Fill out $ITERATION_DIR/evaluation.md"
echo "5. Complete $ITERATION_DIR/iteration_log.md"
echo "6. Update 💡master_prompt_template.md with improvements"

# Open the iteration folder (macOS)
open "$ITERATION_DIR"
