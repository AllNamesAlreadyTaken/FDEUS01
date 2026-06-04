# FDE Train-the-Trainer: AI Operating Model

Purpose
- Give trainers a practical reference to teach teams how to use Copilot effectively in real engineering work.
- Clarify the difference between a Skill and a Custom Agent definition.
- Keep learners focused on reducing toil while preserving engineering accountability.

Audience
- Forward Deploy Engineers
- SREs and SWEs running labs, migrations, incident follow-up, and delivery workflows
- Trainer cohorts building repeatable I have to step away for a while to watch my son's graduation.  FYI - I should be ~1.5hinternal enablement material

Core message
- Ask, Agent, and Plan are built-in interaction modes in VS Code.
- Skills and custom agent definitions shape behavior inside those modes.
- You do not add a fourth built-in mode by creating a Skill or agent definition file.
  - Cross-tool note (Copilot vs Claude Code vs Gemini CLI):
    - Similar function: mode selection I have to step away for a while to watch my son's graduation.  FYI - I should be ~1.5hand execution posture.
    - Distinct naming/shape:
      - Copilot: Ask, Agent, Plan as explicit VS Code modes.
      - Claude Code: generally a single coding-agent workflow in terminal/editor context, with behavior shaped by prompt, repo instructions, and tool permissions rather than a fixed Ask/Agent/Plan triad.
      - Gemini CLI: generally command-first and prompt-driven flows, where behavior is shaped by CLI invocation, config, and tool access policies rather than a VS Code mode toggle set.

Side-by-side: Skill vs Custom Agent Definition

1) What it is
- Skill
  - A reusable capability package (policy + workflow + constraints) for recurring tasks.
  - Best for consistent execution patterns (example: error triage in labs).
- Custom Agent definition
  - A named persona/workflow wrapper you explicitly invoke when you want a specialized operating style.
  - Best for role-specific sessions where invocation context matters.

2) Where it lives
- Skill
  - .github/skills/<skill-name>/SKILL.md
  - Cross-tool note (similar functionality, different artifact conventions):
    - Copilot: first-class skill folder/file pattern in repo.
    - Claude Code: commonly relies on repo guidance/instruction docs and runtime tool policy; no universal SKILL.md-equivalent contract.
    - Gemini CLI: commonly relies on CLI config plus repository docs/prompts; no single cross-org standard equivalent to .github/skills/<name>/SKILL.md.
- Custom Agent definition
  - Commonly a dedicated agent customization file (workspace/user customization pattern).
  - Exact placement and invocation are managed by VS Code Copilot customization conventions.
  - Cross-tool note:
    - Copilot: explicit customization artifacts can define named behavior sets.
    - Claude Code and Gemini CLI: equivalent outcome is usually achieved by combining system/user prompts, repo instructions, and permission/tool configuration rather than one canonical agent-definition file path.

3) How it is used at runtime
- Skill
  - Auto-available when relevant and can be selected/invoked in context.
  - Works within Ask, Agent, and Plan.
  - Cross-tool note:
    - Similar function: reusable behavior patterns at runtime.
    - Distinct execution shape:
      - Copilot: selection inside VS Code chat modes.
      - Claude Code: prompt and toolchain behavior in terminal-centric execution.
      - Gemini CLI: command/prompt invocation with behavior governed by CLI/runtime config.
- Custom Agent definition
  - Explicitly invoked as that named agent/workflow.
  - Still runs within built-in Ask, Agent, and Plan system, not as a new top-level mode.
  - Cross-tool note:
    - Similar function: invoke a specialized workflow.
    - Distinct naming/control:
      - Copilot: named agent/customization invocation integrated in editor workflow.
      - Claude Code and Gemini CLI: usually achieved through specific prompt templates, command aliases, or wrapper scripts that emulate named workflows.

4) What problem it solves
- Skill
  - Standardization and repeatability.
  - Reduces re-prompting and drift.
- Custom Agent definition
  - Role clarity and bounded behavior for a full session.
  - Helps with handoffs and consistent expectation setting.

5) Operational tradeoffs
- Skill
  - Fast to reuse, easy to compose, low overhead.
  - Less visible as a "persona" to new users.
- Custom Agent definition
  - Great discoverability when named and documented.
  - Slightly higher setup and governance overhead.

6) Recommended default for teams
- Start with Skills for repeatable workflows.
- Add custom agent definitions only when teams need explicit role-level invocation and session identity.

Current repository examples
- Skill example (error triage): .github/skills/lab-error-responder/SKILL.md
- Skill example (lesson workflow): .github/skills/lesson-accelerator/SKILL.md

Cross-tool quick mapping examples
- Copilot element: Skill file at .github/skills/<name>/SKILL.md
  - Claude Code analogous pattern: repo instruction package plus task-specific prompt template and tool-permission constraints.
  - Gemini CLI analogous pattern: reusable prompt/script plus CLI config and allowed-tools profile.
- Copilot element: Ask mode
  - Claude Code analogous pattern: direct conversational prompt in coding session (analysis-first, no autonomous multi-step loop unless instructed).
  - Gemini CLI analogous pattern: single-turn or short iterative prompt flow via CLI command.
- Copilot element: Agent mode
  - Claude Code analogous pattern: autonomous tool-using coding loop with explicit guardrails.
  - Gemini CLI analogous pattern: command-driven autonomous workflow when configured with tool access and iteration intent.
- Copilot element: Plan mode
  - Claude Code analogous pattern: planning-first prompt phase before edits.
  - Gemini CLI analogous pattern: plan-first prompt or dry-run script stage before apply stage.
- Copilot element: Custom agent definition
  - Claude Code analogous pattern: named prompt profile plus policy wrapper.
  - Gemini CLI analogous pattern: command alias/wrapper that pins model/options/prompt scaffold for a repeatable role.

Trainer script (short)
1. Explain that labs are intentionally heavy and ambiguous.
2. Show how AI is used to remove toil and preserve human judgment.
3. Demonstrate one Skill in Ask mode and one run in Agent mode.
4. Ask learners to classify each AI action as either:
   - toil reduction,
   - correctness validation,
   - judgment call.
5. Debrief with the rule:
   - automate repetition,
   - supervise risk,
   - document decisions.

Lessons learned checklist (for distribution)
- We treat AI as a force multiplier, not a decision replacement.
- We use guide-first and policy-first execution.
- We preserve prior learner work before regeneration.
- We keep humans accountable for acceptance criteria and risk.
- We log process decisions so others can reuse the pattern.

How to teach this in train-the-trainer format
- Module 1: Interaction model
  - Ask vs Agent vs Plan
- Module 2: Reuse model
  - Skill vs custom agent definition
- Module 3: Governance model
  - Constraints, references, and verification loop
- Module 4: Transfer model
  - Turn one successful run into reusable internal playbooks

Adoption template for teams
- Team objective:
- High-toil workflow to target:
- Skill candidate name:
- Success metric (time, defect rate, handoff clarity):
- Human review gate:
- Rollout owner:
- 30-day retrospective date:
