---
name: superpower
description: Unlock extraordinary productivity by combining multiple Codex skills into a single, coordinated workflow. Use when a user wants to accomplish a complex, multi-step goal that spans coding, communication, research, and deployment in one seamless run.
metadata:
  short-description: Multi-skill supercharged workflow orchestrator
---

# Superpower

Orchestrate multiple Codex skills together to accomplish ambitious, multi-step goals in a single coordinated run.

## When to use

- The task requires several distinct skill domains (e.g., research + code + deploy + notify).
- The user wants maximum output with minimum back-and-forth.
- The goal is ambitious enough that a single skill would leave important steps undone.

## Workflow

1. **Understand the goal**
   - Ask the user to describe the end-to-end outcome they want.
   - Identify every distinct sub-task hidden inside that goal.

2. **Map skills to sub-tasks**
   - For each sub-task, select the most appropriate skill from the available catalog.
   - Common combinations:
     - Research spike → `content-research-writer`
     - Code change → native Codex coding
     - Plan → `create-plan`
     - PR review → `gh-address-comments` or `pr-review-ci-fix`
     - CI failure → `gh-fix-ci`
     - Notify team → `connect` (Slack/email)
     - Document result → `notion-knowledge-capture` or `changelog-generator`

3. **Build an execution sequence**
   - Order sub-tasks by dependency (research before code, code before deploy, deploy before notify).
   - Flag any sub-tasks that can run in parallel to save time.

4. **Execute step by step**
   - Run each sub-task using the mapped skill's guidance.
   - After each step, confirm output before proceeding.
   - If a step fails, diagnose and retry before moving on.

5. **Deliver the complete result**
   - Summarize everything accomplished.
   - List any open items or follow-ups the user should know about.

## Tips

- Start with a clear, written goal statement; vague goals produce vague results.
- You don't need all skills installed — the orchestration logic works with whatever is available.
- For very large goals, break them into two or three superpower runs rather than one enormous session.
