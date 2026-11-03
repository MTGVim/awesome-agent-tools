# OpenShip

<!-- catalog: {"name": "OpenShip", "upstream": "https://github.com/oblien/openship", "types": ["tool"], "agents": [], "category": "utilities", "verification": "metadata", "install_mode": "agent-guide", "last_reviewed": "2026-11-03"} -->

> 도입 가치를 추가 평가할 후보

- **Upstream:** https://github.com/oblien/openship
- **Types:** tool
- **Agents:** Agent-specific compatibility not verified
- **Verification:** trial
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-03

## Why use it?

Git 저장소에서 앱을 빌드하고 배포하며 도메인 라우팅과 TLS를 처리하는 셀프호스팅 배포 플랫폼입니다. AI 에이전트 자체를 조정하는 도구는 아닙니다.

## Requirements

개인용 데스크톱 컨트롤 플레인과 상시 서버/팀용 셀프호스팅을 구분해야 합니다. 배포 대상 서버, SSH, Docker 및 포트 접근 범위를 확인합니다.

## Install

원본 README의 `Quick Start`에서 데스크톱 앱 또는 셀프호스팅 서버를 선택합니다. 로컬 데스크톱 앱은 배포 대상 서버를 SSH로 관리하며, 상시 배포는 서버 설치가 별도로 필요합니다. 원격 설치 스크립트는 내용을 검토한 뒤 실행합니다.

## Update

데스크톱 앱은 공식 릴리스, 서버 CLI는 설치한 채널의 공식 업데이트 방법을 따릅니다. 배포 중 서비스 가동 상태와 설정 백업을 확인합니다.

## Uninstall

컨트롤 플레인과 배포된 앱의 삭제는 다릅니다. 배포 중인 서비스·데이터·DNS·TLS 설정을 확인한 후 별도로 제거합니다.

## Verify

간단한 테스트 앱을 빌드·배포해 URL 라우팅과 TLS, 재배포까지 확인합니다.

## Caveats

서버/네트워크와 실제 배포 상태를 변경할 수 있습니다. AI 에이전트 스킬로 오인하지 말고 배포 인프라 도구로 다룹니다.

## References

- [Upstream](https://github.com/oblien/openship)
