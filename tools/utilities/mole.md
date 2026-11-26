# Mole

<!-- catalog: {"name": "Mole", "upstream": "https://github.com/tw93/Mole", "types": ["tool"], "agents": [], "category": "utilities", "verification": "personal", "install_mode": "cli", "last_reviewed": "2026-11-26"} -->

> macOS 시스템 청소·앱 제거·디스크 분석·최적화 및 개발 프로젝트 산출물 정리 CLI.

- **Upstream:** https://github.com/tw93/Mole
- **Types:** tool
- **Agents:** Standalone CLI (optional upstream agent integrations outside this entry's scope)
- **Verification:** personal (2026-11-26 큐레이터 사용 확인; 개별 기능 독립 검증 아님)
- **Install mode:** cli
- **Last reviewed:** 2026-11-26

## Why use it?

개발 도구 캐시와 빌드 산출물이 쌓인 Mac의 저장 공간을 분석하고 정리하며, 앱 제거와 시스템 상태 확인을 터미널에서 수행합니다.

## Requirements

macOS 12 이상, Intel 또는 Apple Silicon. Windows/Linux용 별도 브랜치도 있으나 이 가이드는 macOS CLI만 대상으로 합니다.

## Install

Homebrew 환경에서 `brew install mole`. 기존 설치와 배포 경로를 먼저 확인합니다. 네이티브 앱이나 별도 에이전트 플러그인은 설치 범위에 포함하지 않습니다.

## Update

Homebrew 설치는 `brew upgrade mole`, 스크립트 설치는 공식 `mo update` 경로를 확인합니다. Nix 설치는 Nix로 관리합니다.

## Uninstall

Homebrew 설치는 `brew uninstall mole`. 스크립트 설치의 공식 제거 명령은 `mo remove`이며 삭제 범위를 사전에 확인합니다. 사용자 설정과 로그의 잔존 여부는 별도 확인합니다.

## Verify

`mo --version`, `mo --help`, `mo status`, `mo analyze`로 설치 및 읽기 기능을 확인합니다. 정리 후보는 `mo clean --dry-run` 및 `mo purge --dry-run`으로 먼저 검토합니다.

## Caveats

`clean`, `purge`, `installer`는 영구 삭제할 수 있습니다. 실행 전 dry-run 결과를 검토하고 사용자 승인을 받습니다. `mo clean --whitelist`로 보호할 캐시를 설정하며, 기본 휴지통 청소도 주의합니다. 전체 CLI를 sudo로 실행하지 않습니다. 앱 제거는 개인 데이터 보존 기본값과 실제 선택 경로를 확인합니다.

## Privacy & Updates

2026-11-26 상류 README 확인. 사용 통계 전송 여부, 기본값, 수신처, opt-out 및 자동 버전 확인/설치 여부는 미확인입니다. 수동 `mo update`를 지원합니다. 작업 로그는 로컬 `~/Library/Logs/mole/operations.log`에 기록되며 `MO_NO_OPLOG=1`로 끌 수 있습니다. 이는 네트워크 전송 opt-out이 아닙니다. 소스 전체 감사와 실제 네트워크 검증은 하지 않았습니다.

## References

- [Upstream README](https://github.com/tw93/Mole/blob/main/README.md)
- [Releases](https://github.com/tw93/Mole/releases)
- [Security](https://github.com/tw93/Mole/blob/main/SECURITY.md)
