#!/usr/bin/env bash
# Reset the PatchPilot demo repo to its "broken" state so the demo can be re-run.
#
# Closes any PR the agent opened, deletes its branches, and restores pricing.py
# to the off-by-one bug. Safe to run repeatedly; run it before every take.
set -euo pipefail

REPO="${DEMO_REPO:-sualharun/patchpilot-demo}"

echo "==> Closing open pull requests on $REPO"
for pr in $(gh pr list --repo "$REPO" --state open --json number --jq '.[].number'); do
  gh pr close "$pr" --repo "$REPO" --delete-branch >/dev/null 2>&1 || true
  echo "    closed PR #$pr"
done

echo "==> Deleting leftover agent branches"
for br in $(gh api "repos/$REPO/branches" --jq '.[].name' | grep '^agent/' || true); do
  gh api -X DELETE "repos/$REPO/git/refs/heads/$br" >/dev/null 2>&1 || true
  echo "    deleted $br"
done

echo "==> Restoring the bug on main"
sha=$(gh api "repos/$REPO/contents/pricing.py" --jq '.sha')
current=$(gh api "repos/$REPO/contents/pricing.py" --jq '.content' | base64 -d)

if grep -q 'quantity > BULK_THRESHOLD' <<<"$current"; then
  echo "    already in the broken state, nothing to do"
else
  fixed=$(sed 's/if quantity >= BULK_THRESHOLD:/if quantity > BULK_THRESHOLD:/' <<<"$current")
  gh api -X PUT "repos/$REPO/contents/pricing.py" \
    -f message="Revert bulk discount threshold for demo reset" \
    -f content="$(base64 <<<"$fixed" | tr -d '\n')" \
    -f sha="$sha" >/dev/null
  echo "    pricing.py reverted to the off-by-one bug"
fi

echo "==> Reopening the demo issue if it was closed"
state=$(gh issue view 1 --repo "$REPO" --json state --jq '.state')
if [[ "$state" == "CLOSED" ]]; then
  gh issue reopen 1 --repo "$REPO" >/dev/null
  echo "    reopened issue #1"
fi

echo
echo "Demo repo is ready: https://github.com/$REPO/issues/1"
