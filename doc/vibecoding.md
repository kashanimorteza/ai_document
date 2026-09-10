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

### Command

#### Claude

```bash
/plugin
```

#### Bash
Marketplace list
```bash
claude plugin marketplace list
```
Marketplace add
```bash
claude plugin marketplace add anthropics/claude-plugins-official --scope project
claude plugin marketplace add fcakyon/claude-codex-settings --scope project
```

### Plugin Installed
```bash
claude plugin list
```

### Find
```
find ~/.claude/skills -name SKILL.md -print 2>/dev/null
find .claude/skills -name SKILL.md -print 2>/dev/null
```