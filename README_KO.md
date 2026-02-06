# 🧠 AI 메모리 시스템 (RLM-Anchor)

> **RLM 기반 AI 어시스턴트용 장기 메모리**

[Recursive Language Models](https://arxiv.org/abs/2512.24601) 원칙에 기반한 AI 기반 개발 환경용 영구 메모리 시스템입니다 ([비디오 가이드](https://www.youtube.com/watch?v=huszaaJPjU8) 참조).

---

## 🌟 주요 기능

- **📁 13개의 체계적인 카테고리** — 프로젝트의 모든 지식을 구조화하여 저장
- **🔍 RLM 스타일 검색** — Examine → Decompose → Recurse → Aggregate
- **🌍 다국어 지원** — 모든 언어로 응답 및 기록 가능
- **⚡ 간편한 명령** — `/remember`, `/recall`, `/wakeup`, `/sleep`
- **🔄 세션 지속성** — 세션 간 컨텍스트 유지
- **📝 Markdown 기반** — 가독성이 높고 Git 친화적

---

## 📦 빠른 시작 및 사용법 (Quick Start & Usage)

> ⚠️ **중요**: 각 프로젝트에는 자체 RLM-Anchor 설치가 필요합니다! 여러 프로젝트에 동일한 메모리를 사용하면 충돌하는 컨텍스트로 인해 AI 혼란이 발생합니다. 새 프로젝트마다 항상 새로 설치하세요.

1. **Git을 사용하여 `.agent/` 폴더를 프로젝트로 가져옵니다**:
   ```bash
   git clone --depth 1 https://github.com/dvgmdvgm/AnchorGravity.git .temp && cp -r .temp/.agent . && rm -rf .temp
   ```
2. **언어를 설정**하세요: `.agent/memory/13_preferences/language.md` 파일.
3. **이 프롬프트를 실행**하세요 (아래 전체 블록 복사):
   ```
   /anchor_agent 현재 프로젝트 디렉토리를 스캔하여 컨텍스트 구축 및 메모리 설정에 도움이 되는 데이터(기술 데이터, 비즈니스 모델, 디자인 규칙 및 프로젝트 컨텍스트를 찾고 보존하기 위한 기타 일반적인 템플릿)를 찾으세요
   ```
4. **작업 시작**은 채팅 명령 `/wakeup`으로 시작합니다.
5. **IDE에서 평소처럼 작업**하세요 (개발, 문제 해결, 비즈니스 결정 등).

*작업 중 중요한 단계에서* `/remember`*를 사용하여 중요한 컨텍스트를 저장할 수 있습니다.*

6. **작업을 마칠 때** (예: 취침 전) `/sleep` 명령을 실행하여 RLM-Anchor가 컨텍스트를 저장하도록 하세요.

*프로젝트로 돌아올 때마다* `/wakeup`*으로 RLM-Anchor를 깨우고, 작업 종료 시* `/sleep`*으로 잠재우면 모든 작업이 기억됩니다.*

---

## 🌍 언어 설정

`.agent/memory/13_preferences/language.md` 수정:

```
LANGUAGE=ko    # 한국어
LANGUAGE=en    # 영어
...
```

---

## ⚡ 명령 목록

| 명령 | 설명 |
|---------|----------|
| `/wakeup` | 세션 시작, 컨텍스트 로드 |
| `/sleep` | 세션 종료, 히스토리에 아카이브 |
| `/remember` | 정보를 메모리에 저장 |
| `/recall` | 메모리에서 정보 검색 |
| `/handoff` | 모델 교체를 위한 요약 생성 |
| `/walkthrough` | 기능 문서 생성 |
| `/anchor_agent` | 프로젝트에 안전하게 통합 |
| `/anchor_briefing` | 프로젝트 전체 브리핑 (13개 카테고리) |
| `/anchor_backup` | 수동 백업 생성 (전송용) |
| `/anchor_restore` | ZIP 백업에서 복원 |
| `/anchor_remove` | 시스템 안전 제거 (백업 포함) |
| `/anchor_cleanup` | 지능형 메모리 정리 (TTL, 스코어링) |
| `/memory-stats` | 메모리 통계 표시 |

---

## 🙏 크레딧
MIT의 [RLM 연구](https://arxiv.org/abs/2512.24601)(Recursive Language Models) 및 [이 비디오 가이드](https://www.youtube.com/watch?v=huszaaJPjU8)에서 영감을 받았습니다.
