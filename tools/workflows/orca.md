# Orca

<!-- catalog: {"name": "Orca", "upstream": "https://github.com/stablyai/orca", "types": ["tool"], "agents": ["Claude Code","Codex","Hermes"], "category": "workflows", "verification": "personal", "install_mode": "agent-guide", "last_reviewed": "2026-11-03"} -->

> 컴퓨터 사용 및 GUI 자동화 도구

- **Upstream:** https://github.com/stablyai/orca
- **Types:** tool
- **Agents:** Claude Code, Codex, Hermes
- **Verification:** personal
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-03

## Why use it?

워크트리별 에이전트 병렬 실행·원격 SSH·디자인 검사·리뷰 기능이 있는 통합 개발 환경입니다. GUI 컴퓨터 조작은 여러 부가 기능 중 하나입니다.

## Requirements

macOS·Windows·Linux용 앱이며, 원격 SSH 및 워크트리·모바일 기능은 환경 설정이 필요합니다. macOS Homebrew에서는 bare `orca`가 다른 패키지이므로 정식 cask 경로를 사용해야 합니다.

## Install

공식 [다운로드](https://onorca.dev/download)에서 설치합니다. macOS Homebrew 경로는 아래와 같습니다.

```bash
brew install --cask stablyai/orca/orca
```

업그레이드는 `brew upgrade --cask stablyai/orca/orca`입니다.

## Update

기존 설치 방식과 변경 이력을 확인한 다음 원본 저장소에서 권장하는 업데이트 절차를 적용합니다.

## Uninstall

설치 이력을 확인해 해당 도구가 추가한 파일·등록만 제거합니다. 공유 설정과 다른 도구는 보존합니다.

## Verify

설치 목록 또는 명령 도움말을 확인하고, 핵심 기능을 최소 한 번 실행해 봅니다.

## Caveats

### 텔레메트리와 네트워크 (2026-11-04 문서 확인)

공식 배포판은 PostHog Cloud로 익명 사용 이벤트를 보냅니다. `Settings → Privacy → Share anonymous usage data`에서 끄거나 `DO_NOT_TRACK=1` / `ORCA_TELEMETRY_DISABLED=1`을 설정합니다. 1.4.148 Windows 빌드에서 초기 활성화가 관찰됐지만 모든 버전에 일반화하지 않습니다. 공식 안내에 따르면 Orca는 기본 자동 업데이트를 사용하며, Linux `.deb`/`.rpm`은 업데이트 존재만 안내합니다. [Privacy](https://www.onorca.dev/docs/telemetry) · [Updates](https://www.onorca.dev/docs/install)

상태 비교: [Privacy, Telemetry & Updates](../../docs/privacy-and-updates.md). 실제 설치된 버전의 설정을 다시 확인합니다.

macOS·Windows·Linux용 앱이며, 원격 SSH 및 워크트리·모바일 기능은 환경 설정이 필요합니다. macOS Homebrew에서는 bare `orca`가 다른 패키지이므로 정식 cask 경로를 사용해야 합니다.

설치 안내를 확인한 것이지 실제 사용자 환경에서 작동을 검증했다는 뜻은 아닙니다.

## References

- [Upstream](https://github.com/stablyai/orca)
