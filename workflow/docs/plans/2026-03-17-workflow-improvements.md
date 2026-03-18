# Workflow Improvements — Implementation Plan

> Đây là spec chi tiết để implement. Đọc từng task, sửa đúng file, đúng vị trí.
> Sau khi sửa xong mỗi task → commit: `docs(workflow): <mô tả ngắn>`

---

## Task 1: Thêm Subagent vs Agent Team Decision vào `execute.md`

**File:** `workflow/skills/orchestrator/references/execute.md`
**Vị trí:** Thêm section mới SAU "## Routing: Subagent vs Agent Team" (sau line 21)

**Thay thế bảng routing hiện tại bằng:**

```markdown
## Routing: Subagent vs Agent Team

### Decision Guide

| Scenario | Dùng | Tại sao |
|----------|------|---------|
| Task < 5 phút, trivial (typo, rename) | Tự làm | Quá nhỏ, spawn agent lãng phí |
| 1 task rõ ràng (thêm 1 component, 1 API) | Subagent | Scope nhỏ, focused |
| Nhiều tasks ĐỘC LẬP cùng loại | Parallel subagents | Không phụ thuộc → nhanh + rẻ |
| Nhiều tasks PHỤ THUỘC nhau, khác domain | Agent Team | Cần sync: merge intermediate, chờ nhau |
| Review (spec hoặc quality) | Subagent | Luôn 1 scope, 1 mục đích |
| Research | Subagent | 1-way: hỏi → trả lời, không cần collab |

### Tóm gọn
```
Tự làm:           task < 5 phút, trivial
Subagent:          1 task rõ ràng, không cần phối hợp
Parallel subagents: nhiều tasks ĐỘC LẬP
Agent Team:        nhiều tasks PHỤ THUỘC, khác domain, cần sync
```
```

**Acceptance:** Section mới xuất hiện sau routing table, trước "## Process".

---

## Task 2: Sửa Agent Team Pattern trong `execute.md`

**File:** `workflow/skills/orchestrator/references/execute.md`
**Vị trí:** Thay thế toàn bộ section "## Agent Team Pattern" (line 133-155)

**Thay bằng:**

```markdown
## Agent Team Pattern

Cho features cần nhiều expertise hoặc layers phụ thuộc nhau.

**Khi nào dùng:**
- Feature cần BE + FE integrate
- Refactor nhiều modules liên quan
- Full-stack: DB + API + UI

**Setup:**
- Lead: orchestrator (you)
- Teammates: phân theo domain/layer, mỗi người 1 worktree

**Flow:**
1. Lead chia scope → mỗi teammate nhận phần việc + worktree riêng
2. Teammates làm SONG SONG
3. Teammate A xong phần → merge vào feature branch
4. Teammate B cần resource từ A → pull từ feature branch → tiếp tục
5. Lặp lại cho đến khi xong
6. Final merge → verify

**Ví dụ: Build login feature**
```
Teammate A (BE): auth API, JWT, DB schema
  → worktree: .worktrees/login-be

Teammate B (FE): login form, validation, API integration
  → worktree: .worktrees/login-fe

Flow:
  A + B chạy song song
  A xong API endpoints → merge vào feat/login
  B pull feat/login → integrate với API
  B xong → merge vào feat/login
  → verify → done
```

**KHÔNG dùng agent team cho:**
- Tasks độc lập → dùng parallel subagents (rẻ hơn)
- Research → dùng subagent researcher (1-way task)
- Review → dùng subagent reviewer (1 scope)
```

**Acceptance:** Agent Team pattern phản ánh collaborative parallel, có ví dụ BE/FE, có "KHÔNG dùng" section.

---

## Task 3: Thêm Git + Worktree Strategy vào `plan.md`

**File:** `workflow/skills/orchestrator/references/plan.md`
**Vị trí:** Thêm section mới SAU "## Parallelization" (sau line 62), TRƯỚC "## Completion"

**Thêm:**

```markdown
## Git Strategy

### Branch
Khi spec approved → tạo feature branch:
```bash
git checkout -b feat/<slug>
```

### Worktree cho parallel tasks
Mỗi parallel group cần worktree riêng để tránh conflict:

```bash
# Tạo worktree per group
git worktree add .worktrees/<slug>-g1 -b feat/<slug>-g1
git worktree add .worktrees/<slug>-g2 -b feat/<slug>-g2
```

### Worktree cho agent team
Mỗi teammate cần worktree riêng theo domain:

```bash
git worktree add .worktrees/<slug>-be -b feat/<slug>-be
git worktree add .worktrees/<slug>-fe -b feat/<slug>-fe
```

### Conflict avoidance
Khi chia tasks vào groups — đảm bảo không có 2 tasks/teammates sửa cùng file.
Nếu buộc phải cùng file → xếp sequential, không parallel.

AI tự quyết — conflict nhỏ thì merge bình thường. Conflict lớn thì surface to user.
```

**Acceptance:** plan.md có git strategy section với worktree cho cả subagent và agent team modes.

---

## Task 4: Thêm Depth vào `research.md`

**File:** `workflow/skills/orchestrator/references/research.md`
**Vị trí:** Thêm section mới SAU "## Process" (sau ### 3. Document Findings, line 63), TRƯỚC "## Docs Responsibility"

**Thêm:**

```markdown
## Depth

### Khi nào dừng research
- Đã có đủ info để trả lời câu hỏi gốc
- 3+ sources confirm cùng kết luận
- User đã cho direction rõ → không cần thêm options

### Khi nào đào sâu hơn
- Kết quả mâu thuẫn nhau → cần thêm sources
- Quyết định ảnh hưởng lớn (architecture, security)
- User nói "tìm hiểu kỹ" hoặc "deep dive"

### Output scale theo context
- Quick question → 1 paragraph + recommendation
- Compare options → Trade-off table + recommendation
- Deep dive → Full findings + sources + multiple perspectives
```

**Acceptance:** research.md có depth guidelines giúp AI biết khi nào dừng.

---

## Task 5: Thêm Regression Check vào `verify.md`

**File:** `workflow/skills/orchestrator/references/verify.md`
**Vị trí:** Thêm section mới TRƯỚC "### 5. Merge Gate" (trước line 63)

**Thêm:**

```markdown
### 4.5. Regression Check

Trước merge gate, check:

1. **Existing tests**: Chạy full test suite nếu project có
   - Pass → tiếp merge gate
   - Fail → xem test nào fail, có phải do feature mới không

2. **Scope check**: `git diff --stat`
   - Chỉ files trong task scope → OK
   - Files ngoài scope bị thay đổi → cần giải thích

3. **Lint** (nếu project có): phải pass trước merge
```

**Acceptance:** verify.md có regression check trước merge gate.

---

## Task 6: Thêm Track Reasoning vào `spec-form.md`

**File:** `workflow/skills/orchestrator/references/spec-form.md`
**Vị trí:** Trong "## Track Classification" section (line 124-131). Thêm SAU bảng hiện tại.

**Thêm:**

```markdown
### Track Reasoning (bắt buộc)

Khi classify track, nói rõ reasoning:

```
Track: STANDARD
Reasoning:
  - reversibility: ✅ code only, revert safe
  - blast_radius:  ⚠️ affects 2 modules
  - coordination:  ✅ none
  - testability:   ✅ unit test sufficient
```

Không silent classify — reasoning phải visible để user audit nếu cần.
```

**Acceptance:** spec-form.md có track reasoning format hiển thị khi classify.

---

## Task 7: Sync `init_workflow.py`

**File:** `workflow/scripts/init_workflow.py`
**Vị trí:** Trong function `init_docs()` (line 42-53), sau line 50.

**Thêm 2 dòng sau `(DOCS_DIR / "adr").mkdir()`:**

```python
    (DOCS_DIR / "architecture").mkdir()
    (DOCS_DIR / "research").mkdir()
```

**Acceptance:** Script tạo đủ dirs mà reference files mention.

---

## Thứ tự thực hiện

```
Task 1 + 2 → commit: "docs(workflow): improve execute.md — subagent vs team decision + collaborative pattern"
Task 3     → commit: "docs(workflow): add git strategy to plan.md"
Task 4     → commit: "docs(workflow): add depth guidelines to research.md"
Task 5     → commit: "docs(workflow): add regression check to verify.md"
Task 6     → commit: "docs(workflow): add track reasoning to spec-form.md"
Task 7     → commit: "fix(workflow): sync init script with new doc dirs"
```

---

## Sau khi xong

Chạy lại evals để verify routing không bị ảnh hưởng bởi changes.
