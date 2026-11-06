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

### Orca 터미널 inline image 표시 문제 (2026-11-06)

Paste Preview에서 편집한 이미지를 전송하거나 Prismantis의 Mermaid pie 차트를 답변에 출력하면 inline image의 base64 문자열이 그대로 노출되는 현상이 관찰됐습니다. Ctrl+L로 화면 전체를 다시 그리면 정상 표시됩니다. 정확한 원인은 확인되지 않았습니다.

반복적으로 발생한다면 로컬 Claude Code mod에서 이미지 전송 완료 또는 Mermaid pie 답변 출력 완료를 감지하고 약 1초 뒤 Orca 터미널에 Ctrl+L을 보내는 임시 shim을 권장합니다. 이미지의 최초 렌더링 이후에 재그리기가 실행되어야 합니다. ORCA_TERMINAL_HANDLE 환경 변수가 없다면 아무것도 실행하지 않고, 이벤트 훅에서는 다른 mod의 동작을 방해하지 않도록 next(e)를 호출해야 합니다. 지연 중 터미널이 종료되거나 대상이 바뀐 경우에도 입력을 보내지 않으며, 해당 이미지 출력이 없으면 불필요한 재그리기를 수행하지 않습니다.

이는 설치된 해결책이 아니라 구현과 검증이 필요한 우회 방법입니다. Orca 또는 Claude Code 렌더러가 수정되면 제거합니다.

## References

- [Upstream](https://github.com/stablyai/orca)
