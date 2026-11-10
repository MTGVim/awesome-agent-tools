# Interfaces

<!-- catalog: {"name": "Interfaces", "upstream": "https://github.com/jakubkrehel/skills", "types": ["skill", "plugin"], "agents": ["Claude Code"], "category": "design", "verification": "personal", "install_mode": "agent-guide", "installers": ["skills-cli"], "last_reviewed": "2026-11-10"} -->

> UI·타이포그래피·색상·접근성·레이아웃·제품 문구의 제작·리뷰를 위한 스킬 모음

- **Upstream:** https://github.com/jakubkrehel/skills
- **Types:** skill, plugin
- **Agents:** Claude Code (공식 플러그인 경로 확인; 다른 호스트의 실제 기능은 별도 확인)
- **Verification:** personal (2026-11-10 큐레이터 사용 확인; 개별 스킬 전체의 검증을 뜻하지 않음)
- **Install mode:** agent-guide
- **Install via:** Skills CLI 또는 Claude Code plugin
- **Last reviewed:** 2026-11-10

## Why use it?

`better-interface`가 접근성·레이아웃·문구·타이포그래피·색상·UI의 도메인별 스킬을 종합해 리뷰합니다. 변경 범위 리뷰는 `interface-review`, Figma·이미지 기반 구현은 `build-design`, 컴포넌트 변형 비교는 `variant`가 담당합니다. 하나의 제품 모음으로 등록하며, 큐레이터가 모든 스킬을 사용했다고 추론하지 않습니다.

## Requirements

선택한 호스트의 Agent Skills 또는 Claude Code plugin 지원이 필요합니다. Skills CLI 경로는 `npx` 실행 환경이 필요하지만 정확한 Node.js 최소 버전은 이번 upstream 자료에서 확인하지 못했습니다. 화면 검증에는 브라우저, Figma 기반 작업에는 연결·인증된 Figma MCP가 필요합니다. `teardown`의 실행 도우미에는 Node.js가 사용됩니다.

## Install

upstream README의 배포 경로는 다음과 같습니다. 설치 전 현재 CLI 도움말·기존 스킬·범위를 확인하고 승인받습니다. 이번 유지보수에서는 실행하지 않았습니다.

```bash
npx skills add jakubkrehel/skills
```

`skills/better-interface/SKILL.md` 등 개별 스킬 디렉터리가 있습니다. 필요한 스킬만 선택하고 모음 전체 설치를 기본으로 강제하지 않습니다. `better-interface`의 종합 리뷰에는 관련 `better-*` 스킬도 필요합니다.

Claude Code 공식 플러그인 경로:

```text
/plugin marketplace add jakubkrehel/skills
/plugin install interfaces@interfaces
```

두 경로를 중복 설치하기 전에 기존 등록을 확인합니다. Skills CLI 배포는 모든 호스트에서의 실행 호환성 보증이 아닙니다.

## Update

설치 당시 사용한 Skills CLI 또는 Claude Code 플러그인 관리 경로를 먼저 확인합니다. upstream README에 별도 갱신 명령이 없어 명령을 추정하지 않습니다. 해당 관리자의 현재 도움말과 변경 내역을 읽고 승인된 대상만 갱신하며 사용자 수정본을 보존합니다.

## Uninstall

실제 설치 경로와 등록을 확인한 뒤 사용한 관리자의 제거 절차로 이 모음의 선택한 스킬 또는 `interfaces@interfaces`만 제거합니다. 정확한 제거 명령은 upstream README에서 확인하지 못했습니다. 공용 스킬·다른 플러그인·사용자 산출물을 함께 지우지 않습니다.

## Verify

호스트가 설치한 스킬을 인식하는지 확인한 뒤, 작은 화면 하나를 범위로 정해 해당 스킬을 호출하고 실제 파일·화면 근거가 포함된 결과를 확인합니다. 등록 확인과 동작 검증은 별개입니다. 이번 조사에서는 설치·실행을 재검증하지 않았습니다.

## Caveats

- `interface-review`, `explain-interface`, `break`, `state-machine`, `variant`, `afk` 등은 upstream에서 사용자 호출로 구분합니다. 모음 설치를 상시 실행 승인으로 해석하지 않습니다.
- `afk`는 로컬 브랜치에서 장시간 개선 작업을 수행하는 별도 스킬입니다. 일반 UI 리뷰 권한으로 코드 수정·연결 서비스 조회까지 승인되었다고 가정하지 않습니다.
- `better-interface`는 각 도메인 소유 스킬이 없으면 해당 도메인을 미검토로 남깁니다. 단일 스킬만 설치해 전체 리뷰가 된다고 주장하지 않습니다.
- 사용 중이라는 큐레이터 확인은 보안 감사나 모든 개별 스킬의 호환성 검증을 의미하지 않습니다.

## Privacy & Updates

2026-11-10 revision `72bdd6121cd595f47fd21c9f23e374028c9cbacd`의 README·플러그인 manifest·선택한 SKILL.md와 일부 teardown 자원을 정적으로 확인했습니다. 자체 텔레메트리의 송신 데이터·기본값·수신자·opt-out, 자체 버전 확인·자동 코드 갱신 정책은 명시적으로 확인하지 못했습니다. **미확인을 외부 전송 없음으로 해석하지 않습니다.**

`build-design`은 Figma 링크를 처리할 때 Figma MCP와 인증을 요구합니다. `afk`는 연결된 분석·오류·배포 로그 등 서비스를 읽도록 지시하며, 원격 URL·브라우저·모델 사용 시의 통신은 호스트와 연결 서비스 설정에 따릅니다. 이는 자체 사용 통계와 구분합니다. 설치·갱신 시 패키지 관리자·GitHub·마켓플레이스 통신도 별개입니다. 전체 소스 네트워크 감사나 실행 감시는 수행하지 않았습니다.

## References

- [README](https://github.com/jakubkrehel/skills/blob/72bdd6121cd595f47fd21c9f23e374028c9cbacd/README.md)
- [플러그인 manifest](https://github.com/jakubkrehel/skills/blob/72bdd6121cd595f47fd21c9f23e374028c9cbacd/.claude-plugin/plugin.json)
- [Marketplace](https://github.com/jakubkrehel/skills/blob/72bdd6121cd595f47fd21c9f23e374028c9cbacd/.claude-plugin/marketplace.json)
- [better-interface](https://github.com/jakubkrehel/skills/blob/72bdd6121cd595f47fd21c9f23e374028c9cbacd/skills/better-interface/SKILL.md)
- [build-design](https://github.com/jakubkrehel/skills/blob/72bdd6121cd595f47fd21c9f23e374028c9cbacd/skills/build-design/SKILL.md)
- [afk](https://github.com/jakubkrehel/skills/blob/72bdd6121cd595f47fd21c9f23e374028c9cbacd/skills/afk/SKILL.md)
