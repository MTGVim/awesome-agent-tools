# Autoharness Codex

<!-- catalog: {"name": "Autoharness Codex", "upstream": "https://github.com/arm092/autoharness-codex", "types": ["skill"], "agents": ["Codex"], "category": "workflows", "verification": "unverified", "install_mode": "agent-guide", "last_reviewed": "2026-11-03"} -->

> Autoharness의 Codex 변형

- **Upstream:** https://github.com/arm092/autoharness-codex
- **Types:** skill
- **Agents:** Codex
- **Verification:** unverified
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-03

## Why use it?

Codex 세션 로그에서 학습한 반복 패턴을 증거와 함께 보관·검색하고 스킬을 병합하는 자동 유지보수 도구입니다.

## Requirements

로그인한 Codex CLI의 플러그인·훅 기능이 필요합니다. macOS 설치 패키지는 macOS 14+, Windows 설치 패키지에는 Python이 동봉되며 수동 설치는 Python 3.11+가 필요합니다.

## Install

원본 README는 플랫폼별 설치기를 제공합니다. macOS는 GitHub Releases의 설치 앱, Windows는 안내된 Windows 설치기를 사용합니다. 설치 전에 릴리스 출처와 코드 서명, 훅 등록 범위를 확인합니다.

## Update

원본 릴리스 설치기로 갱신하되 Codex를 종료하고 이전 프로그램 릴리스 및 학습 데이터 보존 여부를 확인합니다.

## Uninstall

원본 설치기의 제거 기능을 이용해 플러그인 등록을 해제합니다. 학습 데이터는 기본적으로 별도 보존 대상인지 먼저 확인합니다.

## Verify

Codex `/hooks`에서 새 훅의 신뢰·등록 상태를 확인하고 읽기 전용으로 저장된 학습 인덱스를 검사합니다.

## Caveats

백그라운드 학습은 Codex 사용량을 소비합니다. 지원되는 CLI 버전, 설치기 출처와 훅 권한을 확인해야 합니다.

## References

- [Upstream](https://github.com/arm092/autoharness-codex)
