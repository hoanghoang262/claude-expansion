# Workflow Plugin — Audit & Cải tiến

> Đánh giá workflow hiện tại + đề xuất cụ thể từng phần.
> Mỗi section: vấn đề → giải pháp → effort → quyết định.
>
> **Cách dùng:** Đọc checklist cuối, đánh `[x]` / `[~]` / `[-]` cho từng item.

---

## Mục lục

1. [Session Continuity — Bỏ STATE.md, đọc từ nguồn thật](#1-session-continuity)
2. [Track Classification — 4 tiêu chí gốc + externalize reasoning](#2-track-classification)
3. [AI là đồng hành — 4 nguyên tắc cốt lõi](#3-ai-là-đồng-hành)
4. [Merge Gate — Điều kiện trước khi merge](#4-merge-gate)
5. [Spec Review — Verification theo từng Success Criteria](#5-spec-review)
6. [Log Architecture — summary.md + 80/20 output](#6-log-architecture)

---

## 1. Session Continuity

### Vấn đề với STATE.md

STATE.md cố giải quyết: AI mở session mới không biết đang làm gì.
Nhưng tạo ra vấn đề mới:

```
Session kết thúc → quên update STATE.md
→ Session mới đọc STATE.md lỗi thời → AI bị mislead
→ Tệ hơn không có gì
```

Ngoài ra AI đọc STATE.md xong vẫn phải đọc lại approved.md, tasks.md, git log.
**STATE.md chỉ là proxy — luôn có nguy cơ stale.**

### Failure recovery cũng không cần file tracking thêm

Hai cơ chế sẵn có đã đủ:

**Claude Code Compact** — khi hết token, session tiếp tục với context compressed.
Không có "session chết giữa chừng."

**Git worktree per task** — nếu session thực sự kết thúc (crash, đóng terminal):
```bash
git -C ../<slug> status         # files nào đang dở
git -C ../<slug> diff HEAD      # code chưa commit
git -C ../<slug> log --oneline  # đã làm tới đâu
```
Worktree tồn tại với đúng trạng thái. Git là source of truth, không cần file tracking thêm.

### Giải pháp: session_start đọc trực tiếp từ nguồn thật

```python
# session_start.py — thay vì đọc STATE.md:

# 1. git worktree list → tìm worktree nào có uncommitted changes
# 2. Đọc .workflow/specs/<slug>/log/summary.md → tiến độ, decisions, context
# 3. git log --oneline -5 → recent commits

# summary.md đã có task status + decisions
# git đã có code state
# Không cần thêm file nào khác
```

**Effort:** Nhỏ — chỉ sửa `session_start.py`

---

## 2. Track Classification

### Quan điểm

AI đã có kiến thức về mọi domain — không cần checklist riêng cho web, game, CI/CD, script, mobile, data pipeline, hay bất kỳ domain nào khác.

Chỉ cần **4 tiêu chí gốc** để đánh giá risk — AI tự apply vào context cụ thể.
Vấn đề không phải AI classify sai, mà là **AI classify âm thầm, không ai kiểm tra được.**

### 4 tiêu chí gốc

---

#### Reversibility — Nếu sai, có thể quay lại không?

AI nhìn vào:
- Thay đổi có persist ra ngoài code không? (database, file system, external API, email, payment)
- Nếu revert code, hệ thống có về đúng trạng thái cũ không?

```
✅ safe    — chỉ thay đổi code logic, revert = git revert
⚠️ medium  — state có thể rollback với effort (migration có down script)
❌ risky   — side effect vĩnh viễn (email sent, data deleted, API contract changed)
```

---

#### Blast Radius — Nếu sai, ảnh hưởng đến đâu?

AI nhìn vào:
- Bao nhiêu module/service/user bị ảnh hưởng?
- Có phải critical path không? (auth, payment, core game loop, deploy pipeline)
- Failure có cascade sang hệ thống khác không?

```
✅ local   — 1 file, 1 component, isolated
⚠️ medium  — 1 module, vài files liên quan
❌ wide    — cross-module, critical path, toàn system, downstream dependencies
```

---

#### Coordination — Cần sync với ai/gì không?

AI nhìn vào:
- Thay đổi có break contract với service/team khác không? (API, interface, protocol)
- Cần deploy nhiều thứ cùng lúc không?

```
✅ none   — isolated, không ai depend vào
⚠️ soft  — cần inform nhưng không block
❌ hard  — cần coordinate deploy, breaking contract, external approval
```

---

#### Testability — Verify được trước khi ship không?

AI nhìn vào:
- Có thể viết automated test không?
- Test chạy được offline hay chỉ biết đúng/sai trên production?

```
✅ high   — unit/integration test đủ, chạy offline
⚠️ medium — cần staging/real env để test đầy đủ
❌ low    — chỉ verify được trên production, hoặc non-deterministic
```

---

#### Mapping sang Track

```
LIGHT    = tất cả ✅  (và không có behavior change mới)
STANDARD = có ít nhất 1 ⚠️, không có ❌
HEAVY    = có bất kỳ ❌ nào

Conflict → lấy dimension tệ nhất.
```

### Bắt AI externalize reasoning

```
[Task Brief]
Track: STANDARD
Reasoning:
  - reversibility: ✅ safe — không có migration
  - blast_radius:  ⚠️ medium — 2 modules bị ảnh hưởng
  - coordination:  ✅ none
  - testability:   ✅ unit test đủ
Action: proceeding
```

Reasoning không thuyết phục → bạn thấy ngay và correct được.
Không cần checklist cứng — AI tự reason, bạn audit.

**Effort:** Nhỏ — thêm 4 tiêu chí + reasoning format vào spec-formation.md

---

## 3. AI là đồng hành

### Triết lý

Đây không phải feature — đây là **nguyên tắc vận hành cốt lõi**.

Công cụ code nhận lệnh và execute.
Đồng hành có quan điểm, phát hiện vấn đề, nói thẳng khi cần, chịu trách nhiệm về output.

4 nguyên tắc sau cần được viết vào orchestrator SKILL.md như phần mở đầu bắt buộc —
không phải checklist, mà là mindset AI phải internalize.

---

### Nguyên tắc 1 — Thông tin chính xác, không phải tự tin

Phân biệt rõ 3 loại statement trong mọi output:

```
[fact]    — đã verify, có source cụ thể
[infer]   — suy luận từ context, có thể sai
[assume]  — giả định chưa verify, cần confirm
```

Sai lầm nguy hiểm nhất: **AI không biết mà nói như biết.**

```
❌ "Approach này sẽ hoạt động tốt."
✅ "[infer] Approach này phù hợp với pattern hiện tại.
    Chưa verify: [X, Y]. Confirm trước khi proceed?"
```

---

### Nguyên tắc 2 — Đối chiếu trước khi kết luận

Trước khi recommend hoặc implement, cross-check:
- Solution này đã tồn tại trong codebase chưa?
- Recommendation có mâu thuẫn với decision đã documented không?
- Assumption nào cần verify với thực tế project?

```
Bỏ qua bước này → recommend dựa trên general knowledge thay vì context thật
→ Duplicate work, contradict existing decisions, không fit project
```

---

### Nguyên tắc 3 — Có quan điểm, nói thẳng một lần

Khi thấy vấn đề — phải nói. Không im để tiếp tục execute.

**Trigger khi thấy:**
- Approach vi phạm existing architecture hoặc documented decisions
- Risk chưa được mention (security, data loss, breaking change)
- Scope creep tiềm ẩn
- Duplicate functionality đã có
- Có cách đơn giản hơn đáng kể

**Format:**
```
⚠️ Concern: [tên vấn đề ngắn gọn]

Vấn đề: [mô tả cụ thể]
Nếu tiếp tục: [hậu quả thực tế]
Đề xuất: [hướng thay thế]

Quyết định của bạn:
  A) Tiếp tục như cũ
  B) Đổi sang đề xuất
  C) Thảo luận thêm
```

**Rules:**
- Raise **một lần**, đủ thông tin để quyết định
- Không repeat sau khi user đã chọn
- Không từ chối execute sau khi user chọn A — quyết định thuộc về user
- Không raise những gì không thực sự ảnh hưởng đến outcome

---

### Nguyên tắc 4 — Thành thật về giới hạn

AI biết nhiều nhưng không biết tất cả. Signal rõ khi ở ranh giới domain knowledge:

```
"Tôi không quen với [X] — recommendation này dựa trên general patterns,
không phải experience với codebase này. Verify trước khi apply."
```

**Effort:** Trung bình — viết lại phần mở đầu orchestrator SKILL.md

---

## 4. Merge Gate

### Vấn đề

Solo developer — không cần PR.
Nhưng `git-workflow.md` có merge checklist nằm tách biệt, không được gọi tự động.

```
AI hoàn thành tasks → im
→ User phải nhớ tự merge, hoặc AI merge luôn không check
```

### Giải pháp: Gate nhỏ cuối execute

Thêm vào `execute.md` sau doc-sync, trước khi declare done:

```markdown
## Merge Gate

Tự check sau khi tất cả tasks DONE + doc-sync complete:
- [ ] Tất cả tasks là [x]
- [ ] git diff main..HEAD — không có debug code, hardcoded values, TODO
- [ ] Tests pass (nếu project có test runner)
- [ ] Doc-sync đã chạy

Pass → báo cáo:
  "[workflow:done] feat/<slug> sẵn sàng merge.
   Changes: [git diff --stat]
   Merge vào main?"

Không pass → liệt kê cụ thể, không tự merge.
```

**Effort:** Rất nhỏ — ~10 dòng thêm vào execute.md

---

## 5. Spec Review

### Vấn đề

Spec-reviewer hiện tại check tổng quát: "implementation có match spec không?"
Không map từng Success Criteria → dễ bỏ sót.

```
SC: "Export PDF với transactions trong 30 ngày"

Reviewer thấy có export function → ✅
Không check: 30-day limit enforced không? Empty state handled không? Tests có không?
```

### Giải pháp: SC Verification Table bắt buộc

Thêm vào `agents/spec-reviewer.md`:

```markdown
## Output format — bắt buộc

| # | Success Criteria (copy từ spec) | Status       | Evidence             |
|---|---------------------------------|--------------|----------------------|
| 1 | [SC-1 exact text]               | ✅ / ❌ / ⚠️ | file:line hoặc "N/A" |
| 2 | [SC-2 exact text]               | ✅ / ❌ / ⚠️ | file:line hoặc "N/A" |

✅ verified + có evidence
❌ không tìm thấy implementation
⚠️ exists nhưng thiếu test hoặc edge case

Rules:
- Có ❌ → task KHÔNG được mark DONE
- Có ⚠️ → ghi note, user quyết định
- PHẢI cite file:line — không được nói "trông có vẻ ổn"
```

**Effort:** Nhỏ — thêm format vào spec-reviewer.md

---

## 6. Log Architecture

### Hai vấn đề gộp lại

**Thiếu tường minh:** Session mới muốn biết chuyện gì đã xảy ra phải đọc từng file riêng lẻ — tốn token, chậm.

**Không có feedback loop:** Sau nhiều features không có dữ liệu để cải thiện workflow.

### Giải pháp: summary.md + 80/20 output format

#### Cấu trúc log

```
.workflow/specs/<slug>/
  approved.md
  tasks.md
  log/
    summary.md      ← ĐỌC TRƯỚC — index toàn bộ feature
    task-1.md       ← chi tiết implementer (đọc khi cần)
    task-2.md
    review-1.md     ← chi tiết reviewer
    review-2.md
```

#### summary.md — AI append sau mỗi task xong

```markdown
# Summary — feat/<slug>
> Đọc file này trước. Drill vào log/task-N.md nếu cần chi tiết.

## Status
track: STANDARD | tasks: 3/4 | started: 2026-03-12

## Tasks
| # | Title              | Status         | Output                  | Issues        |
|---|--------------------|----------------|-------------------------|---------------|
| 1 | Setup module       | ✅             | src/export.ts created   | none          |
| 2 | PDF generation     | ✅             | commit a1b2c3           | 1 minor fixed |
| 3 | Empty state        | ✅             | returns 204, no data    | none          |
| 4 | Integration tests  | 🔄 in progress | —                       | —             |

## Decisions made
- pdfkit thay vì puppeteer — nhẹ hơn, không cần browser
- 30-day limit enforced ở query layer

## Review findings
- Spec-reviewer: 0 critical, 1 important (fixed)
- Quality-reviewer: ✅ approved

## Retro (điền sau merge)
- Track accurate: ?
- Spec amended: ?
- Lesson: ?
```

#### Tại sao summary.md quan trọng

```
Session mới:
  1. Đọc summary.md → biết ngay context, decisions, tiến độ
  2. Drill vào task-N.md chỉ khi cần chi tiết

Không có summary.md:
  Đọc task-1 + task-2 + review-1 + review-2 + tasks.md
  → Tốn 5x token, phần lớn không cần
```

Pattern này áp dụng rộng hơn: session_start hook đọc summary.md thay vì parse toàn bộ `.workflow/`.

#### 80/20 output format — áp dụng cho mọi subagent

```markdown
## Result                    ← đọc cái này là đủ để tiếp tục
status: ✅ done | commit: a1b2c3
what: [1 câu]
issues: none / [list ngắn]

## Details                   ← chỉ đọc khi cần debug
[full implementation notes]
[files changed]
[test output]
```

**Effort:** Trung bình — update format trong implementer.md, spec-reviewer.md, quality-reviewer.md + append logic vào execute.md

---

## Tổng hợp

| # | Cải tiến | Effort | Impact | Ưu tiên |
|---|----------|--------|--------|---------|
| 1 | session_start đọc git worktree + tasks thay vì STATE.md | Nhỏ | Cao | ⭐ Ngay |
| 2 | 4 tiêu chí gốc + externalize reasoning trong Task Brief | Nhỏ | Cao | ⭐ Ngay |
| 3 | 4 nguyên tắc đồng hành vào orchestrator SKILL.md | Trung bình | Rất cao | ⭐ Ngay |
| 4 | Merge gate cuối execute.md | Rất nhỏ | Trung bình | ⭐ Ngay |
| 5 | SC Verification Table trong spec-reviewer.md | Nhỏ | Cao | ⭐ Ngay |
| 6 | summary.md + 80/20 output format | Trung bình | Cao | Sau |

---

## Checklist quyết định

```
[x] = áp dụng   [~] = một phần (ghi note)   [-] = skip (ghi lý do)

[ ] 1.  session_start.py — đọc git worktree list + summary.md thay vì STATE.md
[ ] 2.  spec-formation.md — thêm 4 tiêu chí + bắt buộc externalize reasoning
[ ] 3a. orchestrator SKILL.md — viết 4 nguyên tắc đồng hành vào đầu file
[ ] 3b. implementer.md + spec-reviewer.md — thêm [fact]/[infer]/[assume] convention
[ ] 4.  execute.md — thêm merge gate sau doc-sync
[ ] 5.  spec-reviewer.md — thêm SC Verification Table bắt buộc
[ ] 6a. execute.md — append vào summary.md sau mỗi task hoàn thành
[ ] 6b. implementer.md + reviewers — áp dụng 80/20 output format
```
