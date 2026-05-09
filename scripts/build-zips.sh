#!/usr/bin/env bash
# Rebuilds the claude.ai upload bundles from the canonical SKILL.md sources.
# Each skill directory under skills/ becomes one zip in dist/, with SKILL.md at the archive root.
# Run from anywhere — script resolves its own paths.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PLUGIN_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SKILLS_DIR="$PLUGIN_ROOT/skills"
DIST_DIR="$PLUGIN_ROOT/dist"

mkdir -p "$DIST_DIR"

# Wipe old zips so deleted skills don't linger.
rm -f "$DIST_DIR"/*.zip

cd "$SKILLS_DIR"
count=0
for skill in */; do
  skill_name="${skill%/}"
  (cd "$skill_name" && zip -rq "$DIST_DIR/${skill_name}.zip" . -x "*.DS_Store")
  echo "  built ${skill_name}.zip"
  count=$((count + 1))
done

echo ""
echo "Built $count skill bundles → $DIST_DIR"
