# XERJ

- **Status:** Archived
- **Type:** tool, mcp
- **Reason:** `needs-review`
- **Archived on:** 2026-11-10
- **Upstream:** https://github.com/xerj-org/xerj
- **Previous placement:** Cool Finds (찍먹 후보); 정식 Active 추천이나 Daily Setup으로 승격하지 않음

## Why archived

큐레이터는 텔레메트리와 유사한 전송 기능에 대한 우려와 기본 설치 절차의 복잡성 때문에 추가 검토가 필요하다고 판단했습니다. 이에 찍먹 후보에서 제외하고 판단 근거를 보관합니다. 이는 큐레이터의 보류 결정이며, 악성 동작이나 모든 환경에서의 설치 실패를 확인했다는 뜻은 아닙니다.

## 확인한 근거와 미확인 사항

2026-11-10에 upstream README의 revision `50e4ffded5518b1822cfac5450fa34d3829ab8ab`를 정적으로 확인했습니다.

- MCP 연결은 검색 노드를 먼저 실행한 뒤 별도의 stdio MCP 프로세스를 연결하는 구조로 안내합니다. 인증을 사용하는 노드는 추가 인증 설정이 필요합니다.
- README의 일부 클라이언트 검증 기록에는 `XERJ_DISABLE_FEEDBACK=true`를 설정하고 자동 field report가 관찰되지 않았다는 설명이 있습니다. 이 설정이 모든 외부 통신·텔레메트리·버전 확인을 끈다는 근거로 해석하지 않습니다.
- 송신 데이터, 기본 활성 여부, 수신자, 전송 조건, opt-out 범위와 자동 업데이트·버전 확인의 세부 동작은 이번 보관 작업에서 검증하지 않았습니다.
- 설치·실행·네트워크 감시는 수행하지 않았습니다. 정식 Active 항목이 아니었으므로 별도의 활성 도구 privacy audit 행은 만들지 않습니다.

출처: https://github.com/xerj-org/xerj/blob/50e4ffded5518b1822cfac5450fa34d3829ab8ab/README.md

## Restore or reconsider

복원 전에는 최신 upstream의 feedback·텔레메트리·외부 통신·업데이트 동작을 문서와 관련 구현에서 구분해 확인하고, 기본 설치·노드 실행·인증·MCP 연결의 최소 절차와 부작용을 검토합니다. 실제 설치와 동작 확인은 별도 승인을 받은 범위에서만 수행하며, 큐레이터의 복원 결정 없이 자동으로 후보나 Active 목록에 되돌리지 않습니다.
