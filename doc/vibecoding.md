<!--------------------------------------------------------------------------------- Vibe coding -->
# Vibe coding



<!--------------------------------------------------------------------------------- Install -->
<br><br>

## Install

```bash
curl -fsSL https://claude.ai/install.sh | bash

echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

claude --version
```


<!--------------------------------------------------------------------------------- Plugin  -->
<br><br>

## Remote

```bash
/remote-control
```



<!--------------------------------------------------------------------------------- Start  -->
<br><br>

## Start

```bash
claude --name "Mk-Linux-AgentInterface-Code"
```



<!--------------------------------------------------------------------------------- Plugin  -->
<br><br>

## Plugin

### Market place

[anthropics](https://github.com/anthropics/claude-plugins-official?utm_source=chatgpt.com)  
[fcakyon](https://github.com/fcakyon/claude-codex-settings?utm_source=chatgpt.com)
[pydantic](github.com/pydantic/skills)


### Claude

```bash
/plugin
```

### Marketplace list

```bash
claude plugin marketplace list
```

### Marketplace add

```bash
claude plugin marketplace add anthropics/claude-plugins-official --scope project
claude plugin marketplace add fcakyon/claude-codex-settings --scope project
```

### Plugin Installed

```bash
claude plugin list
```

### Anthropic Plugin

```bash
claude plugin marketplace add anthropics/claude-plugins-official --scope project
claude plugin marketplace add anthropics/skills --scope project
claude plugin install claude-code-setup@claude-plugins-official --scope project
claude plugin install feature-dev@claude-plugins-official --scope project
claude plugin install commit-commands@claude-plugins-official --scope project
claude plugin install plugin-dev@claude-plugins-official --scope project
claude plugin install frontend-design@claude-plugins-official --scope project
claude plugin install example-skills@anthropic-agent-skills --scope project
```

### pydantic

```bash
claude plugin install pydantic-ai@claude-plugins-official --scope project
```

### Uv

```bash
uvx library-skills
uv add "fastapi[standard]"
```

### Find

```bash
find ~/.claude/skills -name SKILL.md -print 2>/dev/null
find .claude/skills -name SKILL.md -print 2>/dev/null
```