# Archify

<!-- catalog: {"name": "Archify", "upstream": "https://github.com/tt-a1i/archify", "types": ["tool"], "agents": ["Claude Code", "Codex", "Hermes"], "category": "visual", "verification": "personal", "install_mode": "agent-guide", "installers": ["skills-cli"], "last_reviewed": "2026-11-03"} -->

> 설명 산출물 구성 및 시각화 도구

- **Upstream:** https://github.com/tt-a1i/archify
- **Types:** tool
- **Agents:** Claude Code, Codex, Hermes
- **Verification:** personal
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-03

## Why use it?

질문·계획·시스템 구조를 인터랙티브 HTML로 구성하고, 세부 설명 카드와 탐색 가능한 다이어그램으로 공유하도록 돕는 Agent Skill입니다.

## Requirements

Claude Code·Codex에서는 완전한 렌더링·검증 경로를, Hermes에서는 별도의 커뮤니티 Skill 통합을 제공합니다. 기능 범위는 동일하지 않을 수 있고 Node.js가 필요합니다.

## Install

원본 README는 에이전트가 공식 `llms.txt`를 읽어 설치하게 하는 방법을 기본으로 제안합니다. Codex에서 미리 체험하는 공식 예시는 다음과 같습니다.

```bash
npx skills use tt-a1i/archify@archify --agent codex
```

Hermes 커뮤니티 통합은 `hermes skills install skills-sh/tt-a1i/archify/archify -y` 경로를 안내합니다. 원본을 확인한 뒤 선택합니다.

## Update

Archify는 업데이트를 자동 설치하지 않고 새 안정 버전이 있음을 알릴 수 있습니다. 현재 설치된 스킬과 원본 릴리스의 변경 사항을 비교한 뒤 사용자 승인을 받아 갱신합니다.

## Uninstall

설치한 에이전트의 스킬 디렉터리에서 Archify만 제거합니다. 사용자가 만든 HTML 산출물은 보존합니다.

## Verify

간단한 아키텍처 다이어그램을 생성해 HTML을 열어 보고, 링크·노드·검증 기능이 실제로 작동하는지 확인합니다.

## Caveats

도구의 전체 기능은 에이전트별로 다를 수 있습니다. 원본에서 명시한 Mermaid 자동 파싱·범용 자동 레이아웃·WYSIWYG 편집은 현재 범위 밖입니다.

## References

- [Upstream](https://github.com/tt-a1i/archify)
