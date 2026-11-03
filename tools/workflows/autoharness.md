# Autoharness

<!-- catalog: {"name": "Autoharness", "upstream": "https://github.com/tigerless-labs/autoharness", "types": ["plugin", "skill"], "agents": ["Claude Code"], "category": "workflows", "verification": "personal", "install_mode": "agent-guide", "last_reviewed": "2026-11-03"} -->

> 에이전트 스킬 생명주기 자동화

- **Upstream:** https://github.com/tigerless-labs/autoharness
- **Types:** plugin/skill
- **Agents:** Claude Code
- **Verification:** personal
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-03

## Why use it?

Claude Code 작업 세션에서 반복적으로 얻은 해결 패턴을 스킬로 축적하고, 유사 스킬을 병합하며 오래 쓰지 않는 자체 생성 스킬을 정리하는 하네스입니다.

## Requirements

Claude Code와 Python 3.11+가 필요합니다. 원본 README는 Linux·macOS를 지원 대상으로 명시합니다.

## Install

원본 README의 Install 섹션에서 마켓플레이스 등록과 플러그인 설치 식별자를 확인한 다음 설치합니다. 설치 전에 생성 스킬 저장 위치와 훅 사용 범위를 점검합니다.

## Update

원본에 안내된 `claude plugin marketplace update autoharness` 및 `claude plugin update autoharness@autoharness`를 사용합니다.

## Uninstall

원본에 안내된 `claude plugin uninstall autoharness@autoharness`를 사용하며, 생성된 개인 스킬과 학습 기록은 별도로 보존할지 결정합니다.

## Verify

스킬 인덱스가 생성되고 실제 세션 학습·병합 기록이 남는지 확인합니다. 사용자가 만든 기존 스킬이 바뀌지 않았는지 점검합니다.

## Caveats

자동 학습·스킬 수명주기 작업이 훅에서 수행됩니다. 자체 생성 스킬 외 파일을 수정하지 않는다는 원본의 소유권 원칙을 확인합니다.

## References

- [Upstream](https://github.com/tigerless-labs/autoharness)
