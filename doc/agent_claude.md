# Claude

<!--------------------------------------------------------------------------------- Claude -->
## Install

```bash
curl -fsSL https://claude.ai/install.sh | bash

echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

claude --version
```

<!--------------------------------------------------------------------------------- Remote -->
## Remote

```bash
/remote-control
```

<!--------------------------------------------------------------------------------- Start -->
## Start

```bash
claude --name "Mk-Linux-AgentInterface-Code"
```

<!--------------------------------------------------------------------------------- Plugin -->
## Plugin

<!-------------------------- Market place -->
### Market place

[anthropics](https://github.com/anthropics/claude-plugins-official?utm_source=chatgpt.com)  
[fcakyon](https://github.com/fcakyon/claude-codex-settings?utm_source=chatgpt.com)
[pydantic](github.com/pydantic/skills)

```bash
/plugin
```

```bash
claude plugin marketplace list
```

```bash
claude plugin marketplace add anthropics/claude-plugins-official --scope project
claude plugin marketplace add anthropics/skills --scope project
claude plugin marketplace add fcakyon/claude-codex-settings --scope project
```

```bash
claude plugin list
```

```bash
find ~/.claude/skills -name SKILL.md -print 2>/dev/null
find .claude/skills -name SKILL.md -print 2>/dev/null
```

<!-------------------------- Package -->
### Package

#### Anthropic

```bash
claude plugin install claude-code-setup@claude-plugins-official --scope project
claude plugin install feature-dev@claude-plugins-official --scope project
claude plugin install commit-commands@claude-plugins-official --scope project
claude plugin install plugin-dev@claude-plugins-official --scope project
claude plugin install frontend-design@claude-plugins-official --scope project
claude plugin install example-skills@anthropic-agent-skills --scope project

claude plugin marketplace add anthropics/skills --scope project
claude plugin install document-skills@anthropic-agent-skills --scope project

claude plugin install claude-md-management@claude-plugins-official --scope project
```

#### fcakyon

```bash
claude plugin install adhd-output-style@claude-settings --scope project
```

#### pydantic

```bash
claude plugin install pydantic-ai@claude-plugins-official --scope project
```

#### Uv

```bash
uvx library-skills
uv cache clean library-skills
uvx library-skills list --installed
uvx library-skills remove fastapi -y

uv venv
source .venv/bin/activate
uv pip install "fastapi[standard]"
```

<!--------------------------------------------------------------------------------- Tools -->
## Tools

<!-------------------------- Obsidian -->
### Obsidian

```bash

```

<!-------------------------- Lum1104 -->
### Lum1104

```bash
claude plugin marketplace add Lum1104/Understand-Anything --scope project
claude plugin install understand-anything
/understand
```

<!-------------------------- Headroom -->
### Headroom

#### Install
```bash
uv tool install --python 3.13 "headroom-ai[all]"
uv tool update-shell
headroom --version
which headroom
headroom doctor
headroom proxy --port 8787
```

#### Desktop
Run service
```bash
headroom proxy --port 8787
```

vim ~/Library/Application\ Support/Claude/claude_desktop_config.json
```json
"mcpServers": {
"headroom": {
    "command": "/Users/morteza/.local/bin/headroom",
    "args": [
    "mcp",
    "serve",
    "--proxy-url",
    "http://127.0.0.1:8787"
    ]
}
}
```

Run
```bash
/my-interface-configure Use the Headroom MCP proactively throughout this run. Compress large file reads, logs, outputs, JSON, and repeated context with headroom_compress. Retrieve original content only when needed. At the end, run headroom_stats and report Headroom usage for this run.
```

Test
```bash
Use headroom_stats and summarize how much Headroom MCP has been used so far.
```

#### Cli

```bash
headroom wrap claude
headroom unwrap claude
```