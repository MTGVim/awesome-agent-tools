# Skill Creator

<!-- catalog: {"name": "Skill Creator", "upstream": "https://github.com/openai/skills", "types": ["skill"], "agents": ["Codex"], "category": "workflows", "verification": "personal", "install_mode": "agent-guide", "last_reviewed": "2026-11-03"} -->

> 에이전트 스킬 작성 및 개선 가이드. 벤더별 구현 차이 있음

- **Upstream:** https://github.com/openai/skills
- **Types:** skill
- **Agents:** Codex
- **Verification:** personal
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-03

## Why use it?

Codex에서 Agent Skills의 설명, 지침, 도구 구성을 설계·개선하는 제작 흐름입니다. 다만 원본 `openai/skills` 저장소는 폐기 안내를 게시했으며, 새로운 예제는 `openai/plugins`를 가리킵니다.

## Requirements

Codex의 현재 Skills/Plugins 기능과 공식 작성 문서를 확인합니다. `openai/skills`는 더 이상 신규 배포의 권장 기준이 아닙니다.

## Install

별도 구버전 저장소를 복사하기보다 최신 Codex 기본 제공 스킬 또는 [OpenAI Plugins](https://github.com/openai/plugins)의 제작 안내를 우선 확인합니다.

## Update

기존 `openai/skills`의 내용을 강제로 갱신하지 말고 현재 Codex의 플러그인 및 스킬 작성 가이드를 검토합니다.

## Uninstall

별도로 복사한 사용자 제작 스킬만 해당 스킬 경로에서 확인 후 제거합니다. Codex 기본 제공 `.system` 스킬은 직접 삭제하지 않습니다.

## Verify

Codex에서 스킬 제작 기능을 호출하고 새로 만든 SKILL.md가 검색·실행되는지 확인합니다.

## Caveats

**업스트림 저장소 폐기(Deprecated)**: https://github.com/openai/skills 는 새 프로젝트를 https://github.com/openai/plugins 로 안내합니다. 기존 링크는 역사적 참고로만 유지합니다.

## References

- [Upstream](https://github.com/openai/skills)
