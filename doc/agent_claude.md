# Claude

<br><br>

<!--------------------------------------------------------------------------------- Claude -->
## Install

```bash
curl -fsSL https://claude.ai/install.sh | bash

echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

claude --version
```

<br><br>

<!--------------------------------------------------------------------------------- Remote -->
## Remote

```bash
/remote-control
```

<br><br>

<!--------------------------------------------------------------------------------- Start -->
## Start

```bash
CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN=1 claude --name "MK-Mac-Code-MT5" --remote-control --model opus --effort high
CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN=1 claude --name "MK-Linux-Code-MT5" --remote-control --model opus --effort high
$env:CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN="1"; claude --name "MK-Windows-Code-MT5" --remote-control --model opus --effort high
```

<br><br>

<!--------------------------------------------------------------------------------- Plugin -->
## Plugin

<!-------------------------- Command -->
### Command

```bash
/plugin
```

```bash
claude plugin list
```

```bash
claude plugin list --json
```



### Anthropic

[skills](https://github.com/anthropics/skills)  

```bash
claude plugin marketplace add anthropics/skills --scope project
claude plugin install example-skills@anthropic-agent-skills --scope project
claude plugin install document-skills@anthropic-agent-skills --scope project
```

[claude-plugins-official](https://github.com/anthropics/claude-plugins-official)

```bash
claude plugin marketplace add anthropics/claude-plugins-official --scope project
claude plugin install claude-code-setup@claude-plugins-official --scope project
claude plugin install feature-dev@claude-plugins-official --scope project
claude plugin install commit-commands@claude-plugins-official --scope project
claude plugin install plugin-dev@claude-plugins-official --scope project
claude plugin install frontend-design@claude-plugins-official --scope project
claude plugin install claude-md-management@claude-plugins-official --scope project
```

### fcakyon

[fcakyon](https://github.com/fcakyon/claude-codex-settings?utm_source=chatgpt.com)

```bash
claude plugin marketplace add fcakyon/claude-codex-settings --scope project
claude plugin install adhd-output-style@claude-settings --scope project
```

### pydantic

[Source](https://github.com/pydantic/skills)

```bash
claude plugin marketplace add pydantic/skills --scope project
claude plugin install pydantic@pydantic-skills --scope project
claude plugin install logfire@pydantic-skills --scope project 
claude plugin install ai@pydantic-skills --scope project
claude plugin install pydantic-ai-harness@pydantic-skills --scope project

```

claude plugin uninstall ai@pydantic-skills






### Uv

```bash
uvx library-skills
uv cache clean library-skills
uvx library-skills list --installed
uvx library-skills remove fastapi -y

uvx library-skills install --claude --skill sqlmodel --copy -y
uvx library-skills install --claude --skill fastapi --copy -y

uv venv
source .venv/bin/activate
uv pip install "fastapi[standard]"
```

<!-------------------------- multica-ai -->
### andrej-karpathy-skills

https://github.com/multica-ai/andrej-karpathy-skills

```bash
claude plugin marketplace add forrestchang/andrej-karpathy-skills --scope project
claude plugin install andrej-karpathy-skills@karpathy-skills --scope project
```

<br><br>

<!--------------------------------------------------------------------------------- Tools -->
## Tools

<!-------------------------- Graphifyy -->
### Graphifyy

Install
```bash
uv tool install graphifyy
```

Inside project
```bash
graphify install --project
```

Graph
```bash
graphify .
```

Integration
```
graphify claude install
```




<!-------------------------- FastApi -->
### FastApi

[zhanymkanov](https://github.com/zhanymkanov/fastapi-best-practices)  

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