# Engram

- **Status:** Archived
- **Type:** tool, mcp
- **Reason:** `low-value`
- **Archived on:** 2026-11-24
- **Upstream:** https://github.com/Gentleman-Programming/engram
- **Previous guide:** `tools/context/engram.md`

## Why archived

큐레이터의 개인 사용 경험: **매 세션 자동 주입되는 컨텍스트 양이 과도**했고, **자동 업데이트 시 통합 구성이 자주 깨진다고 느껴** 현재 추천 목록과 My Daily Setup에서 제외합니다. 상류의 모든 환경에서 재현되는 결함이라는 주장은 아닙니다.

기존 Engram을 대신해 [Déjà Vu](../tools/context/deja-vu.md)를 시험 사용 중입니다. 대체제의 장기 안정성은 평가 중입니다.

## Previous usage notes

- 2026-11-06: 개인 환경에서 첫 프롬프트 훅이 10초 제한에 걸린 243건을 확인했습니다. 로컬 훅 수정 뒤 해당 측정은 약 0.06초로 감소했으며, 현재 배포판에서 재현 여부는 미확인입니다.
- 2026-11-07: 에이전트가 메모를 직접 고르고 SQLite FTS5로 검색하는 흐름을 유지하기 위해 다시 사용했습니다.
- 2026-11-11: 대체제가 마땅치 않아 다시 Daily Setup에 복원했습니다.

## Restore or reconsider

자동 주입량을 통제할 수 있고 업데이트 이후 통합이 안정적으로 유지되는지 확인할 경우 재평가합니다. 과거 설치 절차를 현재의 안전한 절차로 간주하지 않습니다.
