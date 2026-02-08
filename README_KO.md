# 🧠 AI 메모리 시스템 (RLM-Anchor)

> **RLM 기반 AI 어시스턴트를 위한 장기 기억**

[Recursive Language Models](https://arxiv.org/abs/2512.24601)(MIT 연구) 원칙에 기반한 AI 개발 환경을 위한 영구 메모리 시스템입니다 ([비디오 가이드](https://www.youtube.com/watch?v=huszaaJPjU8) 참조).

> AI 어시스턴트에게 채팅 세션 간에 유지되는 **영구 기억**을 제공하세요.

---

## 💡 문제점

AI와 새 채팅을 시작할 때마다 모든 것을 잊어버립니다:
- 프로젝트 아키텍처
- 과거 결정과 그 이유
- 알려진 버그와 해결 방법
- 당신의 코딩 스타일
- 어제 무엇을 작업했는지

**RLM-Anchor가 이 문제를 해결합니다.** AI에게 구조화된 장기 기억을 제공합니다 — 프로젝트 내의 간단한 Markdown 파일로.

---

---

## 🌟 기능

- **📁 13개의 정리된 카테고리** — 프로젝트 지식의 구조화된 저장
- **🔍 RLM 스타일 검색** — Examine → Decompose → Recurse → Aggregate
- **🌍 다국어 지원** — 모든 언어로 응답 및 항목
- **⚡ 간단한 명령어** — `/remember`, `/recall`, `/wakeup`, `/sleep`
- **🔄 컨텍스트 전달** — AI 모델 간 원활한 전환
- **📝 Markdown 기반** — 사람이 읽을 수 있고 Git 친화적
- **🔄 세션 지속성** — 세션 간 컨텍스트 유지

---

## 📦 빠른 시작 & 사용법

> ⚠️ **중요**: 각 프로젝트에는 별도의 RLM-Anchor 설치가 필요합니다! 여러 프로젝트에 하나의 메모리를 사용하면 충돌하는 컨텍스트로 인해 AI가 혼란스러워집니다. 새 프로젝트마다 항상 새로 설치하세요.

1. **`.agent/` 폴더 가져오기** Git을 통해 프로젝트로:
   ```bash
   git clone --depth 1 https://github.com/dvgmdvgm/AnchorGravity.git .temp && cp -r .temp/.agent . && rm -rf .temp
   ```
2. **언어 설정** `.agent/memory/13_preferences/language.md`에서
3. **이 프롬프트 실행** (전체 블록 복사):
   ```
   /anchor_agent 현재 프로젝트 디렉토리에서 컨텍스트를 구축하고 메모리를 올바르게 구성하는 데 도움이 될 데이터를 스캔하세요 (기술 데이터, 비즈니스 모델, 디자인 규칙 및 프로젝트 컨텍스트를 찾고 보존하기 위한 기타 모든 일반적인 템플릿)
   ```
4. **작업 시작** 채팅 명령 `/wakeup`으로.
5. **IDE에서 작업** (개발, 문제 해결, 비즈니스 결정, 모든 것을 평소처럼).

*작업 중 중요한 단계에서* `/remember`*를 사용하여 중요한 컨텍스트를 저장할 수 있습니다.*

6. **작업을 마치면** IDE에서, 예를 들어 자기 전에, `/sleep`을 실행하여 RLM-Anchor가 컨텍스트를 메모리에 저장하도록 합니다.

*이제 프로젝트 작업으로 돌아갈 때마다 — `/wakeup`으로 RLM-Anchor를 깨우고 세션 끝에 다시 `/sleep`으로 재우면 당신이 한 모든 것을 기억합니다.*

---

## 🌍 언어 설정

`.agent/memory/13_preferences/language.md` 편집:

```
LANGUAGE=ko    # 한국어
LANGUAGE=en    # 영어
LANGUAGE=ru    # 러시아어  
...
```

---

## ⚡ 명령어

| 명령어 | 설명 |
|--------|------|
| `/wakeup` | 세션 시작, 컨텍스트 로드 |
| `/sleep` | 세션 종료, 히스토리에 아카이브 |
| `/remember` | 정보를 메모리에 저장 |
| `/recall` | 메모리에서 정보 찾기 |
| `/handoff` | 모델 전환을 위한 요약 생성 |
| `/walkthrough` | 기능 문서 생성 |
| `/anchor_agent` | 프로젝트에 안전한 통합 |
| `/anchor_briefing` | 전체 프로젝트 브리핑 (모든 13개 카테고리) |
| `/anchor_backup` | 수동 백업 생성 (전송용) |
| `/anchor_restore` | ZIP 백업에서 복원 |
| `/anchor_remove` | 시스템 안전 제거 (백업 포함) |
| `/anchor_cleanup` | 스마트 메모리 정리 (TTL, 스코어링) |
| `/anchor_update` | GitHub에서 최신 버전으로 업데이트 |
| `/anchor_validate` | 메모리 무결성 검사 (5개 검사) |
| `/memory-stats` | 트렌드와 함께 메모리 통계 표시 |

📖 **전체 명령어 문서**: [COMMANDS.md](https://github.com/dvgmdvgm/AnchorGravity/blob/master/docs/COMMANDS.md)

---

## 📁 구조

```
.agent/
├── MEMORY_INDEX.md           # 메인 메모리 인덱스
├── skills/
│   └── MEMORY_SKILL.md       # AI 지침
├── workflows/                 # 명령어 정의
├── scripts/                   # Python 유틸리티
└── memory/
    ├── 01_project/           # 프로젝트 정보
    ├── 02_architecture/      # 시스템 아키텍처
    ├── 03_decisions/         # 아키텍처 결정 (ADR)
    ├── 04_domain/            # 비즈니스 도메인
    ├── 05_code/              # 코드 문서
    ├── 06_problems/          # 문제와 해결책
    ├── 07_context/           # 세션 컨텍스트
    ├── 08_people/            # 사람과 역할
    ├── 09_external/          # 외부 의존성
    ├── 10_testing/           # 테스팅
    ├── 11_deployment/        # 배포
    ├── 12_roadmap/           # 계획과 미래
    └── 13_preferences/       # 설정 및 언어
```

---

## 🔄 작동 방식

### RLM 스타일 프로세스

```
사용자 요청
    ↓
┌─────────────────────────────────────┐
│ 1. EXAMINE — 메모리 인덱스 읽기     │
│ 2. DECOMPOSE — 카테고리 결정        │
│ 3. RECURSE — 파일 내 검색           │
│ 4. AGGREGATE — 데이터 결합          │
└─────────────────────────────────────┘
    ↓
컨텍스트 응답 (설정된 언어로)
```

---

## 📝 사용 예시

### 🚀 초기화 / 연결
```
사용자: /anchor_agent
AI: 📋 통합 분석 중... [스캔하고 안전한 통합 옵션 제공]
```

### ☀️ 세션 시작
```
사용자: /wakeup
AI: 🚀 프로젝트 컨텍스트 로드 중...
    ✅ 세션 시작됨!
    📌 대기 중인 작업: 2
```

### 📌 정보 저장
```
사용자: /remember ACID 트랜잭션을 위해 PostgreSQL을 선택했습니다
AI: ✅ memory/03_decisions/ADR-002-database.md에 저장됨
```

### 🔍 지식 검색
```
사용자: /recall 왜 PostgreSQL을 선택했나요?
AI: 📁 메모리에서 발견:
    출처: memory/03_decisions/ADR-002-database.md
    ACID 트랜잭션 지원을 위해 PostgreSQL을 선택했습니다...
```

### 🔄 컨텍스트 전달 (Handoff)
```
사용자: /handoff
AI: 🔄 컨텍스트 전달 요약 생성 중... [다른 모델용 요약 생성]
```

### 📖 문서 생성
```
사용자: /walkthrough 새 인증
AI: 📖 워크스루 생성됨! memory/07_context/walkthroughs/2026-02-05_auth.md에 저장
```

### 📊 메모리 통계
```
사용자: /memory-stats
AI: 📊 통계: 42개 파일, 13개 카테고리...
```

### 🌙 세션 종료
```
사용자: /sleep
AI: 📝 세션 요약 중...
    ✅ 히스토리 저장됨.
    👋 다음에 봐요!
```

---

## 🛠️ 커스터마이징

### 새 카테고리 추가
1. `memory/`에 폴더 생성
2. `_index.md` 추가 
3. `MEMORY_INDEX.md` 업데이트

### 워크플로우 확장
`workflows/` 내 파일을 편집하여 명령어 커스터마이징.

---

## 📄 라이선스
MIT License — 포크하고 개선하세요!

---

## 🙏 감사의 말
[MIT의 RLM 연구](https://arxiv.org/abs/2512.24601)의 Recursive Language Models와 [이 비디오 가이드](https://www.youtube.com/watch?v=huszaaJPjU8)에서 영감을 받았습니다.
