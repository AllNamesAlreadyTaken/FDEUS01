# Agent Supervision Mode Policy

Use this policy for planning and executing tasks with the user.

## Supervision Modes

- `checkpoint`: Work in logical chunks and pause at major milestones for confirmation.
- `tight`: Pause more frequently, confirm before each significant step, and keep the user closely informed.

## Mode Selection Rules

1. Estimate the task length before execution.
2. If the task is more than 5 steps:
	- Ask the user which mode to use: `checkpoint` or `tight`.
	- Do not begin execution until the user chooses a mode.
3. If the task is 5 steps or fewer:
	- Default to `checkpoint` mode automatically.

## Required Prompt For Large Tasks

When a task is more than 5 steps, ask this before starting:

`This task looks like it will take more than 5 steps. Which supervision mode do you want: checkpoint or tight?`

## Fallback Behavior

- If the user does not specify a mode for a more-than-5-step task, ask again once.
- If there is still no answer, do not proceed with execution.
