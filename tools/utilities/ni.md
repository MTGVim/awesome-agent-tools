# ni

<!-- catalog: {"name": "ni", "upstream": "https://github.com/antfu-collective/ni", "types": ["tool"], "agents": [], "category": "utilities", "verification": "personal", "install_mode": "agent-guide", "last_reviewed": "2026-11-03"} -->

> 패키지 매니저를 자동 감지하는 명령 래퍼

- **Upstream:** https://github.com/antfu-collective/ni
- **Types:** tool
- **Agents:** No agent-specific integration documented
- **Verification:** personal
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-03

## Why use it?

프로젝트의 잠금 파일과 현재 패키지 관리자 환경을 감지하여 npm·pnpm·yarn·bun 등에서 대응되는 설치·실행 명령을 선택합니다.

## Requirements

Node.js 및 사용하는 패키지 매니저가 설치되어 있어야 합니다. 설치하려는 패키지 매니저에 따라 런타임 요구 사항이 다릅니다.

## Install

원본 README는 전역 설치를 안내합니다.

```bash
npm i -g @antfu/ni
```

macOS Homebrew는 `brew install ni`도 지원합니다.

## Update

설치한 패키지 매니저로 `@antfu/ni` 또는 Homebrew 패키지를 갱신합니다.

## Uninstall

`npm uninstall -g @antfu/ni` 또는 사용한 Homebrew 제거 기능으로 도구만 삭제합니다.

## Verify

npm·pnpm 등의 잠금 파일이 있는 샘플 프로젝트에서 `ni`, `nr`, `nlx`가 해당 매니저 명령을 선택하는지 확인합니다.

## Caveats

잠금 파일 감지는 프로젝트 설정을 따릅니다. 기존에 사용한 패키지 매니저를 자동 변경하거나 종속성을 마이그레이션하는 도구는 아닙니다.

## References

- [Upstream](https://github.com/antfu-collective/ni)
