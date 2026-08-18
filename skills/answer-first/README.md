# Answer First

`answer-first` helps an AI give you the useful part first: the answer, decision, result, or next safe action. Extra explanation comes afterward.

## What it changes

When the skill is active, the AI should:

- answer before giving background;
- use numbered steps for multi-step work;
- state blockers clearly;
- avoid unsupported estimates;
- keep options and next steps focused;
- avoid filler openings and generic closers; and
- preserve safety information, evidence, and required formats.

## Quick example

Instead of:

> There are several things to consider when restarting the service...

The AI should write:

> 1. Restart the service: `sudo systemctl restart SERVICE`  
> 2. Check it: `systemctl status SERVICE`

## Files in this skill

- `SKILL.md` — the instructions the AI follows
- `README.md` — setup and usage instructions
- `CHANGELOG.md` — version history
- `tests/` — examples used to check that the skill behaves correctly

## Use with Hermes

### In a conversation

Ask:

> Load the `answer-first` skill and use it for this conversation.

### Start a session with the skill already loaded

```bash
hermes chat -s answer-first
```

For a one-time request:

```bash
hermes chat -s answer-first -q "Your request"
```

Hermes must have the skill installed in the active profile before it can load it.

## Use with Claude Code

Claude Code supports `SKILL.md` packages directly.

### For one project

Copy this folder to:

```text
your-project/.claude/skills/answer-first/
```

### For all of your projects

Copy it to:

```text
~/.claude/skills/answer-first/
```

Claude can select the skill when it is relevant, or you can invoke it directly with:

```text
/answer-first
```

Claude Code documents these locations and the Agent Skills format in [Extend Claude with skills](https://code.claude.com/docs/en/skills).

## Use with Claude.ai

Claude.ai does not need the test files to follow the behavior.

For a Claude Project:

1. Add `SKILL.md` to the project's files or knowledge.
2. Add this project instruction:

   > Follow the complete `answer-first` instructions in `SKILL.md` for this project unless I ask for another style.

For a single conversation, upload `SKILL.md` and ask Claude to follow it for the conversation.

If your Claude account offers synced Skills, add the skill there and invoke it by name. Availability can depend on the Claude product and account.

## Use with ChatGPT

ChatGPT does not automatically discover a `SKILL.md` folder in the same way as Claude Code or Hermes, but it can still use the instructions.

### In a regular chat

Upload `SKILL.md` and say:

> Follow the complete instructions in this file for the rest of this conversation.

### In a ChatGPT Project

1. Add `SKILL.md` to the project files.
2. Add this project instruction:

   > Use the complete `answer-first` instructions in `SKILL.md` as the default response style for this project.

### In a custom GPT

Paste the contents of `SKILL.md` into the GPT's **Instructions** field. Behavioral rules belong in Instructions rather than relying only on a knowledge-file upload.

OpenAI's current help pages for [Projects in ChatGPT](https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt) and [creating a GPT](https://help.openai.com/en/articles/8554397-creating-a-gpt) describe the available setup options. Interface labels may change over time.

## Use with other AI tools

If the tool supports the Agent Skills format, copy the complete `answer-first` folder into its documented skills location.

If it does not support skills directly:

1. Open `SKILL.md`.
2. Copy its contents into the tool's system prompt, custom instructions, agent instructions, or project instructions.
3. Keep the full instruction set together; do not replace it with a short summary if you want the complete behavior.

## Change modes

After the skill is active:

- say `normal mode` to suspend it for the conversation;
- say `answer-first mode` to turn it back on; or
- ask for a detailed explanation when you want more depth for one response.

## Status

Version `0.4.1` is a candidate. It is usable for testing, but it has not yet passed the repository's complete cross-model release process.
