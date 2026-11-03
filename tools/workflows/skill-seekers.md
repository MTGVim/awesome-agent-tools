# Skill Seekers

<!-- catalog: {"name": "Skill Seekers", "upstream": "https://github.com/yusufkaraaslan/Skill_Seekers", "types": ["skill", "tool"], "agents": [], "category": "workflows", "verification": "trial", "install_mode": "agent-guide", "last_reviewed": "2026-11-03"} -->

> 외부 자료를 에이전트 스킬로 변환

- **Upstream:** https://github.com/yusufkaraaslan/Skill_Seekers
- **Types:** skill/tool
- **Agents:** Agent-specific compatibility not verified
- **Verification:** trial
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-03

## Why use it?

문서 웹사이트·GitHub 저장소·PDF·영상·위키 등을 수집해 Agent Skills 및 RAG 시스템용 지식 자산으로 패키징합니다.

## Requirements

원본 README 기준 Python 3.10+와 Git이 필요합니다. 영상·MCP·모델 연결은 별도 의존성 또는 설정이 필요할 수 있습니다.

## Install

원본 빠른 시작의 기본 패키지는 아래와 같습니다.

```bash
pip install skill-seekers
```

그 뒤 공식 문서의 소스 유형별 추출·스킬 패키징 명령을 선택합니다.

## Update

기존 Python 환경과 추가 extras를 확인한 후 최신 안정 릴리스로 갱신합니다. 기존 생성된 스킬 결과물과 설정을 보존합니다.

## Uninstall

설치한 Python 환경에서 패키지를 제거하되, 추출해 생성한 지식 자산과 스킬을 자동 삭제하지 않습니다.

## Verify

작은 공개 문서를 대상으로 변환하고 스킬 패키지가 만들어지는지, 대상 AI 플랫폼의 문서 구조에 맞는지 확인합니다.

## Caveats

소스 유형별 추출 정확도가 다릅니다. 대용량 소스와 비공개 자료는 비용·저작권·보안 조건을 확인해야 합니다.

## References

- [Upstream](https://github.com/yusufkaraaslan/Skill_Seekers)
