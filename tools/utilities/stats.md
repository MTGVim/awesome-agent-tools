# Stats

<!-- catalog: {"name": "Stats", "upstream": "https://github.com/exelban/stats", "types": ["tool"], "agents": [], "category": "utilities", "verification": "personal", "install_mode": "agent-guide", "last_reviewed": "2026-11-03"} -->

> macOS 자원 사용량 모니터링

- **Upstream:** https://github.com/exelban/stats
- **Types:** tool
- **Agents:** No agent-specific integration documented
- **Verification:** personal
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-03

## Why use it?

macOS 메뉴 막대에서 CPU·GPU·메모리·센서·팬·네트워크·배터리 상태를 보여주는 시스템 모니터입니다.

## Requirements

macOS 12 이상 안정 버전을 지원합니다. 팬 제어·원격 모니터링 등은 별도의 권한과 설정이 필요합니다.

## Install

macOS Homebrew에서 설치합니다.

```bash
brew install stats
```

또는 GitHub Releases에서 `Stats.dmg`를 다운로드하여 Applications로 이동합니다.

## Update

Homebrew 설치는 해당 cask 업데이트를 사용하고, 수동 설치는 공식 릴리스와 기존 버전을 비교합니다.

## Uninstall

원본 앱은 SMC helper까지 정리하는 제거 스크립트를 제공합니다. 실행 전에 스크립트 권한과 사용자 설정 보존 여부를 확인합니다.

## Verify

앱 메뉴 막대의 CPU·메모리·네트워크 사용량이 실제 시스템 상태와 함께 갱신되는지 확인합니다.

## Caveats

### 텔레메트리와 네트워크 (2026-11-04 문서 확인)

상류 README는 텔레메트리·분석 수집이 없다고 명시합니다. 다만 업데이트 확인 및 공인 IP 조회를 위한 외부 요청은 발생할 수 있습니다. [Upstream README](https://github.com/exelban/stats#external-api)

상태 비교: [Privacy, Telemetry & Updates](../../docs/privacy-and-updates.md). 실제 설치된 버전의 설정을 다시 확인합니다.

별도 원격 모니터링 설정은 계정·네트워크 연결을 수반할 수 있으며, 단순 로컬 메뉴 막대 앱과 구분해야 합니다.

## References

- [Upstream](https://github.com/exelban/stats)
