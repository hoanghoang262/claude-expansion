# Project: Workflow Plugin — Orchestrator

## Identity

| Field | Value |
|-------|-------|
| Project | `workflow` plugin trong `claude-code-plugin` marketplace |
| Type | AI orchestration skill — PM agent cho Claude Code |
| Owner | hoanghoang262 |
| Goal | Xây dựng một PM orchestrator đủ mạnh để điều phối mọi loại task (không chỉ software dev) |

## What This Is

Plugin `workflow` định nghĩa một orchestrator skill — một Senior PM agent chạy tự động khi Claude Code session bắt đầu. PM này:
- Hiểu user và project (builds understanding, không chỉ follow pipeline)
- Điều phối specialized agents thực hiện công việc
- Duy trì project memory qua sessions (docs/ = externalized brain)

Plugin nằm trong một marketplace rộng hơn (`claude-code-plugin`) cùng với: `playwright-cli`, `memory`, `superpowers`.

## Current Focus (v0.3 Redesign)

Redesign từ v0.2 (process-first, web-dev centric) sang v0.3 (understanding-first, domain-agnostic).

Những thay đổi cốt lõi:
- **Philosophy:** process-first → understanding-first
- **Phases:** CLARIFY/IMPLEMENT → UNDERSTAND/ACT
- **Memory:** flat docs/ → STM/LTM/Consolidation model
- **Modes:** one rigid pipeline → RESPOND/DIRECT/BUILD patterns (descriptive)
- **Init:** scripts-first → understand-first, adaptive structure

## User Context

Developer đang xây dựng plugin này với mục tiêu dài hạn: một AI assistant đủ thông minh và linh động để làm việc như một personal assistant thực sự, không chỉ là coding tool. 90% use case vẫn là software development nhưng kiến trúc phải support mọi loại project.

Working style: tư duy kiến trúc trước khi implement, thích thảo luận kỹ về design decisions, không muốn over-engineer, ưu tiên chất lượng hơn tốc độ.

## Success Criteria

- PM hoạt động tốt với mọi loại project (web, research, learning, script, config...)
- Memory system tích lũy và cải thiện theo thời gian (virtuous cycle)
- Không cần hướng dẫn chi tiết — PM và agents tự hoạt động được
- Action files clean, không duplicate với SKILL.md global rules
