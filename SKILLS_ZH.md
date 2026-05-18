# Awesome Codex Skills 中文整理

產生日期：2026-05-16

這份文件整理本資料夾中的 Codex skills。說明以各技能資料夾內的 `SKILL.md` metadata 與 repo `README.md` 為基礎，並翻成中文用途說明。

## 總覽

- 技能總數：880
- 一般技能：48
- Composio / Rube MCP 自動化技能：832

## 使用方式摘要

- 每個技能通常是一個資料夾，核心檔案是 `SKILL.md`。
- `SKILL.md` 最上方的 `name` 與 `description` 會被 Codex 用來判斷何時觸發該技能。
- 要安裝單一技能，可把該技能資料夾複製到 `$CODEX_HOME/skills/`，或使用 `skill-installer` 內的安裝腳本。
- `composio-skills` 多數需要 Rube MCP / Composio 連線，並且在操作前先搜尋工具 schema。

## 一般技能

### 開發與程式碼工具

| 技能 | 中文名稱 | 中文用途 | 原始描述 | 路徑 |
|---|---|---|---|---|
| `codebase-migrate` | 大型程式碼遷移 | 把大型 refactor、框架升級、API 遷移拆成可審查批次，並搭配測試與 CI 驗證。 | Run large codebase migrations and multi-file refactors. Uses the Composio CLI to coordinate issue tracking, batched PRs, and CI verification while the agent executes the transforms locally across hundreds of files. | `codebase-migrate/SKILL.md` |
| `create-plan` | 執行計畫草擬 | 快速為 coding 任務產生精簡、可執行的實作計畫。 | Create a concise plan. Use when a user explicitly asks for a plan related to a coding task. | `create-plan/SKILL.md` |
| `deploy-pipeline` | 部署管線 | 處理 Stripe、Supabase、Vercel 等端到端 release 流程，包含驗證與 rollback。 | Run end-to-end deploy pipelines across Stripe, Supabase, and Vercel using the Composio CLI. Promote Stripe products, push Supabase migrations, ship Vercel deployments, and verify with post-deploy checks — all from one script. | `deploy-pipeline/SKILL.md` |
| `gh-address-comments` | GitHub 評論處理 | 使用 gh CLI 檢查目前分支 PR 的 review / issue comments，並協助逐項修正。 | Help address review/issue comments on the open GitHub PR for the current branch using gh CLI; verify gh auth first and prompt the user to authenticate if not logged in. | `gh-address-comments/SKILL.md` |
| `gh-fix-ci` | GitHub CI 修復 | 檢查失敗的 GitHub Actions，摘要錯誤並協助修復 CI 問題。 | Inspect GitHub PR checks with gh, pull failing GitHub Actions logs, summarize failure context, then create a fix plan and implement after user approval. Use when a user asks to debug or fix failing PR CI/CD checks on GitHub Actions and wants a plan + code changes; for external checks (e.g., Buildkite), only report the details URL and mark them out of scope. | `gh-fix-ci/SKILL.md` |
| `mcp-builder` | MCP Server 建置 | 依最佳實務建立與評估 MCP server，包含測試與 evaluation harness。 | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK). | `mcp-builder/SKILL.md` |
| `pr-review-ci-fix` | PR Review 與 CI 自動修復 | 透過 Composio CLI 自動做 GitHub / GitLab PR review，並進入 CI 修復循環。 | Automated PR review and CI auto-fix for GitHub and GitLab using the Composio CLI. Pulls diffs, fetches failing job logs, posts review comments, and loops fix commits until checks go green. | `pr-review-ci-fix/SKILL.md` |
| `sentry-triage` | Sentry 問題分診 | 把 Sentry stack frame 對應到本地原始碼，協助診斷 issue，不必手動複製貼上。 | Diagnose Sentry issues without copy-pasting stack traces. Uses the Composio CLI to pull issue details, events, breadcrumbs, and suspect commits, then maps the frames to local source so the agent can propose a fix directly. | `sentry-triage/SKILL.md` |
| `webapp-testing` | Web App 測試 | 執行目標式 web app 測試並摘要結果，適合本地或已部署頁面驗證。 | Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser screenshots, and viewing browser logs. | `webapp-testing/SKILL.md` |

### 生產力與協作

| 技能 | 中文名稱 | 中文用途 | 原始描述 | 路徑 |
|---|---|---|---|---|
| `connect` | Composio 連線設定 | 把 Codex 連到 1000+ 應用程式，讓代理能真正操作 Slack、GitHub、Notion 等外部服務。 | Connect Codex to any app via the Composio CLI. Send emails, create issues, post messages, update databases - take real actions across Gmail, Slack, GitHub, Notion, and 1000+ services from the terminal. | `connect/SKILL.md` |
| `connect-apps` | 應用工作流連接 | 透過 Composio CLI 設定 Claude / Codex 的 app 連線，並從 shell 啟動外部應用工作流。 | Connect Claude to external apps via the Composio CLI. Use this skill when the user wants to send emails, create issues, post messages, or take actions across Gmail, Slack, GitHub, Notion, and 1000+ services from the terminal. | `connect-apps/SKILL.md` |
| `issue-triage` | Issue 分流 | 從終端機分流 Linear / Jira backlog，整理 bug、優先級、風險與後續行動。 | Triage Linear or Jira backlogs and run bug sweeps via the Composio CLI. Bulk-fetch issues, dedupe, relabel, reassign, and post summaries — all from the shell without clicking through the UI. | `issue-triage/SKILL.md` |
| `linear` | Linear 工作管理 | 管理 Linear issue、project 與團隊工作流。 | Manage issues, projects & team workflows in Linear. Use when the user wants to read, create or updates tickets in Linear. | `linear/SKILL.md` |
| `meeting-insights-analyzer` | 會議洞察分析 | 分析會議逐字稿，整理主題、風險、決策、行動項與後續追蹤。 | Analyzes meeting transcripts and recordings to uncover behavioral patterns, communication insights, and actionable feedback. Identifies when you avoid conflict, use filler words, dominate conversations, or miss opportunities to listen. Perfect for professionals seeking to improve their communication and leadership skills. | `meeting-insights-analyzer/SKILL.md` |
| `meeting-notes-and-actions` | 會議紀錄與行動項 | 把會議逐字稿轉成摘要、決策與標註負責人的 action items。 | Turn meeting transcripts or rough notes into crisp summaries with decisions, risks, and owner-tagged action items; use for Zoom/Meet/Teams transcripts, call notes, or long meeting chats to generate share-ready outputs. | `meeting-notes-and-actions/SKILL.md` |
| `internal-comms` | 內部溝通寫作 | 撰寫內部公告、狀態更新、FAQ、stakeholder 訊息與公司內部溝通素材。 | A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. Claude should use this skill whenever asked to write some sort of internal communications (status reports, leadership updates, 3P updates, company newsletters, FAQs, incident reports, project updates, etc.). | `internal-comms/SKILL.md` |
| `invoice-organizer` | 發票整理 | 標準化與抽取發票資訊，方便追蹤、報表、付款或會計整理。 | Automatically organizes invoices and receipts for tax preparation by reading messy files, extracting key information, renaming them consistently, and sorting them into logical folders. Turns hours of manual bookkeeping into minutes of automated organization. | `invoice-organizer/SKILL.md` |
| `notion-knowledge-capture` | Notion 知識擷取 | 把聊天、筆記或零散資訊轉成結構化 Notion 頁面，並建立合適連結。 | Capture conversations and decisions into structured Notion pages; use when turning chats/notes into wiki entries, how-tos, decisions, or FAQs with proper linking. | `notion-knowledge-capture/SKILL.md` |
| `notion-meeting-intelligence` | Notion 會議情報 | 結合 Notion 內容與 Codex 研究，準備會議材料、背景脈絡與行動摘要。 | Prepare meeting materials with Notion context and Codex research; use when gathering context, drafting agendas/pre-reads, and tailoring materials to attendees. | `notion-meeting-intelligence/SKILL.md` |
| `notion-research-documentation` | Notion 研究文件化 | 整合多個 Notion 來源，產生有引用的研究簡報、比較報告或完整文件。 | Research across Notion and synthesize into structured documentation; use when gathering info from multiple Notion sources to produce briefs, comparisons, or reports with citations. | `notion-research-documentation/SKILL.md` |
| `notion-spec-to-implementation` | Notion 規格轉實作 | 把 Notion 規格轉成實作計畫、任務拆解與進度追蹤。 | Turn Notion specs into implementation plans, tasks, and progress tracking; use when implementing PRDs/feature specs and creating Notion plans + tasks from them. | `notion-spec-to-implementation/SKILL.md` |
| `support-ticket-triage` | 客服工單分流 | 分類客服 ticket、判斷優先級、整理下一步，並草擬回覆。 | Triage customer support tickets/emails/chats into categories, priority, and next action; draft responses and create reproducible steps; use for Zendesk/Intercom/Help Scout exports or pasted threads. | `support-ticket-triage/SKILL.md` |
| `file-organizer` | 檔案整理器 | 整理、重新命名、分類與清理工作區檔案，讓資料夾結構更乾淨。 | Intelligently organizes your files and folders across your computer by understanding context, finding duplicates, suggesting better structures, and automating cleanup tasks. Reduces cognitive load and keeps your digital workspace tidy without manual effort. | `file-organizer/SKILL.md` |
| `paperjsx` | PaperJSX 文件產生 | 從結構化 JSON 在本機產生 PPTX、DOCX、XLSX、PDF 發票、報告與圖表。 | Generate PPTX presentations, DOCX documents, XLSX spreadsheets, and PDF reports from structured JSON input using PaperJSX. | `paperjsx/SKILL.md` |
| `skill-share` | 技能分享 | 協助把 skill 與可重用指令分享給團隊，建立一致的工作方式。 | A skill that creates new Claude skills and automatically shares them on Slack using Rube for seamless team collaboration and skill discovery. | `skill-share/SKILL.md` |

### 溝通與寫作

| 技能 | 中文名稱 | 中文用途 | 原始描述 | 路徑 |
|---|---|---|---|---|
| `email-draft-polish` | Email 草稿潤飾 | 依受眾與語氣需求撰寫、改寫、壓縮或潤飾 email。 | Draft, rewrite, or condense emails with target tone, length, and audience; use for cold outreach, replies, status updates, or escalations where clarity and brevity matter. | `email-draft-polish/SKILL.md` |
| `changelog-generator` | 更新紀錄產生器 | 根據 commit、PR、issue 或摘要產生清楚可讀的 changelog / release notes。 | Automatically creates user-facing changelogs from git commits by analyzing commit history, categorizing changes, and transforming technical commits into clear, customer-friendly release notes. Turns hours of manual changelog writing into minutes of automated generation. | `changelog-generator/SKILL.md` |
| `content-research-writer` | 內容研究寫作助手 | 協助研究、列大綱、加引用、改善開頭、逐段回饋，適合文章、教學、技術文件與思想領袖內容。 | Assists in writing high-quality content by conducting research, adding citations, improving hooks, iterating on outlines, and providing real-time feedback on each section. Transforms your writing process from solo effort to collaborative partnership. | `content-research-writer/SKILL.md` |
| `tailored-resume-generator` | 履歷客製化 | 依職缺描述改寫履歷，強化量化成果與職缺匹配度。 | Analyzes job descriptions and generates tailored resumes that highlight relevant experience, skills, and achievements to maximize interview chances | `tailored-resume-generator/SKILL.md` |

### 資料與分析

| 技能 | 中文名稱 | 中文用途 | 原始描述 | 路徑 |
|---|---|---|---|---|
| `spreadsheet-formula-helper` | 試算表公式助手 | 撰寫與除錯 Excel / Google Sheets 公式、pivot、array formula 與資料轉換。 | Write and debug spreadsheet formulas (Excel/Google Sheets), pivot tables, and array formulas; translate between dialects; use when users need working formulas with examples and edge-case checks. | `spreadsheet-formula-helper/SKILL.md` |
| `competitive-ads-extractor` | 競品廣告分析 | 分析競爭對手廣告素材，抽取賣點、受眾、文案角度、創意模式與結構化洞察。 | Extracts and analyzes competitors' ads from ad libraries (Facebook, LinkedIn, etc.) to understand what messaging, problems, and creative approaches are working. Helps inspire and improve your own ad campaigns. | `competitive-ads-extractor/SKILL.md` |
| `datadog-logs` | Datadog 日誌查詢 | 用 Composio CLI 從 shell 查詢與過濾 Datadog logs，產生 JSON 友善輸出與摘要。 | Query and filter Datadog logs from the shell using the Composio CLI. Run scoped log searches, pivot across services/environments, and export structured JSON for downstream agents instead of click-driving the Datadog UI. | `datadog-logs/SKILL.md` |
| `developer-growth-analysis` | 開發者成長分析 | 分析 Codex 對話歷史，找出 coding 模式、學習缺口與可改進習慣。 | Analyzes your recent Codex chat history to identify coding patterns, development gaps, and areas for improvement, curates relevant learning resources from HackerNews, and automatically sends a personalized growth report to your Slack DMs. | `developer-growth-analysis/SKILL.md` |
| `lead-research-assistant` | 潛在客戶研究 | 研究 leads，補齊公司、產業、規模、訊號等 firmographic 資料。 | Identifies high-quality leads for your product or service by analyzing your business, searching for target companies, and providing actionable contact strategies. Perfect for sales, business development, and marketing professionals. | `lead-research-assistant/SKILL.md` |
| `domain-name-brainstormer` | 網域名稱發想 | 依品牌、限制與可用性條件發想網域名稱，並協助檢查候選。 | Generates creative domain name ideas for your project and checks availability across multiple TLDs (.com, .io, .dev, .ai, etc.). Saves hours of brainstorming and manual checking. | `domain-name-brainstormer/SKILL.md` |
| `raffle-winner-picker` | 抽獎中獎者選取 | 隨機選出得獎者並產生可稽核紀錄，適合活動抽獎與公平性留痕。 | Picks random winners from lists, spreadsheets, or Google Sheets for giveaways, raffles, and contests. Ensures fair, unbiased selection with transparency. | `raffle-winner-picker/SKILL.md` |
| `langsmith-fetch` | LangSmith 資料擷取 | 拉取 LangSmith 專案、測試與 trace 資料，供後續分析與除錯。 | Debug LangChain and LangGraph agents by fetching execution traces from LangSmith Studio. Use when debugging agent behavior, investigating errors, analyzing tool calls, checking memory operations, or examining agent performance. Automatically fetches recent traces and analyzes execution patterns. Requires langsmith-fetch CLI installed. | `langsmith-fetch/SKILL.md` |
| `helium-mcp` | Helium MCP 即時研究 | 透過 MCP 查詢即時新聞、偏見評分、市場資料、選擇權定價與平衡式新聞摘要。 | Search real-time news with bias scoring, get live stock/ETF/crypto data with AI analysis, ML options pricing, balanced news synthesis, and meme search via the Helium MCP server. | `helium-mcp/SKILL.md` |

### Meta 與工具

| 技能 | 中文名稱 | 中文用途 | 原始描述 | 路徑 |
|---|---|---|---|---|
| `brand-guidelines` | 品牌規範套用 | 把 OpenAI / Codex 的品牌色、字體與視覺規範套用到文件、簡報、設計稿或其他輸出物。 | Applies OpenAI's brand colors and typography to any artifact that should match the Codex/OpenAI look-and-feel. Use it when brand colors or style guidelines, visual formatting, or company design standards apply. | `brand-guidelines/SKILL.md` |
| `agent-deep-links` | Agent 深層連結產生器 | 產生並驗證 Codex、Cursor、VS Code 等工具可用的 deep link，包含 Slack 可安全貼上的格式與備援說明。 | Build, validate, and troubleshoot deep links for Codex, Cursor, VS Code, Visual Studio, and similar tools. Use when users ask for clickable links (especially in Slack) that open threads, files, folders, or app settings. | `agent-deep-links/SKILL.md` |
| `canvas-design` | Canvas 設計產生器 | 依需求產生結構化的 canvas 版面、設計框架與視覺產物，適合快速做概念稿或設計規劃。 | Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to create a poster, piece of art, design, or other static piece. Create original visual designs, never copying existing artists' work to avoid copyright violations. | `canvas-design/SKILL.md` |
| `image-enhancer` | 圖片增強 | 依 preset 放大、修復與優化圖片，適合改善畫質或產生更乾淨的輸出。 | Improves the quality of images, especially screenshots, by enhancing resolution, sharpness, and clarity. Perfect for preparing images for presentations, documentation, or social media posts. | `image-enhancer/SKILL.md` |
| `slack-gif-creator` | Slack GIF 產生器 | 產生適合 Slack 使用的 GIF，支援字幕、樣式與訊息情境。 | Toolkit for creating animated GIFs optimized for Slack, with validators for size constraints and composable animation primitives. This skill applies when users request animated GIFs or emoji animations for Slack from descriptions like "make me a GIF for Slack of X doing Y". | `slack-gif-creator/SKILL.md` |
| `theme-factory` | 主題工廠 | 建立可重用的 theme token、色票、排版與視覺風格。 | Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are 10 pre-set themes with colors/fonts that you can apply to any artifact that has been creating, or can generate a new theme on-the-fly. | `theme-factory/SKILL.md` |
| `youtube-downloader` | 影片下載整理 | 下載並準備影片供離線檢視、研究或後續處理。 | Download YouTube videos with customizable quality and format options. Use this skill when the user asks to download, save, or grab YouTube videos. Supports various quality settings (best, 1080p, 720p, 480p, 360p), multiple formats (mp4, webm, mkv), and audio-only downloads as MP3. | `video-downloader/SKILL.md` |
| `template-skill` | 技能範本 | 建立新 skill 的起始範本，展示標準資料夾與 SKILL.md 結構。 | Replace with description of the skill and when Claude should use it. | `template-skill/SKILL.md` |
| `skill-installer` | 技能安裝器 | 協助找出、推薦、列出並安裝適合的 Codex skill；可從 curated list 或 GitHub path 安裝，也適合處理像「我找一個superpower skill」這類想先找對 skill 的需求。 | Find, recommend, list, and install Codex skills into $CODEX_HOME/skills from a curated list or a GitHub repo path. Use when a user asks to discover the right skill, browse available skills, says things like "我找一個superpower skill", install a curated skill, or install a skill from another repo (including private repos). | `skill-installer/SKILL.md` |
| `skill-creator` | 技能建立指南 | 指導如何建立有效的 Codex skill，包含 metadata、漸進式載入、腳本與參考資料。 | Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Codex's capabilities with specialized knowledge, workflows, or tool integrations. | `skill-creator/SKILL.md` |

## Composio / Rube MCP 自動化技能

這一區大多是「某個 SaaS / API 的自動化連接器」。通常用途是：先用 Rube MCP 搜尋該服務可用工具與 schema，確認連線，再執行對應的查詢、建立、更新或管理動作。

| # | 技能 | 服務 / 工具 | 中文用途 | 路徑 |
|---:|---|---|---|---|
| 1 | `-21risk-automation` | 21risk | 透過 Composio / Rube MCP 自動化 21risk 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/-21risk-automation/SKILL.md` |
| 2 | `-2chat-automation` | 2chat | 透過 Composio / Rube MCP 自動化 2chat 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/-2chat-automation/SKILL.md` |
| 3 | `ably-automation` | Ably | 透過 Composio / Rube MCP 自動化 Ably 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/ably-automation/SKILL.md` |
| 4 | `abstract-automation` | Abstract | 透過 Composio / Rube MCP 自動化 Abstract 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/abstract-automation/SKILL.md` |
| 5 | `abuselpdb-automation` | Abuselpdb | 透過 Composio / Rube MCP 自動化 Abuselpdb 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/abuselpdb-automation/SKILL.md` |
| 6 | `abyssale-automation` | Abyssale | 透過 Composio / Rube MCP 自動化 Abyssale 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/abyssale-automation/SKILL.md` |
| 7 | `accelo-automation` | Accelo | 透過 Composio / Rube MCP 自動化 Accelo 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/accelo-automation/SKILL.md` |
| 8 | `accredible-certificates-automation` | Accredible Certificates | 透過 Composio / Rube MCP 自動化 Accredible Certificates 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/accredible-certificates-automation/SKILL.md` |
| 9 | `acculynx-automation` | Acculynx | 透過 Composio / Rube MCP 自動化 Acculynx 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/acculynx-automation/SKILL.md` |
| 10 | `active-campaign-automation` | Active Campaign | 透過 Composio / Rube MCP 自動化 Active Campaign 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/active-campaign-automation/SKILL.md` |
| 11 | `addresszen-automation` | Addresszen | 透過 Composio / Rube MCP 自動化 Addresszen 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/addresszen-automation/SKILL.md` |
| 12 | `adobe-automation` | Adobe | 透過 Composio / Rube MCP 自動化 Adobe 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/adobe-automation/SKILL.md` |
| 13 | `adrapid-automation` | Adrapid | 透過 Composio / Rube MCP 自動化 Adrapid 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/adrapid-automation/SKILL.md` |
| 14 | `adyntel-automation` | Adyntel | 透過 Composio / Rube MCP 自動化 Adyntel 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/adyntel-automation/SKILL.md` |
| 15 | `aero-workflow-automation` | Aero Workflow | 透過 Composio / Rube MCP 自動化 Aero Workflow 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/aero-workflow-automation/SKILL.md` |
| 16 | `aeroleads-automation` | Aeroleads | 透過 Composio / Rube MCP 自動化 Aeroleads 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/aeroleads-automation/SKILL.md` |
| 17 | `affinda-automation` | Affinda | 透過 Composio / Rube MCP 自動化 Affinda 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/affinda-automation/SKILL.md` |
| 18 | `affinity-automation` | Affinity | 透過 Composio / Rube MCP 自動化 Affinity 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/affinity-automation/SKILL.md` |
| 19 | `agencyzoom-automation` | Agencyzoom | 透過 Composio / Rube MCP 自動化 Agencyzoom 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/agencyzoom-automation/SKILL.md` |
| 20 | `agent-mail-automation` | Agent Mail | 透過 Composio / Rube MCP 自動化 Agent Mail 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/agent-mail-automation/SKILL.md` |
| 21 | `agentql-automation` | Agentql | 透過 Composio / Rube MCP 自動化 Agentql 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/agentql-automation/SKILL.md` |
| 22 | `agenty-automation` | Agenty | 透過 Composio / Rube MCP 自動化 Agenty 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/agenty-automation/SKILL.md` |
| 23 | `agiled-automation` | Agiled | 透過 Composio / Rube MCP 自動化 Agiled 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/agiled-automation/SKILL.md` |
| 24 | `agility-cms-automation` | Agility CMS | 透過 Composio / Rube MCP 自動化 Agility CMS 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/agility-cms-automation/SKILL.md` |
| 25 | `Ahrefs Automation` | Ahrefs | 透過 Composio / Rube MCP 自動化 Ahrefs 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/ahrefs-automation/SKILL.md` |
| 26 | `ai-ml-api-automation` | AI/ML API | 透過 Composio / Rube MCP 自動化 AI/ML API 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/ai-ml-api-automation/SKILL.md` |
| 27 | `aivoov-automation` | Aivoov | 透過 Composio / Rube MCP 自動化 Aivoov 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/aivoov-automation/SKILL.md` |
| 28 | `alchemy-automation` | Alchemy | 透過 Composio / Rube MCP 自動化 Alchemy 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/alchemy-automation/SKILL.md` |
| 29 | `algodocs-automation` | Algodocs | 透過 Composio / Rube MCP 自動化 Algodocs 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/algodocs-automation/SKILL.md` |
| 30 | `algolia-automation` | Algolia | 透過 Composio / Rube MCP 自動化 Algolia 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/algolia-automation/SKILL.md` |
| 31 | `all-images-ai-automation` | All Images AI | 透過 Composio / Rube MCP 自動化 All Images AI 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/all-images-ai-automation/SKILL.md` |
| 32 | `alpha-vantage-automation` | Alpha Vantage | 透過 Composio / Rube MCP 自動化 Alpha Vantage 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/alpha-vantage-automation/SKILL.md` |
| 33 | `altoviz-automation` | Altoviz | 透過 Composio / Rube MCP 自動化 Altoviz 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/altoviz-automation/SKILL.md` |
| 34 | `alttext-ai-automation` | Alttext AI | 透過 Composio / Rube MCP 自動化 Alttext AI 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/alttext-ai-automation/SKILL.md` |
| 35 | `amara-automation` | Amara | 透過 Composio / Rube MCP 自動化 Amara 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/amara-automation/SKILL.md` |
| 36 | `amazon-automation` | Amazon | 透過 Composio / Rube MCP 自動化 Amazon 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/amazon-automation/SKILL.md` |
| 37 | `ambee-automation` | Ambee | 透過 Composio / Rube MCP 自動化 Ambee 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/ambee-automation/SKILL.md` |
| 38 | `ambient-weather-automation` | Ambient Weather | 透過 Composio / Rube MCP 自動化 Ambient Weather 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/ambient-weather-automation/SKILL.md` |
| 39 | `amcards-automation` | Amcards | 透過 Composio / Rube MCP 自動化 Amcards 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/amcards-automation/SKILL.md` |
| 40 | `anchor-browser-automation` | Anchor Browser | 透過 Composio / Rube MCP 自動化 Anchor Browser 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/anchor-browser-automation/SKILL.md` |
| 41 | `anonyflow-automation` | Anonyflow | 透過 Composio / Rube MCP 自動化 Anonyflow 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/anonyflow-automation/SKILL.md` |
| 42 | `anthropic-administrator-automation` | Anthropic Administrator | 透過 Composio / Rube MCP 自動化 Anthropic Administrator 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/anthropic-administrator-automation/SKILL.md` |
| 43 | `anthropic_administrator-automation` | Anthropic Administrator | 透過 Composio / Rube MCP 自動化 Anthropic Administrator 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/anthropic_administrator-automation/SKILL.md` |
| 44 | `apaleo-automation` | Apaleo | 透過 Composio / Rube MCP 自動化 Apaleo 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/apaleo-automation/SKILL.md` |
| 45 | `apex27-automation` | Apex27 | 透過 Composio / Rube MCP 自動化 Apex27 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/apex27-automation/SKILL.md` |
| 46 | `api-bible-automation` | API Bible | 透過 Composio / Rube MCP 自動化 API Bible 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/api-bible-automation/SKILL.md` |
| 47 | `api-labz-automation` | API Labz | 透過 Composio / Rube MCP 自動化 API Labz 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/api-labz-automation/SKILL.md` |
| 48 | `api-ninjas-automation` | API Ninjas | 透過 Composio / Rube MCP 自動化 API Ninjas 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/api-ninjas-automation/SKILL.md` |
| 49 | `api-sports-automation` | API Sports | 透過 Composio / Rube MCP 自動化 API Sports 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/api-sports-automation/SKILL.md` |
| 50 | `api2pdf-automation` | Api2pdf | 透過 Composio / Rube MCP 自動化 Api2pdf 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/api2pdf-automation/SKILL.md` |
| 51 | `apiflash-automation` | Apiflash | 透過 Composio / Rube MCP 自動化 Apiflash 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/apiflash-automation/SKILL.md` |
| 52 | `Apify Automation` | Apify | 透過 Composio / Rube MCP 自動化 Apify 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/apify-automation/SKILL.md` |
| 53 | `apilio-automation` | Apilio | 透過 Composio / Rube MCP 自動化 Apilio 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/apilio-automation/SKILL.md` |
| 54 | `apipie-ai-automation` | Apipie AI | 透過 Composio / Rube MCP 自動化 Apipie AI 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/apipie-ai-automation/SKILL.md` |
| 55 | `apitemplate-io-automation` | Apitemplate IO | 透過 Composio / Rube MCP 自動化 Apitemplate IO 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/apitemplate-io-automation/SKILL.md` |
| 56 | `apiverve-automation` | Apiverve | 透過 Composio / Rube MCP 自動化 Apiverve 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/apiverve-automation/SKILL.md` |
| 57 | `Apollo Automation` | Apollo | 透過 Composio / Rube MCP 自動化 Apollo 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/apollo-automation/SKILL.md` |
| 58 | `appcircle-automation` | Appcircle | 透過 Composio / Rube MCP 自動化 Appcircle 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/appcircle-automation/SKILL.md` |
| 59 | `appdrag-automation` | Appdrag | 透過 Composio / Rube MCP 自動化 Appdrag 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/appdrag-automation/SKILL.md` |
| 60 | `appointo-automation` | Appointo | 透過 Composio / Rube MCP 自動化 Appointo 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/appointo-automation/SKILL.md` |
| 61 | `appsflyer-automation` | Appsflyer | 透過 Composio / Rube MCP 自動化 Appsflyer 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/appsflyer-automation/SKILL.md` |
| 62 | `appveyor-automation` | Appveyor | 透過 Composio / Rube MCP 自動化 Appveyor 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/appveyor-automation/SKILL.md` |
| 63 | `aryn-automation` | Aryn | 透過 Composio / Rube MCP 自動化 Aryn 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/aryn-automation/SKILL.md` |
| 64 | `ascora-automation` | Ascora | 透過 Composio / Rube MCP 自動化 Ascora 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/ascora-automation/SKILL.md` |
| 65 | `Ashby Automation` | Ashby | 透過 Composio / Rube MCP 自動化 Ashby 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/ashby-automation/SKILL.md` |
| 66 | `asin-data-api-automation` | Asin Data API | 透過 Composio / Rube MCP 自動化 Asin Data API 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/asin-data-api-automation/SKILL.md` |
| 67 | `astica-ai-automation` | Astica AI | 透過 Composio / Rube MCP 自動化 Astica AI 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/astica-ai-automation/SKILL.md` |
| 68 | `async-interview-automation` | Async Interview | 透過 Composio / Rube MCP 自動化 Async Interview 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/async-interview-automation/SKILL.md` |
| 69 | `atlassian-automation` | Atlassian | 透過 Composio / Rube MCP 自動化 Atlassian 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/atlassian-automation/SKILL.md` |
| 70 | `Attio Automation` | Attio | 透過 Composio / Rube MCP 自動化 Attio 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/attio-automation/SKILL.md` |
| 71 | `auth0-automation` | Auth0 | 透過 Composio / Rube MCP 自動化 Auth0 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/auth0-automation/SKILL.md` |
| 72 | `autobound-automation` | Autobound | 透過 Composio / Rube MCP 自動化 Autobound 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/autobound-automation/SKILL.md` |
| 73 | `autom-automation` | Autom | 透過 Composio / Rube MCP 自動化 Autom 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/autom-automation/SKILL.md` |
| 74 | `axonaut-automation` | Axonaut | 透過 Composio / Rube MCP 自動化 Axonaut 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/axonaut-automation/SKILL.md` |
| 75 | `ayrshare-automation` | Ayrshare | 透過 Composio / Rube MCP 自動化 Ayrshare 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/ayrshare-automation/SKILL.md` |
| 76 | `backendless-automation` | Backendless | 透過 Composio / Rube MCP 自動化 Backendless 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/backendless-automation/SKILL.md` |
| 77 | `bannerbear-automation` | Bannerbear | 透過 Composio / Rube MCP 自動化 Bannerbear 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/bannerbear-automation/SKILL.md` |
| 78 | `bart-automation` | Bart | 透過 Composio / Rube MCP 自動化 Bart 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/bart-automation/SKILL.md` |
| 79 | `baselinker-automation` | Baselinker | 透過 Composio / Rube MCP 自動化 Baselinker 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/baselinker-automation/SKILL.md` |
| 80 | `baserow-automation` | Baserow | 透過 Composio / Rube MCP 自動化 Baserow 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/baserow-automation/SKILL.md` |
| 81 | `basin-automation` | Basin | 透過 Composio / Rube MCP 自動化 Basin 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/basin-automation/SKILL.md` |
| 82 | `battlenet-automation` | Battlenet | 透過 Composio / Rube MCP 自動化 Battlenet 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/battlenet-automation/SKILL.md` |
| 83 | `beaconchain-automation` | Beaconchain | 透過 Composio / Rube MCP 自動化 Beaconchain 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/beaconchain-automation/SKILL.md` |
| 84 | `beaconstac-automation` | Beaconstac | 透過 Composio / Rube MCP 自動化 Beaconstac 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/beaconstac-automation/SKILL.md` |
| 85 | `beamer-automation` | Beamer | 透過 Composio / Rube MCP 自動化 Beamer 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/beamer-automation/SKILL.md` |
| 86 | `beeminder-automation` | Beeminder | 透過 Composio / Rube MCP 自動化 Beeminder 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/beeminder-automation/SKILL.md` |
| 87 | `bench-automation` | Bench | 透過 Composio / Rube MCP 自動化 Bench 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/bench-automation/SKILL.md` |
| 88 | `benchmark-email-automation` | Benchmark Email | 透過 Composio / Rube MCP 自動化 Benchmark Email 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/benchmark-email-automation/SKILL.md` |
| 89 | `benzinga-automation` | Benzinga | 透過 Composio / Rube MCP 自動化 Benzinga 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/benzinga-automation/SKILL.md` |
| 90 | `bestbuy-automation` | Bestbuy | 透過 Composio / Rube MCP 自動化 Bestbuy 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/bestbuy-automation/SKILL.md` |
| 91 | `better-proposals-automation` | Better Proposals | 透過 Composio / Rube MCP 自動化 Better Proposals 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/better-proposals-automation/SKILL.md` |
| 92 | `better-stack-automation` | Better Stack | 透過 Composio / Rube MCP 自動化 Better Stack 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/better-stack-automation/SKILL.md` |
| 93 | `bidsketch-automation` | Bidsketch | 透過 Composio / Rube MCP 自動化 Bidsketch 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/bidsketch-automation/SKILL.md` |
| 94 | `big-data-cloud-automation` | Big Data Cloud | 透過 Composio / Rube MCP 自動化 Big Data Cloud 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/big-data-cloud-automation/SKILL.md` |
| 95 | `bigmailer-automation` | Bigmailer | 透過 Composio / Rube MCP 自動化 Bigmailer 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/bigmailer-automation/SKILL.md` |
| 96 | `bigml-automation` | Bigml | 透過 Composio / Rube MCP 自動化 Bigml 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/bigml-automation/SKILL.md` |
| 97 | `bigpicture-io-automation` | Bigpicture IO | 透過 Composio / Rube MCP 自動化 Bigpicture IO 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/bigpicture-io-automation/SKILL.md` |
| 98 | `bitquery-automation` | Bitquery | 透過 Composio / Rube MCP 自動化 Bitquery 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/bitquery-automation/SKILL.md` |
| 99 | `bitwarden-automation` | Bitwarden | 透過 Composio / Rube MCP 自動化 Bitwarden 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/bitwarden-automation/SKILL.md` |
| 100 | `blackbaud-automation` | Blackbaud | 透過 Composio / Rube MCP 自動化 Blackbaud 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/blackbaud-automation/SKILL.md` |
| 101 | `blackboard-automation` | Blackboard | 透過 Composio / Rube MCP 自動化 Blackboard 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/blackboard-automation/SKILL.md` |
| 102 | `blocknative-automation` | Blocknative | 透過 Composio / Rube MCP 自動化 Blocknative 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/blocknative-automation/SKILL.md` |
| 103 | `boldsign-automation` | Boldsign | 透過 Composio / Rube MCP 自動化 Boldsign 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/boldsign-automation/SKILL.md` |
| 104 | `bolna-automation` | Bolna | 透過 Composio / Rube MCP 自動化 Bolna 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/bolna-automation/SKILL.md` |
| 105 | `boloforms-automation` | Boloforms | 透過 Composio / Rube MCP 自動化 Boloforms 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/boloforms-automation/SKILL.md` |
| 106 | `bolt-iot-automation` | Bolt Iot | 透過 Composio / Rube MCP 自動化 Bolt Iot 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/bolt-iot-automation/SKILL.md` |
| 107 | `bonsai-automation` | Bonsai | 透過 Composio / Rube MCP 自動化 Bonsai 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/bonsai-automation/SKILL.md` |
| 108 | `bookingmood-automation` | Bookingmood | 透過 Composio / Rube MCP 自動化 Bookingmood 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/bookingmood-automation/SKILL.md` |
| 109 | `booqable-automation` | Booqable | 透過 Composio / Rube MCP 自動化 Booqable 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/booqable-automation/SKILL.md` |
| 110 | `borneo-automation` | Borneo | 透過 Composio / Rube MCP 自動化 Borneo 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/borneo-automation/SKILL.md` |
| 111 | `botbaba-automation` | Botbaba | 透過 Composio / Rube MCP 自動化 Botbaba 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/botbaba-automation/SKILL.md` |
| 112 | `botpress-automation` | Botpress | 透過 Composio / Rube MCP 自動化 Botpress 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/botpress-automation/SKILL.md` |
| 113 | `botsonic-automation` | Botsonic | 透過 Composio / Rube MCP 自動化 Botsonic 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/botsonic-automation/SKILL.md` |
| 114 | `botstar-automation` | Botstar | 透過 Composio / Rube MCP 自動化 Botstar 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/botstar-automation/SKILL.md` |
| 115 | `bouncer-automation` | Bouncer | 透過 Composio / Rube MCP 自動化 Bouncer 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/bouncer-automation/SKILL.md` |
| 116 | `boxhero-automation` | Boxhero | 透過 Composio / Rube MCP 自動化 Boxhero 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/boxhero-automation/SKILL.md` |
| 117 | `Braintree Automation` | Braintree | 透過 Composio / Rube MCP 自動化 Braintree 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/braintree-automation/SKILL.md` |
| 118 | `brandfetch-automation` | Brandfetch | 透過 Composio / Rube MCP 自動化 Brandfetch 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/brandfetch-automation/SKILL.md` |
| 119 | `breeze-automation` | Breeze | 透過 Composio / Rube MCP 自動化 Breeze 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/breeze-automation/SKILL.md` |
| 120 | `breezy-hr-automation` | Breezy Hr | 透過 Composio / Rube MCP 自動化 Breezy Hr 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/breezy-hr-automation/SKILL.md` |
| 121 | `brex-automation` | Brex | 透過 Composio / Rube MCP 自動化 Brex 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/brex-automation/SKILL.md` |
| 122 | `brex-staging-automation` | Brex Staging | 透過 Composio / Rube MCP 自動化 Brex Staging 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/brex-staging-automation/SKILL.md` |
| 123 | `brightdata-automation` | Brightdata | 透過 Composio / Rube MCP 自動化 Brightdata 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/brightdata-automation/SKILL.md` |
| 124 | `brightpearl-automation` | Brightpearl | 透過 Composio / Rube MCP 自動化 Brightpearl 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/brightpearl-automation/SKILL.md` |
| 125 | `brilliant-directories-automation` | Brilliant Directories | 透過 Composio / Rube MCP 自動化 Brilliant Directories 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/brilliant-directories-automation/SKILL.md` |
| 126 | `browseai-automation` | Browseai | 透過 Composio / Rube MCP 自動化 Browseai 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/browseai-automation/SKILL.md` |
| 127 | `browser-tool-automation` | Browser Tool | 透過 Composio / Rube MCP 自動化 Browser Tool 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/browser-tool-automation/SKILL.md` |
| 128 | `browserbase-tool-automation` | Browserbase Tool | 透過 Composio / Rube MCP 自動化 Browserbase Tool 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/browserbase-tool-automation/SKILL.md` |
| 129 | `browserhub-automation` | Browserhub | 透過 Composio / Rube MCP 自動化 Browserhub 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/browserhub-automation/SKILL.md` |
| 130 | `browserless-automation` | Browserless | 透過 Composio / Rube MCP 自動化 Browserless 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/browserless-automation/SKILL.md` |
| 131 | `btcpay-server-automation` | Btcpay Server | 透過 Composio / Rube MCP 自動化 Btcpay Server 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/btcpay-server-automation/SKILL.md` |
| 132 | `bubble-automation` | Bubble | 透過 Composio / Rube MCP 自動化 Bubble 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/bubble-automation/SKILL.md` |
| 133 | `bugbug-automation` | Bugbug | 透過 Composio / Rube MCP 自動化 Bugbug 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/bugbug-automation/SKILL.md` |
| 134 | `bugherd-automation` | Bugherd | 透過 Composio / Rube MCP 自動化 Bugherd 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/bugherd-automation/SKILL.md` |
| 135 | `bugsnag-automation` | Bugsnag | 透過 Composio / Rube MCP 自動化 Bugsnag 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/bugsnag-automation/SKILL.md` |
| 136 | `buildkite-automation` | Buildkite | 透過 Composio / Rube MCP 自動化 Buildkite 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/buildkite-automation/SKILL.md` |
| 137 | `builtwith-automation` | Builtwith | 透過 Composio / Rube MCP 自動化 Builtwith 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/builtwith-automation/SKILL.md` |
| 138 | `bunnycdn-automation` | Bunnycdn | 透過 Composio / Rube MCP 自動化 Bunnycdn 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/bunnycdn-automation/SKILL.md` |
| 139 | `byteforms-automation` | Byteforms | 透過 Composio / Rube MCP 自動化 Byteforms 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/byteforms-automation/SKILL.md` |
| 140 | `cabinpanda-automation` | Cabinpanda | 透過 Composio / Rube MCP 自動化 Cabinpanda 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/cabinpanda-automation/SKILL.md` |
| 141 | `cal-automation` | Cal | 透過 Composio / Rube MCP 自動化 Cal 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/cal-automation/SKILL.md` |
| 142 | `calendarhero-automation` | Calendarhero | 透過 Composio / Rube MCP 自動化 Calendarhero 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/calendarhero-automation/SKILL.md` |
| 143 | `callerapi-automation` | Callerapi | 透過 Composio / Rube MCP 自動化 Callerapi 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/callerapi-automation/SKILL.md` |
| 144 | `callingly-automation` | Callingly | 透過 Composio / Rube MCP 自動化 Callingly 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/callingly-automation/SKILL.md` |
| 145 | `callpage-automation` | Callpage | 透過 Composio / Rube MCP 自動化 Callpage 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/callpage-automation/SKILL.md` |
| 146 | `campaign-cleaner-automation` | Campaign Cleaner | 透過 Composio / Rube MCP 自動化 Campaign Cleaner 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/campaign-cleaner-automation/SKILL.md` |
| 147 | `campayn-automation` | Campayn | 透過 Composio / Rube MCP 自動化 Campayn 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/campayn-automation/SKILL.md` |
| 148 | `canny-automation` | Canny | 透過 Composio / Rube MCP 自動化 Canny 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/canny-automation/SKILL.md` |
| 149 | `canvas-automation` | Canvas | 透過 Composio / Rube MCP 自動化 Canvas 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/canvas-automation/SKILL.md` |
| 150 | `Capsule CRM Automation` | Capsule CRM | 透過 Composio / Rube MCP 自動化 Capsule CRM 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/capsule-crm-automation/SKILL.md` |
| 151 | `capsule_crm-automation` | Capsule CRM | 透過 Composio / Rube MCP 自動化 Capsule CRM 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/capsule_crm-automation/SKILL.md` |
| 152 | `carbone-automation` | Carbone | 透過 Composio / Rube MCP 自動化 Carbone 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/carbone-automation/SKILL.md` |
| 153 | `cardly-automation` | Cardly | 透過 Composio / Rube MCP 自動化 Cardly 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/cardly-automation/SKILL.md` |
| 154 | `castingwords-automation` | Castingwords | 透過 Composio / Rube MCP 自動化 Castingwords 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/castingwords-automation/SKILL.md` |
| 155 | `cats-automation` | Cats | 透過 Composio / Rube MCP 自動化 Cats 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/cats-automation/SKILL.md` |
| 156 | `cdr-platform-automation` | Cdr Platform | 透過 Composio / Rube MCP 自動化 Cdr Platform 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/cdr-platform-automation/SKILL.md` |
| 157 | `census-bureau-automation` | Census Bureau | 透過 Composio / Rube MCP 自動化 Census Bureau 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/census-bureau-automation/SKILL.md` |
| 158 | `centralstationcrm-automation` | Centralstationcrm | 透過 Composio / Rube MCP 自動化 Centralstationcrm 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/centralstationcrm-automation/SKILL.md` |
| 159 | `certifier-automation` | Certifier | 透過 Composio / Rube MCP 自動化 Certifier 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/certifier-automation/SKILL.md` |
| 160 | `chaser-automation` | Chaser | 透過 Composio / Rube MCP 自動化 Chaser 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/chaser-automation/SKILL.md` |
| 161 | `chatbotkit-automation` | Chatbotkit | 透過 Composio / Rube MCP 自動化 Chatbotkit 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/chatbotkit-automation/SKILL.md` |
| 162 | `chatfai-automation` | Chatfai | 透過 Composio / Rube MCP 自動化 Chatfai 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/chatfai-automation/SKILL.md` |
| 163 | `chatwork-automation` | Chatwork | 透過 Composio / Rube MCP 自動化 Chatwork 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/chatwork-automation/SKILL.md` |
| 164 | `chmeetings-automation` | Chmeetings | 透過 Composio / Rube MCP 自動化 Chmeetings 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/chmeetings-automation/SKILL.md` |
| 165 | `cincopa-automation` | Cincopa | 透過 Composio / Rube MCP 自動化 Cincopa 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/cincopa-automation/SKILL.md` |
| 166 | `claid-ai-automation` | Claid AI | 透過 Composio / Rube MCP 自動化 Claid AI 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/claid-ai-automation/SKILL.md` |
| 167 | `classmarker-automation` | Classmarker | 透過 Composio / Rube MCP 自動化 Classmarker 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/classmarker-automation/SKILL.md` |
| 168 | `clearout-automation` | Clearout | 透過 Composio / Rube MCP 自動化 Clearout 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/clearout-automation/SKILL.md` |
| 169 | `clickmeeting-automation` | Clickmeeting | 透過 Composio / Rube MCP 自動化 Clickmeeting 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/clickmeeting-automation/SKILL.md` |
| 170 | `Clockify Automation` | Clockify | 透過 Composio / Rube MCP 自動化 Clockify 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/clockify-automation/SKILL.md` |
| 171 | `cloudcart-automation` | Cloudcart | 透過 Composio / Rube MCP 自動化 Cloudcart 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/cloudcart-automation/SKILL.md` |
| 172 | `cloudconvert-automation` | Cloudconvert | 透過 Composio / Rube MCP 自動化 Cloudconvert 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/cloudconvert-automation/SKILL.md` |
| 173 | `cloudflare-api-key-automation` | Cloudflare API Key | 透過 Composio / Rube MCP 自動化 Cloudflare API Key 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/cloudflare-api-key-automation/SKILL.md` |
| 174 | `cloudflare-automation` | Cloudflare | 透過 Composio / Rube MCP 自動化 Cloudflare 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/cloudflare-automation/SKILL.md` |
| 175 | `cloudflare-browser-rendering-automation` | Cloudflare Browser Rendering | 透過 Composio / Rube MCP 自動化 Cloudflare Browser Rendering 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/cloudflare-browser-rendering-automation/SKILL.md` |
| 176 | `Cloudinary Automation` | Cloudinary | 透過 Composio / Rube MCP 自動化 Cloudinary 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/cloudinary-automation/SKILL.md` |
| 177 | `cloudlayer-automation` | Cloudlayer | 透過 Composio / Rube MCP 自動化 Cloudlayer 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/cloudlayer-automation/SKILL.md` |
| 178 | `cloudpress-automation` | Cloudpress | 透過 Composio / Rube MCP 自動化 Cloudpress 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/cloudpress-automation/SKILL.md` |
| 179 | `coassemble-automation` | Coassemble | 透過 Composio / Rube MCP 自動化 Coassemble 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/coassemble-automation/SKILL.md` |
| 180 | `codacy-automation` | Codacy | 透過 Composio / Rube MCP 自動化 Codacy 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/codacy-automation/SKILL.md` |
| 181 | `codeinterpreter-automation` | Codeinterpreter | 透過 Composio / Rube MCP 自動化 Codeinterpreter 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/codeinterpreter-automation/SKILL.md` |
| 182 | `codereadr-automation` | Codereadr | 透過 Composio / Rube MCP 自動化 Codereadr 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/codereadr-automation/SKILL.md` |
| 183 | `Coinbase Automation` | Coinbase | 透過 Composio / Rube MCP 自動化 Coinbase 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/coinbase-automation/SKILL.md` |
| 184 | `coinmarketcal-automation` | Coinmarketcal | 透過 Composio / Rube MCP 自動化 Coinmarketcal 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/coinmarketcal-automation/SKILL.md` |
| 185 | `coinmarketcap-automation` | Coinmarketcap | 透過 Composio / Rube MCP 自動化 Coinmarketcap 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/coinmarketcap-automation/SKILL.md` |
| 186 | `coinranking-automation` | Coinranking | 透過 Composio / Rube MCP 自動化 Coinranking 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/coinranking-automation/SKILL.md` |
| 187 | `college-football-data-automation` | College Football Data | 透過 Composio / Rube MCP 自動化 College Football Data 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/college-football-data-automation/SKILL.md` |
| 188 | `composio-automation` | Composio | 透過 Composio / Rube MCP 自動化 Composio 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/composio-automation/SKILL.md` |
| 189 | `composio-search-automation` | Composio Search | 透過 Composio / Rube MCP 自動化 Composio Search 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/composio-search-automation/SKILL.md` |
| 190 | `connecteam-automation` | Connecteam | 透過 Composio / Rube MCP 自動化 Connecteam 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/connecteam-automation/SKILL.md` |
| 191 | `Contentful Automation` | Contentful | 透過 Composio / Rube MCP 自動化 Contentful 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/contentful-automation/SKILL.md` |
| 192 | `contentful-graphql-automation` | Contentful Graphql | 透過 Composio / Rube MCP 自動化 Contentful Graphql 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/contentful-graphql-automation/SKILL.md` |
| 193 | `control-d-automation` | Control D | 透過 Composio / Rube MCP 自動化 Control D 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/control-d-automation/SKILL.md` |
| 194 | `conversion-tools-automation` | Conversion Tools | 透過 Composio / Rube MCP 自動化 Conversion Tools 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/conversion-tools-automation/SKILL.md` |
| 195 | `convertapi-automation` | Convertapi | 透過 Composio / Rube MCP 自動化 Convertapi 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/convertapi-automation/SKILL.md` |
| 196 | `conveyor-automation` | Conveyor | 透過 Composio / Rube MCP 自動化 Conveyor 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/conveyor-automation/SKILL.md` |
| 197 | `convolo-ai-automation` | Convolo AI | 透過 Composio / Rube MCP 自動化 Convolo AI 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/convolo-ai-automation/SKILL.md` |
| 198 | `corrently-automation` | Corrently | 透過 Composio / Rube MCP 自動化 Corrently 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/corrently-automation/SKILL.md` |
| 199 | `countdown-api-automation` | Countdown API | 透過 Composio / Rube MCP 自動化 Countdown API 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/countdown-api-automation/SKILL.md` |
| 200 | `coupa-automation` | Coupa | 透過 Composio / Rube MCP 自動化 Coupa 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/coupa-automation/SKILL.md` |
| 201 | `craftmypdf-automation` | Craftmypdf | 透過 Composio / Rube MCP 自動化 Craftmypdf 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/craftmypdf-automation/SKILL.md` |
| 202 | `crowdin-automation` | Crowdin | 透過 Composio / Rube MCP 自動化 Crowdin 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/crowdin-automation/SKILL.md` |
| 203 | `crustdata-automation` | Crustdata | 透過 Composio / Rube MCP 自動化 Crustdata 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/crustdata-automation/SKILL.md` |
| 204 | `cults-automation` | Cults | 透過 Composio / Rube MCP 自動化 Cults 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/cults-automation/SKILL.md` |
| 205 | `curated-automation` | Curated | 透過 Composio / Rube MCP 自動化 Curated 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/curated-automation/SKILL.md` |
| 206 | `currents-api-automation` | Currents API | 透過 Composio / Rube MCP 自動化 Currents API 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/currents-api-automation/SKILL.md` |
| 207 | `Customer.io Automation` | Customerio | 透過 Composio / Rube MCP 自動化 Customerio 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/customerio-automation/SKILL.md` |
| 208 | `customgpt-automation` | Customgpt | 透過 Composio / Rube MCP 自動化 Customgpt 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/customgpt-automation/SKILL.md` |
| 209 | `customjs-automation` | Customjs | 透過 Composio / Rube MCP 自動化 Customjs 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/customjs-automation/SKILL.md` |
| 210 | `cutt-ly-automation` | Cutt Ly | 透過 Composio / Rube MCP 自動化 Cutt Ly 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/cutt-ly-automation/SKILL.md` |
| 211 | `d2lbrightspace-automation` | D2lbrightspace | 透過 Composio / Rube MCP 自動化 D2lbrightspace 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/d2lbrightspace-automation/SKILL.md` |
| 212 | `dadata-ru-automation` | Dadata Ru | 透過 Composio / Rube MCP 自動化 Dadata Ru 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/dadata-ru-automation/SKILL.md` |
| 213 | `daffy-automation` | Daffy | 透過 Composio / Rube MCP 自動化 Daffy 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/daffy-automation/SKILL.md` |
| 214 | `dailybot-automation` | Dailybot | 透過 Composio / Rube MCP 自動化 Dailybot 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/dailybot-automation/SKILL.md` |
| 215 | `datagma-automation` | Datagma | 透過 Composio / Rube MCP 自動化 Datagma 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/datagma-automation/SKILL.md` |
| 216 | `datarobot-automation` | Datarobot | 透過 Composio / Rube MCP 自動化 Datarobot 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/datarobot-automation/SKILL.md` |
| 217 | `deadline-funnel-automation` | Deadline Funnel | 透過 Composio / Rube MCP 自動化 Deadline Funnel 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/deadline-funnel-automation/SKILL.md` |
| 218 | `deel-automation` | Deel | 透過 Composio / Rube MCP 自動化 Deel 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/deel-automation/SKILL.md` |
| 219 | `deepgram-automation` | Deepgram | 透過 Composio / Rube MCP 自動化 Deepgram 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/deepgram-automation/SKILL.md` |
| 220 | `demio-automation` | Demio | 透過 Composio / Rube MCP 自動化 Demio 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/demio-automation/SKILL.md` |
| 221 | `desktime-automation` | Desktime | 透過 Composio / Rube MCP 自動化 Desktime 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/desktime-automation/SKILL.md` |
| 222 | `detrack-automation` | Detrack | 透過 Composio / Rube MCP 自動化 Detrack 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/detrack-automation/SKILL.md` |
| 223 | `dialmycalls-automation` | Dialmycalls | 透過 Composio / Rube MCP 自動化 Dialmycalls 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/dialmycalls-automation/SKILL.md` |
| 224 | `dialpad-automation` | Dialpad | 透過 Composio / Rube MCP 自動化 Dialpad 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/dialpad-automation/SKILL.md` |
| 225 | `dictionary-api-automation` | Dictionary API | 透過 Composio / Rube MCP 自動化 Dictionary API 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/dictionary-api-automation/SKILL.md` |
| 226 | `diffbot-automation` | Diffbot | 透過 Composio / Rube MCP 自動化 Diffbot 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/diffbot-automation/SKILL.md` |
| 227 | `digicert-automation` | Digicert | 透過 Composio / Rube MCP 自動化 Digicert 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/digicert-automation/SKILL.md` |
| 228 | `digital-ocean-automation` | Digital Ocean | 透過 Composio / Rube MCP 自動化 Digital Ocean 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/digital-ocean-automation/SKILL.md` |
| 229 | `discordbot-automation` | Discordbot | 透過 Composio / Rube MCP 自動化 Discordbot 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/discordbot-automation/SKILL.md` |
| 230 | `dnsfilter-automation` | Dnsfilter | 透過 Composio / Rube MCP 自動化 Dnsfilter 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/dnsfilter-automation/SKILL.md` |
| 231 | `dock-certs-automation` | Dock Certs | 透過 Composio / Rube MCP 自動化 Dock Certs 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/dock-certs-automation/SKILL.md` |
| 232 | `Docker Hub Automation` | Docker Hub | 透過 Composio / Rube MCP 自動化 Docker Hub 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/docker-hub-automation/SKILL.md` |
| 233 | `docker_hub-automation` | Docker Hub | 透過 Composio / Rube MCP 自動化 Docker Hub 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/docker_hub-automation/SKILL.md` |
| 234 | `docmosis-automation` | Docmosis | 透過 Composio / Rube MCP 自動化 Docmosis 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/docmosis-automation/SKILL.md` |
| 235 | `docnify-automation` | Docnify | 透過 Composio / Rube MCP 自動化 Docnify 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/docnify-automation/SKILL.md` |
| 236 | `docsbot-ai-automation` | Docsbot AI | 透過 Composio / Rube MCP 自動化 Docsbot AI 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/docsbot-ai-automation/SKILL.md` |
| 237 | `docsumo-automation` | Docsumo | 透過 Composio / Rube MCP 自動化 Docsumo 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/docsumo-automation/SKILL.md` |
| 238 | `docugenerate-automation` | Docugenerate | 透過 Composio / Rube MCP 自動化 Docugenerate 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/docugenerate-automation/SKILL.md` |
| 239 | `documenso-automation` | Documenso | 透過 Composio / Rube MCP 自動化 Documenso 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/documenso-automation/SKILL.md` |
| 240 | `documint-automation` | Documint | 透過 Composio / Rube MCP 自動化 Documint 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/documint-automation/SKILL.md` |
| 241 | `docupilot-automation` | Docupilot | 透過 Composio / Rube MCP 自動化 Docupilot 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/docupilot-automation/SKILL.md` |
| 242 | `docupost-automation` | Docupost | 透過 Composio / Rube MCP 自動化 Docupost 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/docupost-automation/SKILL.md` |
| 243 | `docuseal-automation` | Docuseal | 透過 Composio / Rube MCP 自動化 Docuseal 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/docuseal-automation/SKILL.md` |
| 244 | `doppler-marketing-automation-automation` | Doppler Marketing Automation | 透過 Composio / Rube MCP 自動化 Doppler Marketing Automation 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/doppler-marketing-automation-automation/SKILL.md` |
| 245 | `doppler-secretops-automation` | Doppler Secretops | 透過 Composio / Rube MCP 自動化 Doppler Secretops 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/doppler-secretops-automation/SKILL.md` |
| 246 | `dotsimple-automation` | Dotsimple | 透過 Composio / Rube MCP 自動化 Dotsimple 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/dotsimple-automation/SKILL.md` |
| 247 | `dovetail-automation` | Dovetail | 透過 Composio / Rube MCP 自動化 Dovetail 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/dovetail-automation/SKILL.md` |
| 248 | `dpd2-automation` | Dpd2 | 透過 Composio / Rube MCP 自動化 Dpd2 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/dpd2-automation/SKILL.md` |
| 249 | `draftable-automation` | Draftable | 透過 Composio / Rube MCP 自動化 Draftable 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/draftable-automation/SKILL.md` |
| 250 | `dreamstudio-automation` | Dreamstudio | 透過 Composio / Rube MCP 自動化 Dreamstudio 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/dreamstudio-automation/SKILL.md` |
| 251 | `drip-jobs-automation` | Drip Jobs | 透過 Composio / Rube MCP 自動化 Drip Jobs 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/drip-jobs-automation/SKILL.md` |
| 252 | `dripcel-automation` | Dripcel | 透過 Composio / Rube MCP 自動化 Dripcel 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/dripcel-automation/SKILL.md` |
| 253 | `dromo-automation` | Dromo | 透過 Composio / Rube MCP 自動化 Dromo 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/dromo-automation/SKILL.md` |
| 254 | `dropbox-sign-automation` | Dropbox Sign | 透過 Composio / Rube MCP 自動化 Dropbox Sign 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/dropbox-sign-automation/SKILL.md` |
| 255 | `dropcontact-automation` | Dropcontact | 透過 Composio / Rube MCP 自動化 Dropcontact 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/dropcontact-automation/SKILL.md` |
| 256 | `dungeon-fighter-online-automation` | Dungeon Fighter Online | 透過 Composio / Rube MCP 自動化 Dungeon Fighter Online 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/dungeon-fighter-online-automation/SKILL.md` |
| 257 | `Dynamics 365 Automation` | Dynamics365 | 透過 Composio / Rube MCP 自動化 Dynamics365 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/dynamics365-automation/SKILL.md` |
| 258 | `echtpost-automation` | Echtpost | 透過 Composio / Rube MCP 自動化 Echtpost 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/echtpost-automation/SKILL.md` |
| 259 | `ElevenLabs Automation` | ElevenLabs | 透過 Composio / Rube MCP 自動化 ElevenLabs 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/elevenlabs-automation/SKILL.md` |
| 260 | `elorus-automation` | Elorus | 透過 Composio / Rube MCP 自動化 Elorus 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/elorus-automation/SKILL.md` |
| 261 | `emailable-automation` | Emailable | 透過 Composio / Rube MCP 自動化 Emailable 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/emailable-automation/SKILL.md` |
| 262 | `emaillistverify-automation` | Emaillistverify | 透過 Composio / Rube MCP 自動化 Emaillistverify 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/emaillistverify-automation/SKILL.md` |
| 263 | `emailoctopus-automation` | Emailoctopus | 透過 Composio / Rube MCP 自動化 Emailoctopus 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/emailoctopus-automation/SKILL.md` |
| 264 | `emelia-automation` | Emelia | 透過 Composio / Rube MCP 自動化 Emelia 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/emelia-automation/SKILL.md` |
| 265 | `encodian-automation` | Encodian | 透過 Composio / Rube MCP 自動化 Encodian 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/encodian-automation/SKILL.md` |
| 266 | `endorsal-automation` | Endorsal | 透過 Composio / Rube MCP 自動化 Endorsal 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/endorsal-automation/SKILL.md` |
| 267 | `enginemailer-automation` | Enginemailer | 透過 Composio / Rube MCP 自動化 Enginemailer 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/enginemailer-automation/SKILL.md` |
| 268 | `enigma-automation` | Enigma | 透過 Composio / Rube MCP 自動化 Enigma 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/enigma-automation/SKILL.md` |
| 269 | `entelligence-automation` | Entelligence | 透過 Composio / Rube MCP 自動化 Entelligence 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/entelligence-automation/SKILL.md` |
| 270 | `eodhd-apis-automation` | Eodhd Apis | 透過 Composio / Rube MCP 自動化 Eodhd Apis 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/eodhd-apis-automation/SKILL.md` |
| 271 | `epic-games-automation` | Epic Games | 透過 Composio / Rube MCP 自動化 Epic Games 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/epic-games-automation/SKILL.md` |
| 272 | `esignatures-io-automation` | Esignatures IO | 透過 Composio / Rube MCP 自動化 Esignatures IO 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/esignatures-io-automation/SKILL.md` |
| 273 | `espocrm-automation` | Espocrm | 透過 Composio / Rube MCP 自動化 Espocrm 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/espocrm-automation/SKILL.md` |
| 274 | `esputnik-automation` | Esputnik | 透過 Composio / Rube MCP 自動化 Esputnik 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/esputnik-automation/SKILL.md` |
| 275 | `etermin-automation` | Etermin | 透過 Composio / Rube MCP 自動化 Etermin 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/etermin-automation/SKILL.md` |
| 276 | `evenium-automation` | Evenium | 透過 Composio / Rube MCP 自動化 Evenium 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/evenium-automation/SKILL.md` |
| 277 | `Eventbrite Automation` | Eventbrite | 透過 Composio / Rube MCP 自動化 Eventbrite 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/eventbrite-automation/SKILL.md` |
| 278 | `eventee-automation` | Eventee | 透過 Composio / Rube MCP 自動化 Eventee 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/eventee-automation/SKILL.md` |
| 279 | `eventzilla-automation` | Eventzilla | 透過 Composio / Rube MCP 自動化 Eventzilla 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/eventzilla-automation/SKILL.md` |
| 280 | `everhour-automation` | Everhour | 透過 Composio / Rube MCP 自動化 Everhour 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/everhour-automation/SKILL.md` |
| 281 | `eversign-automation` | Eversign | 透過 Composio / Rube MCP 自動化 Eversign 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/eversign-automation/SKILL.md` |
| 282 | `exa-automation` | Exa | 透過 Composio / Rube MCP 自動化 Exa 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/exa-automation/SKILL.md` |
| 283 | `Excel Automation` | Excel | 透過 Composio / Rube MCP 自動化 Excel 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/excel-automation/SKILL.md` |
| 284 | `exist-automation` | Exist | 透過 Composio / Rube MCP 自動化 Exist 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/exist-automation/SKILL.md` |
| 285 | `expofp-automation` | Expofp | 透過 Composio / Rube MCP 自動化 Expofp 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/expofp-automation/SKILL.md` |
| 286 | `extracta-ai-automation` | Extracta AI | 透過 Composio / Rube MCP 自動化 Extracta AI 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/extracta-ai-automation/SKILL.md` |
| 287 | `Facebook Automation` | Facebook | 透過 Composio / Rube MCP 自動化 Facebook 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/facebook-automation/SKILL.md` |
| 288 | `faceup-automation` | Faceup | 透過 Composio / Rube MCP 自動化 Faceup 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/faceup-automation/SKILL.md` |
| 289 | `factorial-automation` | Factorial | 透過 Composio / Rube MCP 自動化 Factorial 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/factorial-automation/SKILL.md` |
| 290 | `feathery-automation` | Feathery | 透過 Composio / Rube MCP 自動化 Feathery 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/feathery-automation/SKILL.md` |
| 291 | `felt-automation` | Felt | 透過 Composio / Rube MCP 自動化 Felt 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/felt-automation/SKILL.md` |
| 292 | `fibery-automation` | Fibery | 透過 Composio / Rube MCP 自動化 Fibery 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/fibery-automation/SKILL.md` |
| 293 | `fidel-api-automation` | Fidel API | 透過 Composio / Rube MCP 自動化 Fidel API 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/fidel-api-automation/SKILL.md` |
| 294 | `files-com-automation` | Files Com | 透過 Composio / Rube MCP 自動化 Files Com 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/files-com-automation/SKILL.md` |
| 295 | `fillout-forms-automation` | Fillout Forms | 透過 Composio / Rube MCP 自動化 Fillout Forms 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/fillout-forms-automation/SKILL.md` |
| 296 | `fillout_forms-automation` | Fillout Forms | 透過 Composio / Rube MCP 自動化 Fillout Forms 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/fillout_forms-automation/SKILL.md` |
| 297 | `finage-automation` | Finage | 透過 Composio / Rube MCP 自動化 Finage 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/finage-automation/SKILL.md` |
| 298 | `findymail-automation` | Findymail | 透過 Composio / Rube MCP 自動化 Findymail 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/findymail-automation/SKILL.md` |
| 299 | `finerworks-automation` | Finerworks | 透過 Composio / Rube MCP 自動化 Finerworks 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/finerworks-automation/SKILL.md` |
| 300 | `fingertip-automation` | Fingertip | 透過 Composio / Rube MCP 自動化 Fingertip 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/fingertip-automation/SKILL.md` |
| 301 | `finmei-automation` | Finmei | 透過 Composio / Rube MCP 自動化 Finmei 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/finmei-automation/SKILL.md` |
| 302 | `fireberry-automation` | Fireberry | 透過 Composio / Rube MCP 自動化 Fireberry 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/fireberry-automation/SKILL.md` |
| 303 | `Firecrawl Automation` | Firecrawl | 透過 Composio / Rube MCP 自動化 Firecrawl 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/firecrawl-automation/SKILL.md` |
| 304 | `fireflies-automation` | Fireflies | 透過 Composio / Rube MCP 自動化 Fireflies 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/fireflies-automation/SKILL.md` |
| 305 | `firmao-automation` | Firmao | 透過 Composio / Rube MCP 自動化 Firmao 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/firmao-automation/SKILL.md` |
| 306 | `fitbit-automation` | Fitbit | 透過 Composio / Rube MCP 自動化 Fitbit 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/fitbit-automation/SKILL.md` |
| 307 | `fixer-automation` | Fixer | 透過 Composio / Rube MCP 自動化 Fixer 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/fixer-automation/SKILL.md` |
| 308 | `fixer-io-automation` | Fixer IO | 透過 Composio / Rube MCP 自動化 Fixer IO 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/fixer-io-automation/SKILL.md` |
| 309 | `flexisign-automation` | Flexisign | 透過 Composio / Rube MCP 自動化 Flexisign 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/flexisign-automation/SKILL.md` |
| 310 | `flowiseai-automation` | Flowiseai | 透過 Composio / Rube MCP 自動化 Flowiseai 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/flowiseai-automation/SKILL.md` |
| 311 | `flutterwave-automation` | Flutterwave | 透過 Composio / Rube MCP 自動化 Flutterwave 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/flutterwave-automation/SKILL.md` |
| 312 | `fluxguard-automation` | Fluxguard | 透過 Composio / Rube MCP 自動化 Fluxguard 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/fluxguard-automation/SKILL.md` |
| 313 | `folk-automation` | Folk | 透過 Composio / Rube MCP 自動化 Folk 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/folk-automation/SKILL.md` |
| 314 | `fomo-automation` | Fomo | 透過 Composio / Rube MCP 自動化 Fomo 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/fomo-automation/SKILL.md` |
| 315 | `forcemanager-automation` | Forcemanager | 透過 Composio / Rube MCP 自動化 Forcemanager 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/forcemanager-automation/SKILL.md` |
| 316 | `formbricks-automation` | Formbricks | 透過 Composio / Rube MCP 自動化 Formbricks 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/formbricks-automation/SKILL.md` |
| 317 | `formcarry-automation` | Formcarry | 透過 Composio / Rube MCP 自動化 Formcarry 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/formcarry-automation/SKILL.md` |
| 318 | `formdesk-automation` | Formdesk | 透過 Composio / Rube MCP 自動化 Formdesk 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/formdesk-automation/SKILL.md` |
| 319 | `formsite-automation` | Formsite | 透過 Composio / Rube MCP 自動化 Formsite 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/formsite-automation/SKILL.md` |
| 320 | `foursquare-automation` | Foursquare | 透過 Composio / Rube MCP 自動化 Foursquare 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/foursquare-automation/SKILL.md` |
| 321 | `fraudlabs-pro-automation` | Fraudlabs Pro | 透過 Composio / Rube MCP 自動化 Fraudlabs Pro 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/fraudlabs-pro-automation/SKILL.md` |
| 322 | `FreshBooks Automation` | Freshbooks | 透過 Composio / Rube MCP 自動化 Freshbooks 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/freshbooks-automation/SKILL.md` |
| 323 | `front-automation` | Front | 透過 Composio / Rube MCP 自動化 Front 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/front-automation/SKILL.md` |
| 324 | `fullenrich-automation` | Fullenrich | 透過 Composio / Rube MCP 自動化 Fullenrich 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/fullenrich-automation/SKILL.md` |
| 325 | `gagelist-automation` | Gagelist | 透過 Composio / Rube MCP 自動化 Gagelist 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/gagelist-automation/SKILL.md` |
| 326 | `gamma-automation` | Gamma | 透過 Composio / Rube MCP 自動化 Gamma 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/gamma-automation/SKILL.md` |
| 327 | `gan-ai-automation` | Gan AI | 透過 Composio / Rube MCP 自動化 Gan AI 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/gan-ai-automation/SKILL.md` |
| 328 | `gatherup-automation` | Gatherup | 透過 Composio / Rube MCP 自動化 Gatherup 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/gatherup-automation/SKILL.md` |
| 329 | `gemini-automation` | Gemini | 透過 Composio / Rube MCP 自動化 Gemini 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/gemini-automation/SKILL.md` |
| 330 | `gender-api-automation` | Gender API | 透過 Composio / Rube MCP 自動化 Gender API 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/gender-api-automation/SKILL.md` |
| 331 | `genderapi-io-automation` | Genderapi IO | 透過 Composio / Rube MCP 自動化 Genderapi IO 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/genderapi-io-automation/SKILL.md` |
| 332 | `genderize-automation` | Genderize | 透過 Composio / Rube MCP 自動化 Genderize 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/genderize-automation/SKILL.md` |
| 333 | `geoapify-automation` | Geoapify | 透過 Composio / Rube MCP 自動化 Geoapify 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/geoapify-automation/SKILL.md` |
| 334 | `geocodio-automation` | Geocodio | 透過 Composio / Rube MCP 自動化 Geocodio 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/geocodio-automation/SKILL.md` |
| 335 | `geokeo-automation` | Geokeo | 透過 Composio / Rube MCP 自動化 Geokeo 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/geokeo-automation/SKILL.md` |
| 336 | `getform-automation` | Getform | 透過 Composio / Rube MCP 自動化 Getform 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/getform-automation/SKILL.md` |
| 337 | `gift-up-automation` | Gift Up | 透過 Composio / Rube MCP 自動化 Gift Up 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/gift-up-automation/SKILL.md` |
| 338 | `gigasheet-automation` | Gigasheet | 透過 Composio / Rube MCP 自動化 Gigasheet 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/gigasheet-automation/SKILL.md` |
| 339 | `giphy-automation` | Giphy | 透過 Composio / Rube MCP 自動化 Giphy 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/giphy-automation/SKILL.md` |
| 340 | `gist-automation` | Gist | 透過 Composio / Rube MCP 自動化 Gist 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/gist-automation/SKILL.md` |
| 341 | `givebutter-automation` | Givebutter | 透過 Composio / Rube MCP 自動化 Givebutter 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/givebutter-automation/SKILL.md` |
| 342 | `gladia-automation` | Gladia | 透過 Composio / Rube MCP 自動化 Gladia 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/gladia-automation/SKILL.md` |
| 343 | `gleap-automation` | Gleap | 透過 Composio / Rube MCP 自動化 Gleap 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/gleap-automation/SKILL.md` |
| 344 | `globalping-automation` | Globalping | 透過 Composio / Rube MCP 自動化 Globalping 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/globalping-automation/SKILL.md` |
| 345 | `go-to-webinar-automation` | Go To Webinar | 透過 Composio / Rube MCP 自動化 Go To Webinar 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/go-to-webinar-automation/SKILL.md` |
| 346 | `godial-automation` | Godial | 透過 Composio / Rube MCP 自動化 Godial 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/godial-automation/SKILL.md` |
| 347 | `Gong Automation` | Gong | 透過 Composio / Rube MCP 自動化 Gong 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/gong-automation/SKILL.md` |
| 348 | `goodbits-automation` | Goodbits | 透過 Composio / Rube MCP 自動化 Goodbits 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/goodbits-automation/SKILL.md` |
| 349 | `goody-automation` | Goody | 透過 Composio / Rube MCP 自動化 Goody 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/goody-automation/SKILL.md` |
| 350 | `google-address-validation-automation` | Google Address Validation | 透過 Composio / Rube MCP 自動化 Google Address Validation 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/google-address-validation-automation/SKILL.md` |
| 351 | `google-admin-automation` | Google Admin | 透過 Composio / Rube MCP 自動化 Google Admin 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/google-admin-automation/SKILL.md` |
| 352 | `google-classroom-automation` | Google Classroom | 透過 Composio / Rube MCP 自動化 Google Classroom 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/google-classroom-automation/SKILL.md` |
| 353 | `google-cloud-vision-automation` | Google Cloud Vision | 透過 Composio / Rube MCP 自動化 Google Cloud Vision 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/google-cloud-vision-automation/SKILL.md` |
| 354 | `google-maps-automation` | Google Maps | 透過 Composio / Rube MCP 自動化 Google Maps 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/google-maps-automation/SKILL.md` |
| 355 | `google-search-console-automation` | Google Search Console | 透過 Composio / Rube MCP 自動化 Google Search Console 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/google-search-console-automation/SKILL.md` |
| 356 | `google_admin-automation` | Google Admin | 透過 Composio / Rube MCP 自動化 Google Admin 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/google_admin-automation/SKILL.md` |
| 357 | `google_classroom-automation` | Google Classroom | 透過 Composio / Rube MCP 自動化 Google Classroom 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/google_classroom-automation/SKILL.md` |
| 358 | `google_maps-automation` | Google Maps | 透過 Composio / Rube MCP 自動化 Google Maps 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/google_maps-automation/SKILL.md` |
| 359 | `google_search_console-automation` | Google Search Console | 透過 Composio / Rube MCP 自動化 Google Search Console 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/google_search_console-automation/SKILL.md` |
| 360 | `googleads-automation` | Google Ads | 透過 Composio / Rube MCP 自動化 Google Ads 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/googleads-automation/SKILL.md` |
| 361 | `googlebigquery-automation` | Google BigQuery | 透過 Composio / Rube MCP 自動化 Google BigQuery 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/googlebigquery-automation/SKILL.md` |
| 362 | `googlecalendar-automation` | Google Calendar | 透過 Composio / Rube MCP 自動化 Google Calendar 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/googlecalendar-automation/SKILL.md` |
| 363 | `googledocs-automation` | Google Docs | 透過 Composio / Rube MCP 自動化 Google Docs 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/googledocs-automation/SKILL.md` |
| 364 | `googledrive-automation` | Google Drive | 透過 Composio / Rube MCP 自動化 Google Drive 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/googledrive-automation/SKILL.md` |
| 365 | `googlemeet-automation` | Google Meet | 透過 Composio / Rube MCP 自動化 Google Meet 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/googlemeet-automation/SKILL.md` |
| 366 | `googlephotos-automation` | Google Photos | 透過 Composio / Rube MCP 自動化 Google Photos 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/googlephotos-automation/SKILL.md` |
| 367 | `googleslides-automation` | Google Slides | 透過 Composio / Rube MCP 自動化 Google Slides 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/googleslides-automation/SKILL.md` |
| 368 | `googlesuper-automation` | Googlesuper | 透過 Composio / Rube MCP 自動化 Googlesuper 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/googlesuper-automation/SKILL.md` |
| 369 | `googletasks-automation` | Google Tasks | 透過 Composio / Rube MCP 自動化 Google Tasks 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/googletasks-automation/SKILL.md` |
| 370 | `Gorgias Automation` | Gorgias | 透過 Composio / Rube MCP 自動化 Gorgias 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/gorgias-automation/SKILL.md` |
| 371 | `gosquared-automation` | Gosquared | 透過 Composio / Rube MCP 自動化 Gosquared 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/gosquared-automation/SKILL.md` |
| 372 | `grafbase-automation` | Grafbase | 透過 Composio / Rube MCP 自動化 Grafbase 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/grafbase-automation/SKILL.md` |
| 373 | `graphhopper-automation` | Graphhopper | 透過 Composio / Rube MCP 自動化 Graphhopper 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/graphhopper-automation/SKILL.md` |
| 374 | `griptape-automation` | Griptape | 透過 Composio / Rube MCP 自動化 Griptape 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/griptape-automation/SKILL.md` |
| 375 | `grist-automation` | Grist | 透過 Composio / Rube MCP 自動化 Grist 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/grist-automation/SKILL.md` |
| 376 | `GroqCloud Automation` | Groqcloud | 透過 Composio / Rube MCP 自動化 Groqcloud 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/groqcloud-automation/SKILL.md` |
| 377 | `Gumroad Automation` | Gumroad | 透過 Composio / Rube MCP 自動化 Gumroad 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/gumroad-automation/SKILL.md` |
| 378 | `habitica-automation` | Habitica | 透過 Composio / Rube MCP 自動化 Habitica 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/habitica-automation/SKILL.md` |
| 379 | `hackernews-automation` | Hackernews | 透過 Composio / Rube MCP 自動化 Hackernews 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/hackernews-automation/SKILL.md` |
| 380 | `happy-scribe-automation` | Happy Scribe | 透過 Composio / Rube MCP 自動化 Happy Scribe 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/happy-scribe-automation/SKILL.md` |
| 381 | `Harvest Automation` | Harvest | 透過 Composio / Rube MCP 自動化 Harvest 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/harvest-automation/SKILL.md` |
| 382 | `hashnode-automation` | Hashnode | 透過 Composio / Rube MCP 自動化 Hashnode 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/hashnode-automation/SKILL.md` |
| 383 | `helcim-automation` | Helcim | 透過 Composio / Rube MCP 自動化 Helcim 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/helcim-automation/SKILL.md` |
| 384 | `helloleads-automation` | Helloleads | 透過 Composio / Rube MCP 自動化 Helloleads 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/helloleads-automation/SKILL.md` |
| 385 | `helpwise-automation` | Helpwise | 透過 Composio / Rube MCP 自動化 Helpwise 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/helpwise-automation/SKILL.md` |
| 386 | `here-automation` | Here | 透過 Composio / Rube MCP 自動化 Here 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/here-automation/SKILL.md` |
| 387 | `HeyGen Automation` | Heygen | 透過 Composio / Rube MCP 自動化 Heygen 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/heygen-automation/SKILL.md` |
| 388 | `heyreach-automation` | Heyreach | 透過 Composio / Rube MCP 自動化 Heyreach 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/heyreach-automation/SKILL.md` |
| 389 | `heyzine-automation` | Heyzine | 透過 Composio / Rube MCP 自動化 Heyzine 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/heyzine-automation/SKILL.md` |
| 390 | `highergov-automation` | Highergov | 透過 Composio / Rube MCP 自動化 Highergov 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/highergov-automation/SKILL.md` |
| 391 | `highlevel-automation` | Highlevel | 透過 Composio / Rube MCP 自動化 Highlevel 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/highlevel-automation/SKILL.md` |
| 392 | `honeybadger-automation` | Honeybadger | 透過 Composio / Rube MCP 自動化 Honeybadger 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/honeybadger-automation/SKILL.md` |
| 393 | `honeyhive-automation` | Honeyhive | 透過 Composio / Rube MCP 自動化 Honeyhive 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/honeyhive-automation/SKILL.md` |
| 394 | `hookdeck-automation` | Hookdeck | 透過 Composio / Rube MCP 自動化 Hookdeck 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/hookdeck-automation/SKILL.md` |
| 395 | `hotspotsystem-automation` | Hotspotsystem | 透過 Composio / Rube MCP 自動化 Hotspotsystem 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/hotspotsystem-automation/SKILL.md` |
| 396 | `html-to-image-automation` | Html To Image | 透過 Composio / Rube MCP 自動化 Html To Image 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/html-to-image-automation/SKILL.md` |
| 397 | `humanitix-automation` | Humanitix | 透過 Composio / Rube MCP 自動化 Humanitix 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/humanitix-automation/SKILL.md` |
| 398 | `humanloop-automation` | Humanloop | 透過 Composio / Rube MCP 自動化 Humanloop 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/humanloop-automation/SKILL.md` |
| 399 | `Hunter Automation` | Hunter | 透過 Composio / Rube MCP 自動化 Hunter 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/hunter-automation/SKILL.md` |
| 400 | `hypeauditor-automation` | Hypeauditor | 透過 Composio / Rube MCP 自動化 Hypeauditor 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/hypeauditor-automation/SKILL.md` |
| 401 | `hyperbrowser-automation` | Hyperbrowser | 透過 Composio / Rube MCP 自動化 Hyperbrowser 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/hyperbrowser-automation/SKILL.md` |
| 402 | `hyperise-automation` | Hyperise | 透過 Composio / Rube MCP 自動化 Hyperise 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/hyperise-automation/SKILL.md` |
| 403 | `hystruct-automation` | Hystruct | 透過 Composio / Rube MCP 自動化 Hystruct 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/hystruct-automation/SKILL.md` |
| 404 | `icims-talent-cloud-automation` | Icims Talent Cloud | 透過 Composio / Rube MCP 自動化 Icims Talent Cloud 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/icims-talent-cloud-automation/SKILL.md` |
| 405 | `icypeas-automation` | Icypeas | 透過 Composio / Rube MCP 自動化 Icypeas 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/icypeas-automation/SKILL.md` |
| 406 | `idea-scale-automation` | Idea Scale | 透過 Composio / Rube MCP 自動化 Idea Scale 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/idea-scale-automation/SKILL.md` |
| 407 | `identitycheck-automation` | Identitycheck | 透過 Composio / Rube MCP 自動化 Identitycheck 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/identitycheck-automation/SKILL.md` |
| 408 | `ignisign-automation` | Ignisign | 透過 Composio / Rube MCP 自動化 Ignisign 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/ignisign-automation/SKILL.md` |
| 409 | `imagekit-io-automation` | Imagekit IO | 透過 Composio / Rube MCP 自動化 Imagekit IO 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/imagekit-io-automation/SKILL.md` |
| 410 | `imgbb-automation` | Imgbb | 透過 Composio / Rube MCP 自動化 Imgbb 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/imgbb-automation/SKILL.md` |
| 411 | `imgix-automation` | Imgix | 透過 Composio / Rube MCP 自動化 Imgix 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/imgix-automation/SKILL.md` |
| 412 | `influxdb-cloud-automation` | Influxdb Cloud | 透過 Composio / Rube MCP 自動化 Influxdb Cloud 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/influxdb-cloud-automation/SKILL.md` |
| 413 | `insighto-ai-automation` | Insighto AI | 透過 Composio / Rube MCP 自動化 Insighto AI 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/insighto-ai-automation/SKILL.md` |
| 414 | `instacart-automation` | Instacart | 透過 Composio / Rube MCP 自動化 Instacart 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/instacart-automation/SKILL.md` |
| 415 | `Instantly Automation` | Instantly | 透過 Composio / Rube MCP 自動化 Instantly 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/instantly-automation/SKILL.md` |
| 416 | `intelliprint-automation` | Intelliprint | 透過 Composio / Rube MCP 自動化 Intelliprint 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/intelliprint-automation/SKILL.md` |
| 417 | `interzoid-automation` | Interzoid | 透過 Composio / Rube MCP 自動化 Interzoid 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/interzoid-automation/SKILL.md` |
| 418 | `ip2location-automation` | Ip2location | 透過 Composio / Rube MCP 自動化 Ip2location 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/ip2location-automation/SKILL.md` |
| 419 | `ip2location-io-automation` | Ip2location IO | 透過 Composio / Rube MCP 自動化 Ip2location IO 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/ip2location-io-automation/SKILL.md` |
| 420 | `ip2proxy-automation` | Ip2proxy | 透過 Composio / Rube MCP 自動化 Ip2proxy 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/ip2proxy-automation/SKILL.md` |
| 421 | `ip2whois-automation` | Ip2whois | 透過 Composio / Rube MCP 自動化 Ip2whois 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/ip2whois-automation/SKILL.md` |
| 422 | `ipdata-co-automation` | Ipdata Co | 透過 Composio / Rube MCP 自動化 Ipdata Co 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/ipdata-co-automation/SKILL.md` |
| 423 | `ipinfo-io-automation` | Ipinfo IO | 透過 Composio / Rube MCP 自動化 Ipinfo IO 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/ipinfo-io-automation/SKILL.md` |
| 424 | `iqair-airvisual-automation` | Iqair Airvisual | 透過 Composio / Rube MCP 自動化 Iqair Airvisual 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/iqair-airvisual-automation/SKILL.md` |
| 425 | `jigsawstack-automation` | Jigsawstack | 透過 Composio / Rube MCP 自動化 Jigsawstack 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/jigsawstack-automation/SKILL.md` |
| 426 | `jobnimbus-automation` | Jobnimbus | 透過 Composio / Rube MCP 自動化 Jobnimbus 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/jobnimbus-automation/SKILL.md` |
| 427 | `Jotform Automation` | Jotform | 透過 Composio / Rube MCP 自動化 Jotform 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/jotform-automation/SKILL.md` |
| 428 | `jumpcloud-automation` | Jumpcloud | 透過 Composio / Rube MCP 自動化 Jumpcloud 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/jumpcloud-automation/SKILL.md` |
| 429 | `junglescout-automation` | Junglescout | 透過 Composio / Rube MCP 自動化 Junglescout 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/junglescout-automation/SKILL.md` |
| 430 | `kadoa-automation` | Kadoa | 透過 Composio / Rube MCP 自動化 Kadoa 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/kadoa-automation/SKILL.md` |
| 431 | `kaggle-automation` | Kaggle | 透過 Composio / Rube MCP 自動化 Kaggle 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/kaggle-automation/SKILL.md` |
| 432 | `kaleido-automation` | Kaleido | 透過 Composio / Rube MCP 自動化 Kaleido 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/kaleido-automation/SKILL.md` |
| 433 | `keap-automation` | Keap | 透過 Composio / Rube MCP 自動化 Keap 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/keap-automation/SKILL.md` |
| 434 | `keen-io-automation` | Keen IO | 透過 Composio / Rube MCP 自動化 Keen IO 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/keen-io-automation/SKILL.md` |
| 435 | `kickbox-automation` | Kickbox | 透過 Composio / Rube MCP 自動化 Kickbox 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/kickbox-automation/SKILL.md` |
| 436 | `kit-automation` | Kit | 透過 Composio / Rube MCP 自動化 Kit 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/kit-automation/SKILL.md` |
| 437 | `klipfolio-automation` | Klipfolio | 透過 Composio / Rube MCP 自動化 Klipfolio 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/klipfolio-automation/SKILL.md` |
| 438 | `ko-fi-automation` | Ko Fi | 透過 Composio / Rube MCP 自動化 Ko Fi 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/ko-fi-automation/SKILL.md` |
| 439 | `Kommo Automation` | Kommo | 透過 Composio / Rube MCP 自動化 Kommo 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/kommo-automation/SKILL.md` |
| 440 | `kontent-ai-automation` | Kontent AI | 透過 Composio / Rube MCP 自動化 Kontent AI 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/kontent-ai-automation/SKILL.md` |
| 441 | `kraken-io-automation` | Kraken IO | 透過 Composio / Rube MCP 自動化 Kraken IO 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/kraken-io-automation/SKILL.md` |
| 442 | `l2s-automation` | L2s | 透過 Composio / Rube MCP 自動化 L2s 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/l2s-automation/SKILL.md` |
| 443 | `labs64-netlicensing-automation` | Labs64 Netlicensing | 透過 Composio / Rube MCP 自動化 Labs64 Netlicensing 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/labs64-netlicensing-automation/SKILL.md` |
| 444 | `landbot-automation` | Landbot | 透過 Composio / Rube MCP 自動化 Landbot 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/landbot-automation/SKILL.md` |
| 445 | `langbase-automation` | Langbase | 透過 Composio / Rube MCP 自動化 Langbase 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/langbase-automation/SKILL.md` |
| 446 | `lastpass-automation` | Lastpass | 透過 Composio / Rube MCP 自動化 Lastpass 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/lastpass-automation/SKILL.md` |
| 447 | `LaunchDarkly Automation` | LaunchDarkly | 透過 Composio / Rube MCP 自動化 LaunchDarkly 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/launch-darkly-automation/SKILL.md` |
| 448 | `launch_darkly-automation` | LaunchDarkly | 透過 Composio / Rube MCP 自動化 LaunchDarkly 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/launch_darkly-automation/SKILL.md` |
| 449 | `leadfeeder-automation` | Leadfeeder | 透過 Composio / Rube MCP 自動化 Leadfeeder 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/leadfeeder-automation/SKILL.md` |
| 450 | `leadoku-automation` | Leadoku | 透過 Composio / Rube MCP 自動化 Leadoku 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/leadoku-automation/SKILL.md` |
| 451 | `leiga-automation` | Leiga | 透過 Composio / Rube MCP 自動化 Leiga 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/leiga-automation/SKILL.md` |
| 452 | `Lemlist Automation` | Lemlist | 透過 Composio / Rube MCP 自動化 Lemlist 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/lemlist-automation/SKILL.md` |
| 453 | `Lemon Squeezy Automation` | Lemon Squeezy | 透過 Composio / Rube MCP 自動化 Lemon Squeezy 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/lemon-squeezy-automation/SKILL.md` |
| 454 | `lemon_squeezy-automation` | Lemon Squeezy | 透過 Composio / Rube MCP 自動化 Lemon Squeezy 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/lemon_squeezy-automation/SKILL.md` |
| 455 | `lessonspace-automation` | Lessonspace | 透過 Composio / Rube MCP 自動化 Lessonspace 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/lessonspace-automation/SKILL.md` |
| 456 | `Lever Automation` | Lever | 透過 Composio / Rube MCP 自動化 Lever 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/lever-automation/SKILL.md` |
| 457 | `lever-sandbox-automation` | Lever Sandbox | 透過 Composio / Rube MCP 自動化 Lever Sandbox 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/lever-sandbox-automation/SKILL.md` |
| 458 | `leverly-automation` | Leverly | 透過 Composio / Rube MCP 自動化 Leverly 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/leverly-automation/SKILL.md` |
| 459 | `lexoffice-automation` | Lexoffice | 透過 Composio / Rube MCP 自動化 Lexoffice 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/lexoffice-automation/SKILL.md` |
| 460 | `linguapop-automation` | Linguapop | 透過 Composio / Rube MCP 自動化 Linguapop 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/linguapop-automation/SKILL.md` |
| 461 | `linkhut-automation` | Linkhut | 透過 Composio / Rube MCP 自動化 Linkhut 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/linkhut-automation/SKILL.md` |
| 462 | `linkup-automation` | Linkup | 透過 Composio / Rube MCP 自動化 Linkup 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/linkup-automation/SKILL.md` |
| 463 | `listclean-automation` | Listclean | 透過 Composio / Rube MCP 自動化 Listclean 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/listclean-automation/SKILL.md` |
| 464 | `listennotes-automation` | Listennotes | 透過 Composio / Rube MCP 自動化 Listennotes 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/listennotes-automation/SKILL.md` |
| 465 | `livesession-automation` | Livesession | 透過 Composio / Rube MCP 自動化 Livesession 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/livesession-automation/SKILL.md` |
| 466 | `lmnt-automation` | Lmnt | 透過 Composio / Rube MCP 自動化 Lmnt 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/lmnt-automation/SKILL.md` |
| 467 | `lodgify-automation` | Lodgify | 透過 Composio / Rube MCP 自動化 Lodgify 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/lodgify-automation/SKILL.md` |
| 468 | `logo-dev-automation` | Logo Dev | 透過 Composio / Rube MCP 自動化 Logo Dev 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/logo-dev-automation/SKILL.md` |
| 469 | `loomio-automation` | Loomio | 透過 Composio / Rube MCP 自動化 Loomio 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/loomio-automation/SKILL.md` |
| 470 | `loyverse-automation` | Loyverse | 透過 Composio / Rube MCP 自動化 Loyverse 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/loyverse-automation/SKILL.md` |
| 471 | `magnetic-automation` | Magnetic | 透過 Composio / Rube MCP 自動化 Magnetic 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/magnetic-automation/SKILL.md` |
| 472 | `mailbluster-automation` | Mailbluster | 透過 Composio / Rube MCP 自動化 Mailbluster 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/mailbluster-automation/SKILL.md` |
| 473 | `mailboxlayer-automation` | Mailboxlayer | 透過 Composio / Rube MCP 自動化 Mailboxlayer 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/mailboxlayer-automation/SKILL.md` |
| 474 | `mailcheck-automation` | Mailcheck | 透過 Composio / Rube MCP 自動化 Mailcheck 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/mailcheck-automation/SKILL.md` |
| 475 | `mailcoach-automation` | Mailcoach | 透過 Composio / Rube MCP 自動化 Mailcoach 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/mailcoach-automation/SKILL.md` |
| 476 | `MailerLite Automation` | Mailerlite | 透過 Composio / Rube MCP 自動化 Mailerlite 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/mailerlite-automation/SKILL.md` |
| 477 | `mailersend-automation` | Mailersend | 透過 Composio / Rube MCP 自動化 Mailersend 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/mailersend-automation/SKILL.md` |
| 478 | `mails-so-automation` | Mails So | 透過 Composio / Rube MCP 自動化 Mails So 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/mails-so-automation/SKILL.md` |
| 479 | `mailsoftly-automation` | Mailsoftly | 透過 Composio / Rube MCP 自動化 Mailsoftly 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/mailsoftly-automation/SKILL.md` |
| 480 | `maintainx-automation` | Maintainx | 透過 Composio / Rube MCP 自動化 Maintainx 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/maintainx-automation/SKILL.md` |
| 481 | `many-chat-automation` | ManyChat | 透過 Composio / Rube MCP 自動化 ManyChat 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/many-chat-automation/SKILL.md` |
| 482 | `many_chat-automation` | ManyChat | 透過 Composio / Rube MCP 自動化 ManyChat 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/many_chat-automation/SKILL.md` |
| 483 | `mapbox-automation` | Mapbox | 透過 Composio / Rube MCP 自動化 Mapbox 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/mapbox-automation/SKILL.md` |
| 484 | `mapulus-automation` | Mapulus | 透過 Composio / Rube MCP 自動化 Mapulus 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/mapulus-automation/SKILL.md` |
| 485 | `mboum-automation` | Mboum | 透過 Composio / Rube MCP 自動化 Mboum 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/mboum-automation/SKILL.md` |
| 486 | `melo-automation` | Melo | 透過 Composio / Rube MCP 自動化 Melo 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/melo-automation/SKILL.md` |
| 487 | `mem-automation` | Mem | 透過 Composio / Rube MCP 自動化 Mem 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/mem-automation/SKILL.md` |
| 488 | `mem0-automation` | Mem0 | 透過 Composio / Rube MCP 自動化 Mem0 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/mem0-automation/SKILL.md` |
| 489 | `memberspot-automation` | Memberspot | 透過 Composio / Rube MCP 自動化 Memberspot 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/memberspot-automation/SKILL.md` |
| 490 | `memberstack-automation` | Memberstack | 透過 Composio / Rube MCP 自動化 Memberstack 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/memberstack-automation/SKILL.md` |
| 491 | `membervault-automation` | Membervault | 透過 Composio / Rube MCP 自動化 Membervault 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/membervault-automation/SKILL.md` |
| 492 | `metaads-automation` | Metaads | 透過 Composio / Rube MCP 自動化 Metaads 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/metaads-automation/SKILL.md` |
| 493 | `metaphor-automation` | Metaphor | 透過 Composio / Rube MCP 自動化 Metaphor 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/metaphor-automation/SKILL.md` |
| 494 | `mezmo-automation` | Mezmo | 透過 Composio / Rube MCP 自動化 Mezmo 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/mezmo-automation/SKILL.md` |
| 495 | `Microsoft Clarity Automation` | Microsoft Clarity | 透過 Composio / Rube MCP 自動化 Microsoft Clarity 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/microsoft-clarity-automation/SKILL.md` |
| 496 | `microsoft-tenant-automation` | Microsoft Tenant | 透過 Composio / Rube MCP 自動化 Microsoft Tenant 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/microsoft-tenant-automation/SKILL.md` |
| 497 | `microsoft_clarity-automation` | Microsoft Clarity | 透過 Composio / Rube MCP 自動化 Microsoft Clarity 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/microsoft_clarity-automation/SKILL.md` |
| 498 | `minerstat-automation` | Minerstat | 透過 Composio / Rube MCP 自動化 Minerstat 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/minerstat-automation/SKILL.md` |
| 499 | `missive-automation` | Missive | 透過 Composio / Rube MCP 自動化 Missive 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/missive-automation/SKILL.md` |
| 500 | `Mistral AI Automation` | Mistral AI | 透過 Composio / Rube MCP 自動化 Mistral AI 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/mistral-ai-automation/SKILL.md` |
| 501 | `mistral_ai-automation` | Mistral AI | 透過 Composio / Rube MCP 自動化 Mistral AI 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/mistral_ai-automation/SKILL.md` |
| 502 | `mocean-automation` | Mocean | 透過 Composio / Rube MCP 自動化 Mocean 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/mocean-automation/SKILL.md` |
| 503 | `moco-automation` | Moco | 透過 Composio / Rube MCP 自動化 Moco 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/moco-automation/SKILL.md` |
| 504 | `modelry-automation` | Modelry | 透過 Composio / Rube MCP 自動化 Modelry 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/modelry-automation/SKILL.md` |
| 505 | `moneybird-automation` | Moneybird | 透過 Composio / Rube MCP 自動化 Moneybird 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/moneybird-automation/SKILL.md` |
| 506 | `moonclerk-automation` | Moonclerk | 透過 Composio / Rube MCP 自動化 Moonclerk 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/moonclerk-automation/SKILL.md` |
| 507 | `moosend-automation` | Moosend | 透過 Composio / Rube MCP 自動化 Moosend 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/moosend-automation/SKILL.md` |
| 508 | `mopinion-automation` | Mopinion | 透過 Composio / Rube MCP 自動化 Mopinion 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/mopinion-automation/SKILL.md` |
| 509 | `more-trees-automation` | More Trees | 透過 Composio / Rube MCP 自動化 More Trees 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/more-trees-automation/SKILL.md` |
| 510 | `moxie-automation` | Moxie | 透過 Composio / Rube MCP 自動化 Moxie 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/moxie-automation/SKILL.md` |
| 511 | `moz-automation` | Moz | 透過 Composio / Rube MCP 自動化 Moz 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/moz-automation/SKILL.md` |
| 512 | `msg91-automation` | Msg91 | 透過 Composio / Rube MCP 自動化 Msg91 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/msg91-automation/SKILL.md` |
| 513 | `mural-automation` | Mural | 透過 Composio / Rube MCP 自動化 Mural 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/mural-automation/SKILL.md` |
| 514 | `mx-technologies-automation` | Mx Technologies | 透過 Composio / Rube MCP 自動化 Mx Technologies 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/mx-technologies-automation/SKILL.md` |
| 515 | `mx-toolbox-automation` | Mx Toolbox | 透過 Composio / Rube MCP 自動化 Mx Toolbox 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/mx-toolbox-automation/SKILL.md` |
| 516 | `nango-automation` | Nango | 透過 Composio / Rube MCP 自動化 Nango 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/nango-automation/SKILL.md` |
| 517 | `nano-nets-automation` | Nano Nets | 透過 Composio / Rube MCP 自動化 Nano Nets 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/nano-nets-automation/SKILL.md` |
| 518 | `nasa-automation` | NASA | 透過 Composio / Rube MCP 自動化 NASA 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/nasa-automation/SKILL.md` |
| 519 | `nasdaq-automation` | Nasdaq | 透過 Composio / Rube MCP 自動化 Nasdaq 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/nasdaq-automation/SKILL.md` |
| 520 | `ncscale-automation` | Ncscale | 透過 Composio / Rube MCP 自動化 Ncscale 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/ncscale-automation/SKILL.md` |
| 521 | `needle-automation` | Needle | 透過 Composio / Rube MCP 自動化 Needle 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/needle-automation/SKILL.md` |
| 522 | `Neon Automation` | Neon | 透過 Composio / Rube MCP 自動化 Neon 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/neon-automation/SKILL.md` |
| 523 | `NetSuite Automation` | Netsuite | 透過 Composio / Rube MCP 自動化 Netsuite 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/netsuite-automation/SKILL.md` |
| 524 | `neuronwriter-automation` | Neuronwriter | 透過 Composio / Rube MCP 自動化 Neuronwriter 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/neuronwriter-automation/SKILL.md` |
| 525 | `neutrino-automation` | Neutrino | 透過 Composio / Rube MCP 自動化 Neutrino 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/neutrino-automation/SKILL.md` |
| 526 | `neverbounce-automation` | Neverbounce | 透過 Composio / Rube MCP 自動化 Neverbounce 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/neverbounce-automation/SKILL.md` |
| 527 | `New Relic Automation` | New Relic | 透過 Composio / Rube MCP 自動化 New Relic 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/new-relic-automation/SKILL.md` |
| 528 | `new_relic-automation` | New Relic | 透過 Composio / Rube MCP 自動化 New Relic 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/new_relic-automation/SKILL.md` |
| 529 | `news-api-automation` | News API | 透過 Composio / Rube MCP 自動化 News API 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/news-api-automation/SKILL.md` |
| 530 | `nextdns-automation` | Nextdns | 透過 Composio / Rube MCP 自動化 Nextdns 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/nextdns-automation/SKILL.md` |
| 531 | `ngrok-automation` | Ngrok | 透過 Composio / Rube MCP 自動化 Ngrok 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/ngrok-automation/SKILL.md` |
| 532 | `ninox-automation` | Ninox | 透過 Composio / Rube MCP 自動化 Ninox 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/ninox-automation/SKILL.md` |
| 533 | `nocrm-io-automation` | Nocrm IO | 透過 Composio / Rube MCP 自動化 Nocrm IO 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/nocrm-io-automation/SKILL.md` |
| 534 | `npm-automation` | npm | 透過 Composio / Rube MCP 自動化 npm 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/npm-automation/SKILL.md` |
| 535 | `ocr-web-service-automation` | Ocr Web Service | 透過 Composio / Rube MCP 自動化 Ocr Web Service 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/ocr-web-service-automation/SKILL.md` |
| 536 | `ocrspace-automation` | Ocrspace | 透過 Composio / Rube MCP 自動化 Ocrspace 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/ocrspace-automation/SKILL.md` |
| 537 | `Omnisend Automation` | Omnisend | 透過 Composio / Rube MCP 自動化 Omnisend 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/omnisend-automation/SKILL.md` |
| 538 | `oncehub-automation` | Oncehub | 透過 Composio / Rube MCP 自動化 Oncehub 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/oncehub-automation/SKILL.md` |
| 539 | `onedesk-automation` | Onedesk | 透過 Composio / Rube MCP 自動化 Onedesk 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/onedesk-automation/SKILL.md` |
| 540 | `onepage-automation` | Onepage | 透過 Composio / Rube MCP 自動化 Onepage 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/onepage-automation/SKILL.md` |
| 541 | `onesignal-rest-api-automation` | OneSignal REST API | 透過 Composio / Rube MCP 自動化 OneSignal REST API 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/onesignal-rest-api-automation/SKILL.md` |
| 542 | `onesignal-user-auth-automation` | Onesignal User Auth | 透過 Composio / Rube MCP 自動化 Onesignal User Auth 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/onesignal-user-auth-automation/SKILL.md` |
| 543 | `onesignal_rest_api-automation` | OneSignal REST API | 透過 Composio / Rube MCP 自動化 OneSignal REST API 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/onesignal_rest_api-automation/SKILL.md` |
| 544 | `open-sea-automation` | Open Sea | 透過 Composio / Rube MCP 自動化 Open Sea 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/open-sea-automation/SKILL.md` |
| 545 | `OpenAI Automation` | OpenAI | 透過 Composio / Rube MCP 自動化 OpenAI 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/openai-automation/SKILL.md` |
| 546 | `opencage-automation` | Opencage | 透過 Composio / Rube MCP 自動化 Opencage 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/opencage-automation/SKILL.md` |
| 547 | `opengraph-io-automation` | Opengraph IO | 透過 Composio / Rube MCP 自動化 Opengraph IO 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/opengraph-io-automation/SKILL.md` |
| 548 | `openperplex-automation` | Openperplex | 透過 Composio / Rube MCP 自動化 Openperplex 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/openperplex-automation/SKILL.md` |
| 549 | `openrouter-automation` | Openrouter | 透過 Composio / Rube MCP 自動化 Openrouter 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/openrouter-automation/SKILL.md` |
| 550 | `openweather-api-automation` | Openweather API | 透過 Composio / Rube MCP 自動化 Openweather API 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/openweather-api-automation/SKILL.md` |
| 551 | `optimoroute-automation` | Optimoroute | 透過 Composio / Rube MCP 自動化 Optimoroute 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/optimoroute-automation/SKILL.md` |
| 552 | `owl-protocol-automation` | Owl Protocol | 透過 Composio / Rube MCP 自動化 Owl Protocol 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/owl-protocol-automation/SKILL.md` |
| 553 | `page-x-automation` | Page X | 透過 Composio / Rube MCP 自動化 Page X 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/page-x-automation/SKILL.md` |
| 554 | `PandaDoc Automation` | Pandadoc | 透過 Composio / Rube MCP 自動化 Pandadoc 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/pandadoc-automation/SKILL.md` |
| 555 | `paradym-automation` | Paradym | 透過 Composio / Rube MCP 自動化 Paradym 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/paradym-automation/SKILL.md` |
| 556 | `parallel-automation` | Parallel | 透過 Composio / Rube MCP 自動化 Parallel 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/parallel-automation/SKILL.md` |
| 557 | `parma-automation` | Parma | 透過 Composio / Rube MCP 自動化 Parma 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/parma-automation/SKILL.md` |
| 558 | `parsehub-automation` | Parsehub | 透過 Composio / Rube MCP 自動化 Parsehub 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/parsehub-automation/SKILL.md` |
| 559 | `parsera-automation` | Parsera | 透過 Composio / Rube MCP 自動化 Parsera 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/parsera-automation/SKILL.md` |
| 560 | `parseur-automation` | Parseur | 透過 Composio / Rube MCP 自動化 Parseur 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/parseur-automation/SKILL.md` |
| 561 | `passcreator-automation` | Passcreator | 透過 Composio / Rube MCP 自動化 Passcreator 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/passcreator-automation/SKILL.md` |
| 562 | `passslot-automation` | Passslot | 透過 Composio / Rube MCP 自動化 Passslot 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/passslot-automation/SKILL.md` |
| 563 | `payhip-automation` | Payhip | 透過 Composio / Rube MCP 自動化 Payhip 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/payhip-automation/SKILL.md` |
| 564 | `pdf-api-io-automation` | PDF API.io | 透過 Composio / Rube MCP 自動化 PDF API.io 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/pdf-api-io-automation/SKILL.md` |
| 565 | `pdf-co-automation` | PDF.co | 透過 Composio / Rube MCP 自動化 PDF.co 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/pdf-co-automation/SKILL.md` |
| 566 | `pdf4me-automation` | PDF4me | 透過 Composio / Rube MCP 自動化 PDF4me 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/pdf4me-automation/SKILL.md` |
| 567 | `pdfless-automation` | Pdfless | 透過 Composio / Rube MCP 自動化 Pdfless 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/pdfless-automation/SKILL.md` |
| 568 | `pdfmonkey-automation` | PDFMonkey | 透過 Composio / Rube MCP 自動化 PDFMonkey 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/pdfmonkey-automation/SKILL.md` |
| 569 | `peopledatalabs-automation` | Peopledatalabs | 透過 Composio / Rube MCP 自動化 Peopledatalabs 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/peopledatalabs-automation/SKILL.md` |
| 570 | `perigon-automation` | Perigon | 透過 Composio / Rube MCP 自動化 Perigon 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/perigon-automation/SKILL.md` |
| 571 | `perplexityai-automation` | Perplexity AI | 透過 Composio / Rube MCP 自動化 Perplexity AI 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/perplexityai-automation/SKILL.md` |
| 572 | `persistiq-automation` | Persistiq | 透過 Composio / Rube MCP 自動化 Persistiq 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/persistiq-automation/SKILL.md` |
| 573 | `pexels-automation` | Pexels | 透過 Composio / Rube MCP 自動化 Pexels 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/pexels-automation/SKILL.md` |
| 574 | `PhantomBuster Automation` | Phantombuster | 透過 Composio / Rube MCP 自動化 Phantombuster 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/phantombuster-automation/SKILL.md` |
| 575 | `piggy-automation` | Piggy | 透過 Composio / Rube MCP 自動化 Piggy 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/piggy-automation/SKILL.md` |
| 576 | `piloterr-automation` | Piloterr | 透過 Composio / Rube MCP 自動化 Piloterr 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/piloterr-automation/SKILL.md` |
| 577 | `pilvio-automation` | Pilvio | 透過 Composio / Rube MCP 自動化 Pilvio 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/pilvio-automation/SKILL.md` |
| 578 | `pingdom-automation` | Pingdom | 透過 Composio / Rube MCP 自動化 Pingdom 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/pingdom-automation/SKILL.md` |
| 579 | `pipeline-crm-automation` | Pipeline CRM | 透過 Composio / Rube MCP 自動化 Pipeline CRM 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/pipeline-crm-automation/SKILL.md` |
| 580 | `placekey-automation` | Placekey | 透過 Composio / Rube MCP 自動化 Placekey 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/placekey-automation/SKILL.md` |
| 581 | `placid-automation` | Placid | 透過 Composio / Rube MCP 自動化 Placid 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/placid-automation/SKILL.md` |
| 582 | `plain-automation` | Plain | 透過 Composio / Rube MCP 自動化 Plain 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/plain-automation/SKILL.md` |
| 583 | `plasmic-automation` | Plasmic | 透過 Composio / Rube MCP 自動化 Plasmic 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/plasmic-automation/SKILL.md` |
| 584 | `platerecognizer-automation` | Platerecognizer | 透過 Composio / Rube MCP 自動化 Platerecognizer 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/platerecognizer-automation/SKILL.md` |
| 585 | `plisio-automation` | Plisio | 透過 Composio / Rube MCP 自動化 Plisio 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/plisio-automation/SKILL.md` |
| 586 | `polygon-automation` | Polygon | 透過 Composio / Rube MCP 自動化 Polygon 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/polygon-automation/SKILL.md` |
| 587 | `polygon-io-automation` | Polygon IO | 透過 Composio / Rube MCP 自動化 Polygon IO 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/polygon-io-automation/SKILL.md` |
| 588 | `poptin-automation` | Poptin | 透過 Composio / Rube MCP 自動化 Poptin 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/poptin-automation/SKILL.md` |
| 589 | `postgrid-automation` | Postgrid | 透過 Composio / Rube MCP 自動化 Postgrid 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/postgrid-automation/SKILL.md` |
| 590 | `postgrid-verify-automation` | Postgrid Verify | 透過 Composio / Rube MCP 自動化 Postgrid Verify 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/postgrid-verify-automation/SKILL.md` |
| 591 | `precoro-automation` | Precoro | 透過 Composio / Rube MCP 自動化 Precoro 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/precoro-automation/SKILL.md` |
| 592 | `prerender-automation` | Prerender | 透過 Composio / Rube MCP 自動化 Prerender 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/prerender-automation/SKILL.md` |
| 593 | `printautopilot-automation` | Printautopilot | 透過 Composio / Rube MCP 自動化 Printautopilot 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/printautopilot-automation/SKILL.md` |
| 594 | `prisma-automation` | Prisma | 透過 Composio / Rube MCP 自動化 Prisma 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/prisma-automation/SKILL.md` |
| 595 | `Prismic Automation` | Prismic | 透過 Composio / Rube MCP 自動化 Prismic 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/prismic-automation/SKILL.md` |
| 596 | `process-street-automation` | Process Street | 透過 Composio / Rube MCP 自動化 Process Street 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/process-street-automation/SKILL.md` |
| 597 | `procfu-automation` | Procfu | 透過 Composio / Rube MCP 自動化 Procfu 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/procfu-automation/SKILL.md` |
| 598 | `Productboard Automation` | Productboard | 透過 Composio / Rube MCP 自動化 Productboard 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/productboard-automation/SKILL.md` |
| 599 | `productlane-automation` | Productlane | 透過 Composio / Rube MCP 自動化 Productlane 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/productlane-automation/SKILL.md` |
| 600 | `project-bubble-automation` | Project Bubble | 透過 Composio / Rube MCP 自動化 Project Bubble 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/project-bubble-automation/SKILL.md` |
| 601 | `proofly-automation` | Proofly | 透過 Composio / Rube MCP 自動化 Proofly 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/proofly-automation/SKILL.md` |
| 602 | `proxiedmail-automation` | Proxiedmail | 透過 Composio / Rube MCP 自動化 Proxiedmail 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/proxiedmail-automation/SKILL.md` |
| 603 | `pushbullet-automation` | Pushbullet | 透過 Composio / Rube MCP 自動化 Pushbullet 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/pushbullet-automation/SKILL.md` |
| 604 | `pushover-automation` | Pushover | 透過 Composio / Rube MCP 自動化 Pushover 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/pushover-automation/SKILL.md` |
| 605 | `quaderno-automation` | Quaderno | 透過 Composio / Rube MCP 自動化 Quaderno 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/quaderno-automation/SKILL.md` |
| 606 | `qualaroo-automation` | Qualaroo | 透過 Composio / Rube MCP 自動化 Qualaroo 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/qualaroo-automation/SKILL.md` |
| 607 | `QuickBooks Automation` | Quickbooks | 透過 Composio / Rube MCP 自動化 Quickbooks 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/quickbooks-automation/SKILL.md` |
| 608 | `radar-automation` | Radar | 透過 Composio / Rube MCP 自動化 Radar 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/radar-automation/SKILL.md` |
| 609 | `rafflys-automation` | Rafflys | 透過 Composio / Rube MCP 自動化 Rafflys 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/rafflys-automation/SKILL.md` |
| 610 | `ragic-automation` | Ragic | 透過 Composio / Rube MCP 自動化 Ragic 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/ragic-automation/SKILL.md` |
| 611 | `raisely-automation` | Raisely | 透過 Composio / Rube MCP 自動化 Raisely 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/raisely-automation/SKILL.md` |
| 612 | `Ramp Automation` | Ramp | 透過 Composio / Rube MCP 自動化 Ramp 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/ramp-automation/SKILL.md` |
| 613 | `ravenseotools-automation` | Ravenseotools | 透過 Composio / Rube MCP 自動化 Ravenseotools 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/ravenseotools-automation/SKILL.md` |
| 614 | `re-amaze-automation` | Re Amaze | 透過 Composio / Rube MCP 自動化 Re Amaze 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/re-amaze-automation/SKILL.md` |
| 615 | `realphonevalidation-automation` | Realphonevalidation | 透過 Composio / Rube MCP 自動化 Realphonevalidation 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/realphonevalidation-automation/SKILL.md` |
| 616 | `recallai-automation` | Recallai | 透過 Composio / Rube MCP 自動化 Recallai 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/recallai-automation/SKILL.md` |
| 617 | `recruitee-automation` | Recruitee | 透過 Composio / Rube MCP 自動化 Recruitee 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/recruitee-automation/SKILL.md` |
| 618 | `refiner-automation` | Refiner | 透過 Composio / Rube MCP 自動化 Refiner 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/refiner-automation/SKILL.md` |
| 619 | `remarkety-automation` | Remarkety | 透過 Composio / Rube MCP 自動化 Remarkety 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/remarkety-automation/SKILL.md` |
| 620 | `remote-retrieval-automation` | Remote Retrieval | 透過 Composio / Rube MCP 自動化 Remote Retrieval 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/remote-retrieval-automation/SKILL.md` |
| 621 | `remove-bg-automation` | Remove Bg | 透過 Composio / Rube MCP 自動化 Remove Bg 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/remove-bg-automation/SKILL.md` |
| 622 | `renderform-automation` | Renderform | 透過 Composio / Rube MCP 自動化 Renderform 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/renderform-automation/SKILL.md` |
| 623 | `repairshopr-automation` | Repairshopr | 透過 Composio / Rube MCP 自動化 Repairshopr 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/repairshopr-automation/SKILL.md` |
| 624 | `Replicate Automation` | Replicate | 透過 Composio / Rube MCP 自動化 Replicate 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/replicate-automation/SKILL.md` |
| 625 | `reply-automation` | Reply | 透過 Composio / Rube MCP 自動化 Reply 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/reply-automation/SKILL.md` |
| 626 | `reply-io-automation` | Reply IO | 透過 Composio / Rube MCP 自動化 Reply IO 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/reply-io-automation/SKILL.md` |
| 627 | `resend-automation` | Resend | 透過 Composio / Rube MCP 自動化 Resend 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/resend-automation/SKILL.md` |
| 628 | `respond-io-automation` | Respond IO | 透過 Composio / Rube MCP 自動化 Respond IO 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/respond-io-automation/SKILL.md` |
| 629 | `retailed-automation` | Retailed | 透過 Composio / Rube MCP 自動化 Retailed 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/retailed-automation/SKILL.md` |
| 630 | `retellai-automation` | Retellai | 透過 Composio / Rube MCP 自動化 Retellai 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/retellai-automation/SKILL.md` |
| 631 | `retently-automation` | Retently | 透過 Composio / Rube MCP 自動化 Retently 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/retently-automation/SKILL.md` |
| 632 | `rev-ai-automation` | Rev AI | 透過 Composio / Rube MCP 自動化 Rev AI 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/rev-ai-automation/SKILL.md` |
| 633 | `revolt-automation` | Revolt | 透過 Composio / Rube MCP 自動化 Revolt 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/revolt-automation/SKILL.md` |
| 634 | `RingCentral Automation` | RingCentral | 透過 Composio / Rube MCP 自動化 RingCentral 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/ring-central-automation/SKILL.md` |
| 635 | `ring_central-automation` | RingCentral | 透過 Composio / Rube MCP 自動化 RingCentral 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/ring_central-automation/SKILL.md` |
| 636 | `rippling-automation` | Rippling | 透過 Composio / Rube MCP 自動化 Rippling 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/rippling-automation/SKILL.md` |
| 637 | `ritekit-automation` | Ritekit | 透過 Composio / Rube MCP 自動化 Ritekit 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/ritekit-automation/SKILL.md` |
| 638 | `rkvst-automation` | Rkvst | 透過 Composio / Rube MCP 自動化 Rkvst 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/rkvst-automation/SKILL.md` |
| 639 | `rocketlane-automation` | Rocketlane | 透過 Composio / Rube MCP 自動化 Rocketlane 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/rocketlane-automation/SKILL.md` |
| 640 | `rootly-automation` | Rootly | 透過 Composio / Rube MCP 自動化 Rootly 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/rootly-automation/SKILL.md` |
| 641 | `rosette-text-analytics-automation` | Rosette Text Analytics | 透過 Composio / Rube MCP 自動化 Rosette Text Analytics 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/rosette-text-analytics-automation/SKILL.md` |
| 642 | `route4me-automation` | Route4me | 透過 Composio / Rube MCP 自動化 Route4me 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/route4me-automation/SKILL.md` |
| 643 | `safetyculture-automation` | Safetyculture | 透過 Composio / Rube MCP 自動化 Safetyculture 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/safetyculture-automation/SKILL.md` |
| 644 | `sage-automation` | Sage | 透過 Composio / Rube MCP 自動化 Sage 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/sage-automation/SKILL.md` |
| 645 | `salesforce-marketing-cloud-automation` | Salesforce Marketing Cloud | 透過 Composio / Rube MCP 自動化 Salesforce Marketing Cloud 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/salesforce-marketing-cloud-automation/SKILL.md` |
| 646 | `salesforce-service-cloud-automation` | Salesforce Service Cloud | 透過 Composio / Rube MCP 自動化 Salesforce Service Cloud 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/salesforce-service-cloud-automation/SKILL.md` |
| 647 | `salesmate-automation` | Salesmate | 透過 Composio / Rube MCP 自動化 Salesmate 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/salesmate-automation/SKILL.md` |
| 648 | `sap-successfactors-automation` | Sap Successfactors | 透過 Composio / Rube MCP 自動化 Sap Successfactors 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/sap-successfactors-automation/SKILL.md` |
| 649 | `satismeter-automation` | Satismeter | 透過 Composio / Rube MCP 自動化 Satismeter 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/satismeter-automation/SKILL.md` |
| 650 | `scrape-do-automation` | Scrape Do | 透過 Composio / Rube MCP 自動化 Scrape Do 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/scrape-do-automation/SKILL.md` |
| 651 | `scrapegraph-ai-automation` | Scrapegraph AI | 透過 Composio / Rube MCP 自動化 Scrapegraph AI 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/scrapegraph-ai-automation/SKILL.md` |
| 652 | `scrapfly-automation` | Scrapfly | 透過 Composio / Rube MCP 自動化 Scrapfly 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/scrapfly-automation/SKILL.md` |
| 653 | `scrapingant-automation` | Scrapingant | 透過 Composio / Rube MCP 自動化 Scrapingant 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/scrapingant-automation/SKILL.md` |
| 654 | `scrapingbee-automation` | Scrapingbee | 透過 Composio / Rube MCP 自動化 Scrapingbee 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/scrapingbee-automation/SKILL.md` |
| 655 | `screenshot-fyi-automation` | Screenshot Fyi | 透過 Composio / Rube MCP 自動化 Screenshot Fyi 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/screenshot-fyi-automation/SKILL.md` |
| 656 | `screenshotone-automation` | Screenshotone | 透過 Composio / Rube MCP 自動化 Screenshotone 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/screenshotone-automation/SKILL.md` |
| 657 | `seat-geek-automation` | Seat Geek | 透過 Composio / Rube MCP 自動化 Seat Geek 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/seat-geek-automation/SKILL.md` |
| 658 | `securitytrails-automation` | Securitytrails | 透過 Composio / Rube MCP 自動化 Securitytrails 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/securitytrails-automation/SKILL.md` |
| 659 | `segmetrics-automation` | Segmetrics | 透過 Composio / Rube MCP 自動化 Segmetrics 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/segmetrics-automation/SKILL.md` |
| 660 | `seismic-automation` | Seismic | 透過 Composio / Rube MCP 自動化 Seismic 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/seismic-automation/SKILL.md` |
| 661 | `semanticscholar-automation` | Semanticscholar | 透過 Composio / Rube MCP 自動化 Semanticscholar 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/semanticscholar-automation/SKILL.md` |
| 662 | `SEMrush Automation` | Semrush | 透過 Composio / Rube MCP 自動化 Semrush 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/semrush-automation/SKILL.md` |
| 663 | `sendbird-ai-chabot-automation` | Sendbird AI Chabot | 透過 Composio / Rube MCP 自動化 Sendbird AI Chabot 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/sendbird-ai-chabot-automation/SKILL.md` |
| 664 | `sendbird-automation` | Sendbird | 透過 Composio / Rube MCP 自動化 Sendbird 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/sendbird-automation/SKILL.md` |
| 665 | `sendfox-automation` | Sendfox | 透過 Composio / Rube MCP 自動化 Sendfox 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/sendfox-automation/SKILL.md` |
| 666 | `sendlane-automation` | Sendlane | 透過 Composio / Rube MCP 自動化 Sendlane 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/sendlane-automation/SKILL.md` |
| 667 | `sendloop-automation` | Sendloop | 透過 Composio / Rube MCP 自動化 Sendloop 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/sendloop-automation/SKILL.md` |
| 668 | `sendspark-automation` | Sendspark | 透過 Composio / Rube MCP 自動化 Sendspark 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/sendspark-automation/SKILL.md` |
| 669 | `sensibo-automation` | Sensibo | 透過 Composio / Rube MCP 自動化 Sensibo 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/sensibo-automation/SKILL.md` |
| 670 | `seqera-automation` | Seqera | 透過 Composio / Rube MCP 自動化 Seqera 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/seqera-automation/SKILL.md` |
| 671 | `serpapi-automation` | SerpApi | 透過 Composio / Rube MCP 自動化 SerpApi 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/serpapi-automation/SKILL.md` |
| 672 | `serpdog-automation` | Serpdog | 透過 Composio / Rube MCP 自動化 Serpdog 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/serpdog-automation/SKILL.md` |
| 673 | `serply-automation` | Serply | 透過 Composio / Rube MCP 自動化 Serply 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/serply-automation/SKILL.md` |
| 674 | `servicem8-automation` | Servicem8 | 透過 Composio / Rube MCP 自動化 Servicem8 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/servicem8-automation/SKILL.md` |
| 675 | `sevdesk-automation` | Sevdesk | 透過 Composio / Rube MCP 自動化 Sevdesk 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/sevdesk-automation/SKILL.md` |
| 676 | `SharePoint Automation` | SharePoint | 透過 Composio / Rube MCP 自動化 SharePoint 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/share-point-automation/SKILL.md` |
| 677 | `share_point-automation` | SharePoint | 透過 Composio / Rube MCP 自動化 SharePoint 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/share_point-automation/SKILL.md` |
| 678 | `shipengine-automation` | Shipengine | 透過 Composio / Rube MCP 自動化 Shipengine 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/shipengine-automation/SKILL.md` |
| 679 | `short-io-automation` | Short IO | 透過 Composio / Rube MCP 自動化 Short IO 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/short-io-automation/SKILL.md` |
| 680 | `short-menu-automation` | Short Menu | 透過 Composio / Rube MCP 自動化 Short Menu 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/short-menu-automation/SKILL.md` |
| 681 | `Shortcut Automation` | Shortcut | 透過 Composio / Rube MCP 自動化 Shortcut 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/shortcut-automation/SKILL.md` |
| 682 | `shorten-rest-automation` | Shorten Rest | 透過 Composio / Rube MCP 自動化 Shorten Rest 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/shorten-rest-automation/SKILL.md` |
| 683 | `shortpixel-automation` | Shortpixel | 透過 Composio / Rube MCP 自動化 Shortpixel 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/shortpixel-automation/SKILL.md` |
| 684 | `shotstack-automation` | Shotstack | 透過 Composio / Rube MCP 自動化 Shotstack 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/shotstack-automation/SKILL.md` |
| 685 | `sidetracker-automation` | Sidetracker | 透過 Composio / Rube MCP 自動化 Sidetracker 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/sidetracker-automation/SKILL.md` |
| 686 | `signaturely-automation` | Signaturely | 透過 Composio / Rube MCP 自動化 Signaturely 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/signaturely-automation/SKILL.md` |
| 687 | `signpath-automation` | Signpath | 透過 Composio / Rube MCP 自動化 Signpath 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/signpath-automation/SKILL.md` |
| 688 | `signwell-automation` | Signwell | 透過 Composio / Rube MCP 自動化 Signwell 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/signwell-automation/SKILL.md` |
| 689 | `similarweb-digitalrank-api-automation` | Similarweb Digitalrank API | 透過 Composio / Rube MCP 自動化 Similarweb Digitalrank API 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/similarweb-digitalrank-api-automation/SKILL.md` |
| 690 | `similarweb_digitalrank_api-automation` | Similarweb Digitalrank API | 透過 Composio / Rube MCP 自動化 Similarweb Digitalrank API 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/similarweb_digitalrank_api-automation/SKILL.md` |
| 691 | `simla-com-automation` | Simla Com | 透過 Composio / Rube MCP 自動化 Simla Com 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/simla-com-automation/SKILL.md` |
| 692 | `simple-analytics-automation` | Simple Analytics | 透過 Composio / Rube MCP 自動化 Simple Analytics 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/simple-analytics-automation/SKILL.md` |
| 693 | `simplesat-automation` | Simplesat | 透過 Composio / Rube MCP 自動化 Simplesat 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/simplesat-automation/SKILL.md` |
| 694 | `sitespeakai-automation` | Sitespeakai | 透過 Composio / Rube MCP 自動化 Sitespeakai 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/sitespeakai-automation/SKILL.md` |
| 695 | `skyfire-automation` | Skyfire | 透過 Composio / Rube MCP 自動化 Skyfire 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/skyfire-automation/SKILL.md` |
| 696 | `slackbot-automation` | Slackbot | 透過 Composio / Rube MCP 自動化 Slackbot 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/slackbot-automation/SKILL.md` |
| 697 | `smartproxy-automation` | Smartproxy | 透過 Composio / Rube MCP 自動化 Smartproxy 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/smartproxy-automation/SKILL.md` |
| 698 | `smartrecruiters-automation` | Smartrecruiters | 透過 Composio / Rube MCP 自動化 Smartrecruiters 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/smartrecruiters-automation/SKILL.md` |
| 699 | `sms-alert-automation` | SMS Alert | 透過 Composio / Rube MCP 自動化 SMS Alert 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/sms-alert-automation/SKILL.md` |
| 700 | `smtp2go-automation` | Smtp2go | 透過 Composio / Rube MCP 自動化 Smtp2go 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/smtp2go-automation/SKILL.md` |
| 701 | `smugmug-automation` | Smugmug | 透過 Composio / Rube MCP 自動化 Smugmug 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/smugmug-automation/SKILL.md` |
| 702 | `Snowflake Automation` | Snowflake | 透過 Composio / Rube MCP 自動化 Snowflake 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/snowflake-automation/SKILL.md` |
| 703 | `sourcegraph-automation` | Sourcegraph | 透過 Composio / Rube MCP 自動化 Sourcegraph 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/sourcegraph-automation/SKILL.md` |
| 704 | `splitwise-automation` | Splitwise | 透過 Composio / Rube MCP 自動化 Splitwise 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/splitwise-automation/SKILL.md` |
| 705 | `spoki-automation` | Spoki | 透過 Composio / Rube MCP 自動化 Spoki 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/spoki-automation/SKILL.md` |
| 706 | `spondyr-automation` | Spondyr | 透過 Composio / Rube MCP 自動化 Spondyr 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/spondyr-automation/SKILL.md` |
| 707 | `Spotify Automation` | Spotify | 透過 Composio / Rube MCP 自動化 Spotify 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/spotify-automation/SKILL.md` |
| 708 | `spotlightr-automation` | Spotlightr | 透過 Composio / Rube MCP 自動化 Spotlightr 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/spotlightr-automation/SKILL.md` |
| 709 | `sslmate-cert-spotter-api-automation` | Sslmate Cert Spotter API | 透過 Composio / Rube MCP 自動化 Sslmate Cert Spotter API 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/sslmate-cert-spotter-api-automation/SKILL.md` |
| 710 | `stack-exchange-automation` | Stack Exchange | 透過 Composio / Rube MCP 自動化 Stack Exchange 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/stack-exchange-automation/SKILL.md` |
| 711 | `stannp-automation` | Stannp | 透過 Composio / Rube MCP 自動化 Stannp 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/stannp-automation/SKILL.md` |
| 712 | `starton-automation` | Starton | 透過 Composio / Rube MCP 自動化 Starton 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/starton-automation/SKILL.md` |
| 713 | `statuscake-automation` | Statuscake | 透過 Composio / Rube MCP 自動化 Statuscake 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/statuscake-automation/SKILL.md` |
| 714 | `storeganise-automation` | Storeganise | 透過 Composio / Rube MCP 自動化 Storeganise 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/storeganise-automation/SKILL.md` |
| 715 | `storerocket-automation` | Storerocket | 透過 Composio / Rube MCP 自動化 Storerocket 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/storerocket-automation/SKILL.md` |
| 716 | `stormglass-io-automation` | Stormglass IO | 透過 Composio / Rube MCP 自動化 Stormglass IO 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/stormglass-io-automation/SKILL.md` |
| 717 | `strava-automation` | Strava | 透過 Composio / Rube MCP 自動化 Strava 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/strava-automation/SKILL.md` |
| 718 | `streamtime-automation` | Streamtime | 透過 Composio / Rube MCP 自動化 Streamtime 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/streamtime-automation/SKILL.md` |
| 719 | `supadata-automation` | Supadata | 透過 Composio / Rube MCP 自動化 Supadata 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/supadata-automation/SKILL.md` |
| 720 | `superchat-automation` | Superchat | 透過 Composio / Rube MCP 自動化 Superchat 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/superchat-automation/SKILL.md` |
| 721 | `supportbee-automation` | Supportbee | 透過 Composio / Rube MCP 自動化 Supportbee 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/supportbee-automation/SKILL.md` |
| 722 | `supportivekoala-automation` | Supportivekoala | 透過 Composio / Rube MCP 自動化 Supportivekoala 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/supportivekoala-automation/SKILL.md` |
| 723 | `SurveyMonkey Automation` | Survey Monkey | 透過 Composio / Rube MCP 自動化 Survey Monkey 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/survey-monkey-automation/SKILL.md` |
| 724 | `survey_monkey-automation` | Survey Monkey | 透過 Composio / Rube MCP 自動化 Survey Monkey 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/survey_monkey-automation/SKILL.md` |
| 725 | `svix-automation` | Svix | 透過 Composio / Rube MCP 自動化 Svix 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/svix-automation/SKILL.md` |
| 726 | `sympla-automation` | Sympla | 透過 Composio / Rube MCP 自動化 Sympla 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/sympla-automation/SKILL.md` |
| 727 | `synthflow-ai-automation` | Synthflow AI | 透過 Composio / Rube MCP 自動化 Synthflow AI 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/synthflow-ai-automation/SKILL.md` |
| 728 | `taggun-automation` | Taggun | 透過 Composio / Rube MCP 自動化 Taggun 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/taggun-automation/SKILL.md` |
| 729 | `talenthr-automation` | Talenthr | 透過 Composio / Rube MCP 自動化 Talenthr 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/talenthr-automation/SKILL.md` |
| 730 | `tally-automation` | Tally | 透過 Composio / Rube MCP 自動化 Tally 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/tally-automation/SKILL.md` |
| 731 | `tapfiliate-automation` | Tapfiliate | 透過 Composio / Rube MCP 自動化 Tapfiliate 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/tapfiliate-automation/SKILL.md` |
| 732 | `tapform-automation` | Tapform | 透過 Composio / Rube MCP 自動化 Tapform 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/tapform-automation/SKILL.md` |
| 733 | `tavily-automation` | Tavily | 透過 Composio / Rube MCP 自動化 Tavily 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/tavily-automation/SKILL.md` |
| 734 | `taxjar-automation` | Taxjar | 透過 Composio / Rube MCP 自動化 Taxjar 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/taxjar-automation/SKILL.md` |
| 735 | `teamcamp-automation` | Teamcamp | 透過 Composio / Rube MCP 自動化 Teamcamp 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/teamcamp-automation/SKILL.md` |
| 736 | `telnyx-automation` | Telnyx | 透過 Composio / Rube MCP 自動化 Telnyx 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/telnyx-automation/SKILL.md` |
| 737 | `teltel-automation` | Teltel | 透過 Composio / Rube MCP 自動化 Teltel 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/teltel-automation/SKILL.md` |
| 738 | `templated-automation` | Templated | 透過 Composio / Rube MCP 自動化 Templated 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/templated-automation/SKILL.md` |
| 739 | `test-app-automation` | Test App | 透過 Composio / Rube MCP 自動化 Test App 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/test-app-automation/SKILL.md` |
| 740 | `text-to-pdf-automation` | Text To PDF | 透過 Composio / Rube MCP 自動化 Text To PDF 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/text-to-pdf-automation/SKILL.md` |
| 741 | `textcortex-automation` | Textcortex | 透過 Composio / Rube MCP 自動化 Textcortex 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/textcortex-automation/SKILL.md` |
| 742 | `textit-automation` | Textit | 透過 Composio / Rube MCP 自動化 Textit 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/textit-automation/SKILL.md` |
| 743 | `textrazor-automation` | Textrazor | 透過 Composio / Rube MCP 自動化 Textrazor 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/textrazor-automation/SKILL.md` |
| 744 | `thanks-io-automation` | Thanks IO | 透過 Composio / Rube MCP 自動化 Thanks IO 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/thanks-io-automation/SKILL.md` |
| 745 | `the-odds-api-automation` | The Odds API | 透過 Composio / Rube MCP 自動化 The Odds API 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/the-odds-api-automation/SKILL.md` |
| 746 | `ticketmaster-automation` | Ticketmaster | 透過 Composio / Rube MCP 自動化 Ticketmaster 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/ticketmaster-automation/SKILL.md` |
| 747 | `ticktick-automation` | Ticktick | 透過 Composio / Rube MCP 自動化 Ticktick 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/ticktick-automation/SKILL.md` |
| 748 | `timecamp-automation` | Timecamp | 透過 Composio / Rube MCP 自動化 Timecamp 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/timecamp-automation/SKILL.md` |
| 749 | `timekit-automation` | Timekit | 透過 Composio / Rube MCP 自動化 Timekit 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/timekit-automation/SKILL.md` |
| 750 | `timelinesai-automation` | Timelinesai | 透過 Composio / Rube MCP 自動化 Timelinesai 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/timelinesai-automation/SKILL.md` |
| 751 | `timelink-automation` | Timelink | 透過 Composio / Rube MCP 自動化 Timelink 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/timelink-automation/SKILL.md` |
| 752 | `timely-automation` | Timely | 透過 Composio / Rube MCP 自動化 Timely 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/timely-automation/SKILL.md` |
| 753 | `tinyurl-automation` | Tinyurl | 透過 Composio / Rube MCP 自動化 Tinyurl 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/tinyurl-automation/SKILL.md` |
| 754 | `tisane-automation` | Tisane | 透過 Composio / Rube MCP 自動化 Tisane 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/tisane-automation/SKILL.md` |
| 755 | `Toggl Automation` | Toggl | 透過 Composio / Rube MCP 自動化 Toggl 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/toggl-automation/SKILL.md` |
| 756 | `token-metrics-automation` | Token Metrics | 透過 Composio / Rube MCP 自動化 Token Metrics 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/token-metrics-automation/SKILL.md` |
| 757 | `tomba-automation` | Tomba | 透過 Composio / Rube MCP 自動化 Tomba 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/tomba-automation/SKILL.md` |
| 758 | `tomtom-automation` | Tomtom | 透過 Composio / Rube MCP 自動化 Tomtom 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/tomtom-automation/SKILL.md` |
| 759 | `toneden-automation` | Toneden | 透過 Composio / Rube MCP 自動化 Toneden 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/toneden-automation/SKILL.md` |
| 760 | `tpscheck-automation` | Tpscheck | 透過 Composio / Rube MCP 自動化 Tpscheck 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/tpscheck-automation/SKILL.md` |
| 761 | `triggercmd-automation` | Triggercmd | 透過 Composio / Rube MCP 自動化 Triggercmd 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/triggercmd-automation/SKILL.md` |
| 762 | `tripadvisor-content-api-automation` | Tripadvisor Content API | 透過 Composio / Rube MCP 自動化 Tripadvisor Content API 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/tripadvisor-content-api-automation/SKILL.md` |
| 763 | `turbot-pipes-automation` | Turbot Pipes | 透過 Composio / Rube MCP 自動化 Turbot Pipes 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/turbot-pipes-automation/SKILL.md` |
| 764 | `turso-automation` | Turso | 透過 Composio / Rube MCP 自動化 Turso 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/turso-automation/SKILL.md` |
| 765 | `twelve-data-automation` | Twelve Data | 透過 Composio / Rube MCP 自動化 Twelve Data 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/twelve-data-automation/SKILL.md` |
| 766 | `twitch-automation` | Twitch | 透過 Composio / Rube MCP 自動化 Twitch 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/twitch-automation/SKILL.md` |
| 767 | `twocaptcha-automation` | Twocaptcha | 透過 Composio / Rube MCP 自動化 Twocaptcha 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/twocaptcha-automation/SKILL.md` |
| 768 | `typefully-automation` | Typefully | 透過 Composio / Rube MCP 自動化 Typefully 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/typefully-automation/SKILL.md` |
| 769 | `typless-automation` | Typless | 透過 Composio / Rube MCP 自動化 Typless 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/typless-automation/SKILL.md` |
| 770 | `u301-automation` | U301 | 透過 Composio / Rube MCP 自動化 U301 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/u301-automation/SKILL.md` |
| 771 | `unione-automation` | Unione | 透過 Composio / Rube MCP 自動化 Unione 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/unione-automation/SKILL.md` |
| 772 | `updown-io-automation` | Updown IO | 透過 Composio / Rube MCP 自動化 Updown IO 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/updown-io-automation/SKILL.md` |
| 773 | `Uploadcare Automation` | Uploadcare | 透過 Composio / Rube MCP 自動化 Uploadcare 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/uploadcare-automation/SKILL.md` |
| 774 | `uptimerobot-automation` | Uptimerobot | 透過 Composio / Rube MCP 自動化 Uptimerobot 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/uptimerobot-automation/SKILL.md` |
| 775 | `userlist-automation` | Userlist | 透過 Composio / Rube MCP 自動化 Userlist 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/userlist-automation/SKILL.md` |
| 776 | `v0-automation` | V0 | 透過 Composio / Rube MCP 自動化 V0 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/v0-automation/SKILL.md` |
| 777 | `venly-automation` | Venly | 透過 Composio / Rube MCP 自動化 Venly 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/venly-automation/SKILL.md` |
| 778 | `veo-automation` | Veo | 透過 Composio / Rube MCP 自動化 Veo 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/veo-automation/SKILL.md` |
| 779 | `verifiedemail-automation` | Verifiedemail | 透過 Composio / Rube MCP 自動化 Verifiedemail 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/verifiedemail-automation/SKILL.md` |
| 780 | `veriphone-automation` | Veriphone | 透過 Composio / Rube MCP 自動化 Veriphone 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/veriphone-automation/SKILL.md` |
| 781 | `vero-automation` | Vero | 透過 Composio / Rube MCP 自動化 Vero 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/vero-automation/SKILL.md` |
| 782 | `vestaboard-automation` | Vestaboard | 透過 Composio / Rube MCP 自動化 Vestaboard 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/vestaboard-automation/SKILL.md` |
| 783 | `virustotal-automation` | Virustotal | 透過 Composio / Rube MCP 自動化 Virustotal 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/virustotal-automation/SKILL.md` |
| 784 | `visme-automation` | Visme | 透過 Composio / Rube MCP 自動化 Visme 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/visme-automation/SKILL.md` |
| 785 | `waboxapp-automation` | Waboxapp | 透過 Composio / Rube MCP 自動化 Waboxapp 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/waboxapp-automation/SKILL.md` |
| 786 | `wachete-automation` | Wachete | 透過 Composio / Rube MCP 自動化 Wachete 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/wachete-automation/SKILL.md` |
| 787 | `waiverfile-automation` | Waiverfile | 透過 Composio / Rube MCP 自動化 Waiverfile 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/waiverfile-automation/SKILL.md` |
| 788 | `wakatime-automation` | Wakatime | 透過 Composio / Rube MCP 自動化 Wakatime 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/wakatime-automation/SKILL.md` |
| 789 | `wati-automation` | Wati | 透過 Composio / Rube MCP 自動化 Wati 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/wati-automation/SKILL.md` |
| 790 | `Wave Accounting Automation` | Wave Accounting | 透過 Composio / Rube MCP 自動化 Wave Accounting 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/wave-accounting-automation/SKILL.md` |
| 791 | `wave_accounting-automation` | Wave Accounting | 透過 Composio / Rube MCP 自動化 Wave Accounting 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/wave_accounting-automation/SKILL.md` |
| 792 | `weathermap-automation` | Weathermap | 透過 Composio / Rube MCP 自動化 Weathermap 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/weathermap-automation/SKILL.md` |
| 793 | `Webex Automation` | Webex | 透過 Composio / Rube MCP 自動化 Webex 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/webex-automation/SKILL.md` |
| 794 | `webscraping-ai-automation` | Webscraping AI | 透過 Composio / Rube MCP 自動化 Webscraping AI 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/webscraping-ai-automation/SKILL.md` |
| 795 | `webvizio-automation` | Webvizio | 透過 Composio / Rube MCP 自動化 Webvizio 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/webvizio-automation/SKILL.md` |
| 796 | `whautomate-automation` | Whautomate | 透過 Composio / Rube MCP 自動化 Whautomate 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/whautomate-automation/SKILL.md` |
| 797 | `winston-ai-automation` | Winston AI | 透過 Composio / Rube MCP 自動化 Winston AI 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/winston-ai-automation/SKILL.md` |
| 798 | `wit-ai-automation` | Wit AI | 透過 Composio / Rube MCP 自動化 Wit AI 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/wit-ai-automation/SKILL.md` |
| 799 | `wiz-automation` | Wiz | 透過 Composio / Rube MCP 自動化 Wiz 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/wiz-automation/SKILL.md` |
| 800 | `wolfram-alpha-api-automation` | Wolfram Alpha API | 透過 Composio / Rube MCP 自動化 Wolfram Alpha API 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/wolfram-alpha-api-automation/SKILL.md` |
| 801 | `woodpecker-co-automation` | Woodpecker Co | 透過 Composio / Rube MCP 自動化 Woodpecker Co 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/woodpecker-co-automation/SKILL.md` |
| 802 | `workable-automation` | Workable | 透過 Composio / Rube MCP 自動化 Workable 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/workable-automation/SKILL.md` |
| 803 | `Workday Automation` | Workday | 透過 Composio / Rube MCP 自動化 Workday 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/workday-automation/SKILL.md` |
| 804 | `workiom-automation` | Workiom | 透過 Composio / Rube MCP 自動化 Workiom 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/workiom-automation/SKILL.md` |
| 805 | `worksnaps-automation` | Worksnaps | 透過 Composio / Rube MCP 自動化 Worksnaps 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/worksnaps-automation/SKILL.md` |
| 806 | `writer-automation` | Writer | 透過 Composio / Rube MCP 自動化 Writer 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/writer-automation/SKILL.md` |
| 807 | `Xero Automation` | Xero | 透過 Composio / Rube MCP 自動化 Xero 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/xero-automation/SKILL.md` |
| 808 | `y-gy-automation` | Y Gy | 透過 Composio / Rube MCP 自動化 Y Gy 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/y-gy-automation/SKILL.md` |
| 809 | `yandex-automation` | Yandex | 透過 Composio / Rube MCP 自動化 Yandex 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/yandex-automation/SKILL.md` |
| 810 | `yelp-automation` | Yelp | 透過 Composio / Rube MCP 自動化 Yelp 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/yelp-automation/SKILL.md` |
| 811 | `ynab-automation` | YNAB | 透過 Composio / Rube MCP 自動化 YNAB 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/ynab-automation/SKILL.md` |
| 812 | `yousearch-automation` | Yousearch | 透過 Composio / Rube MCP 自動化 Yousearch 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/yousearch-automation/SKILL.md` |
| 813 | `zenrows-automation` | Zenrows | 透過 Composio / Rube MCP 自動化 Zenrows 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/zenrows-automation/SKILL.md` |
| 814 | `zenserp-automation` | Zenserp | 透過 Composio / Rube MCP 自動化 Zenserp 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/zenserp-automation/SKILL.md` |
| 815 | `zeplin-automation` | Zeplin | 透過 Composio / Rube MCP 自動化 Zeplin 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/zeplin-automation/SKILL.md` |
| 816 | `zerobounce-automation` | Zerobounce | 透過 Composio / Rube MCP 自動化 Zerobounce 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/zerobounce-automation/SKILL.md` |
| 817 | `zoho-automation` | Zoho | 透過 Composio / Rube MCP 自動化 Zoho 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/zoho-automation/SKILL.md` |
| 818 | `zoho-bigin-automation` | Zoho Bigin | 透過 Composio / Rube MCP 自動化 Zoho Bigin 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/zoho-bigin-automation/SKILL.md` |
| 819 | `Zoho Books Automation` | Zoho Books | 透過 Composio / Rube MCP 自動化 Zoho Books 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/zoho-books-automation/SKILL.md` |
| 820 | `Zoho Desk Automation` | Zoho Desk | 透過 Composio / Rube MCP 自動化 Zoho Desk 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/zoho-desk-automation/SKILL.md` |
| 821 | `zoho-inventory-automation` | Zoho Inventory | 透過 Composio / Rube MCP 自動化 Zoho Inventory 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/zoho-inventory-automation/SKILL.md` |
| 822 | `zoho-invoice-automation` | Zoho Invoice | 透過 Composio / Rube MCP 自動化 Zoho Invoice 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/zoho-invoice-automation/SKILL.md` |
| 823 | `zoho-mail-automation` | Zoho Mail | 透過 Composio / Rube MCP 自動化 Zoho Mail 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/zoho-mail-automation/SKILL.md` |
| 824 | `zoho_bigin-automation` | Zoho Bigin | 透過 Composio / Rube MCP 自動化 Zoho Bigin 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/zoho_bigin-automation/SKILL.md` |
| 825 | `zoho_books-automation` | Zoho Books | 透過 Composio / Rube MCP 自動化 Zoho Books 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/zoho_books-automation/SKILL.md` |
| 826 | `zoho_desk-automation` | Zoho Desk | 透過 Composio / Rube MCP 自動化 Zoho Desk 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/zoho_desk-automation/SKILL.md` |
| 827 | `zoho_inventory-automation` | Zoho Inventory | 透過 Composio / Rube MCP 自動化 Zoho Inventory 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/zoho_inventory-automation/SKILL.md` |
| 828 | `zoho_invoice-automation` | Zoho Invoice | 透過 Composio / Rube MCP 自動化 Zoho Invoice 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/zoho_invoice-automation/SKILL.md` |
| 829 | `zoho_mail-automation` | Zoho Mail | 透過 Composio / Rube MCP 自動化 Zoho Mail 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/zoho_mail-automation/SKILL.md` |
| 830 | `zoominfo-automation` | Zoominfo | 透過 Composio / Rube MCP 自動化 Zoominfo 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/zoominfo-automation/SKILL.md` |
| 831 | `zylvie-automation` | Zylvie | 透過 Composio / Rube MCP 自動化 Zylvie 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/zylvie-automation/SKILL.md` |
| 832 | `zyte-api-automation` | Zyte API | 透過 Composio / Rube MCP 自動化 Zyte API 的操作；使用前通常需先搜尋目前工具 schema，並確認該服務連線已啟用。 | `composio-skills/zyte-api-automation/SKILL.md` |

## 建議優先看的技能

- `skill-installer`：先學怎麼安裝其他技能。
- `skill-creator` / `template-skill`：如果你想自己做技能，先看這兩個。
- `connect` / `connect-apps`：如果你想讓 Codex 操作外部服務，先看這兩個。
- `gh-fix-ci` / `gh-address-comments` / `pr-review-ci-fix`：如果主要做 GitHub PR 與 CI 工作，這組最實用。
- `meeting-notes-and-actions` / `content-research-writer` / `spreadsheet-formula-helper`：偏日常生產力用途。
