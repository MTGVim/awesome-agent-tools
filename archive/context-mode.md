# Context Mode

- **Status:** Archived
- **Reason:** `low-value`
- **Archived on:** 2026-11-10

## Why archived

큐레이터가 시험 사용한 결과 이미지 등을 읽는 작업에 방해가 됐으며, 적용 후 세션이 더 길어졌다는 체감은 없었습니다.

## Historical guide

아래는 시험 당시의 가이드입니다. 현재 설치 절차는 업스트림 문서를 확인합니다.

<!-- catalog: {"name":"Context Mode","upstream":"https://github.com/mksglu/context-mode","types":["plugin"],"agents":["Claude Code"],"category":"context","verification":"trial","install_mode":"agent-guide","last_reviewed":"2026-11-06"} -->

> 도구 출력을 로컬에서 분리·검색해 컨텍스트를 절약하는 플러그인

- **Upstream:** https://github.com/mksglu/context-mode
- **Types:** plugin
- **Agents:** Claude Code
- **Verification:** trial
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-06

## Why use it?

도구 출력을 로컬에서 분리·검색해 컨텍스트를 절약하는 플러그인. 출력 압축 시 중요한 정보가 보존되는지 확인해야 합니다.

## Requirements

운영체제와 에이전트별 지원 범위는 원본에서 확인합니다.

## Install

[공식 설치 안내](https://github.com/mksglu/context-mode)를 확인합니다.

## Update

설치 방식에 따라 공식 업데이트 절차를 따릅니다.

## Uninstall

해당 도구가 추가한 설정과 실행 파일만 제거합니다.

## Verify

원본과 축약 출력의 정보 보존, 실제 세션 토큰과 디버깅 품질을 비교합니다.

## Caveats

### 개인 사용 평가 (2026-11-06)

재독량 중 약 17%인 도구 결과를 줄이려고 1주 시험합니다. 시험 당시 절감률을 측정하지 않았으며 My Daily Setup에도 포함하지 않았습니다. 무료 로컬 플러그인과 별도 유료 Gateway를 구분합니다.

## Privacy & Updates

2026-11-10에 확인한 업스트림 문서에 따르면 로컬 플러그인은 사용 통계와 오류 보고를 전송하지 않습니다. `context-mode doctor`를 실행하면 npm에서 버전을 조회하며, 필요하면 Git 릴리스 태그를 조회합니다. 호스트의 자동 갱신 여부는 확인하지 않았습니다. Gateway에는 별도 정책이 적용됩니다. [보안 및 개인정보 안내](https://github.com/mksglu/context-mode#security-and-privacy)

## References

- [Upstream](https://github.com/mksglu/context-mode)
