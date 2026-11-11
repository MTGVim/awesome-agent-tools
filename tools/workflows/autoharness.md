# Autoharness

<!-- catalog: {"name": "Autoharness", "upstream": "https://github.com/tigerless-labs/autoharness", "types": ["plugin", "skill"], "agents": ["Claude Code"], "category": "workflows", "verification": "unverified", "install_mode": "cli", "last_reviewed": "2026-11-11"} -->

> 실제 세션에서 스킬을 배우고 사용 빈도로 유지·통합·보관하는 Claude Code 플러그인

- **Upstream:** https://github.com/tigerless-labs/autoharness
- **Types:** plugin, skill
- **Agents:** Claude Code
- **Verification:** unverified
- **Install mode:** cli
- **Last reviewed:** 2026-11-11

## Why use it?

Stop 훅이 세션 기록의 구간을 수집하고, 백그라운드 reflector(Haiku)가 기존 스킬과 비교해 변경을 제안합니다. promoter가 구조·소유권 등을 검증한 뒤 적용하고, curator가 겹치는 스킬을 통합합니다. 생성 후 실제 사용 빈도로 유지 여부를 판단하며, 쓰이지 않는 스킬은 삭제 대신 되돌릴 수 있는 archive로 이동합니다. upstream은 자신이 만든 스킬만 관리한다고 명시합니다.

2026-11-11 복원은 설치·child 실행 사용자 보고와 새 격리 옵션을 바탕으로 한 재평가입니다. 스킬 품질·비용 대비 가치는 아직 미검증이며, 1–2주 재측정 전에는 My Daily Setup에 추가하지 않습니다.

## Requirements

- 로그인된 Claude Code와 PATH의 **Python 3.11+**(`python3`). upstream은 Linux·macOS를 안내합니다.
- 사용자 보고: 2026-11-11 Claude Code **2.1.322**에서 설치 및 child 호출 확인. 최소 지원 Claude Code 버전이라는 뜻은 아닙니다.
- 학습용 `claude -p` 호출도 사용자의 플랜 사용량을 소비합니다. API 인증이면 해당 API 비용이 발생합니다.

## Install

터미널에서 공식 marketplace/plugin 식별자로 등록합니다.

```sh
claude plugin marketplace add tigerless-labs/autoharness
claude plugin install autoharness@autoharness
```

Claude Code를 재시작하거나 `/reload-plugins`로 다시 로드합니다. 위 설치 명령은 2026-11-11 사용자 실행 확인 보고이며, 이 문서 작업에서 설치하지 않았습니다.

## Update

일반 공식 절차는 marketplace 새로고침 → plugin 갱신 → Claude Code 재시작입니다.

```sh
claude plugin marketplace update autoharness
claude plugin update autoharness@autoharness
```

**고정 버전 주의:** 2026-11-11 확인한 manifest는 2026-09-04 이후 여전히 `0.5.3`입니다. upstream 설명대로 캐시는 manifest 버전을 기준으로 하므로 `claude plugin update`의 버전 비교나 marketplace `autoUpdate`만으로는 이후 commit이 반영되지 않을 수 있습니다. 서드파티 marketplace 자동 갱신은 기본 OFF이며, 켜도 이 문제를 해결하지 못합니다.

먼저 `~/.claude/plugins/installed_plugins.json`의 해당 plugin·scope의 `gitCommitSha`를 읽고 upstream HEAD와 비교합니다. 사용자 정의 Claude 설정 디렉터리를 쓰면 그 경로를 확인합니다.

```sh
git ls-remote https://github.com/tigerless-labs/autoharness HEAD
```

SHA가 다르면 활성 scope·설정과 학습 상태를 먼저 보존한 뒤 다음 절차로 캐시를 갱신하고 재시작합니다. 설치 뒤 `gitCommitSha`를 다시 대조합니다.

```sh
claude plugin marketplace update autoharness
claude plugin uninstall --keep-data autoharness@autoharness
claude plugin install autoharness@autoharness
```

2026-11-11 사용자는 이 재설치 후 enabled 상태와 env 설정이 유지됨을 확인했다고 보고했습니다. 다른 scope·버전까지의 보존 보장은 아니며, 이 작업에서는 재실행하지 않았습니다.

## Uninstall

```sh
claude plugin uninstall autoharness@autoharness
claude plugin marketplace remove autoharness
```

등록 해제는 학습 데이터 삭제가 아닙니다. 기본 전역 상태 `~/.claude/autoharness/`, 각 저장소의 `.claude/autoharness/`, 생성 스킬 `~/.claude/skills/`·`<repo>/.claude/skills/`와 그 아래 `.archive/`는 별도로 남습니다. 사용자 환경에서 보고된 `~/.claude/autoharness-projects/`도 잔여 확인 대상이지만 현재 source에서 이 이름은 찾지 못했으므로 기본 생성 경로로 단정하지 않습니다.

`CLAUDE_CONFIG_DIR`, `AUTOHARNESS_GLOBAL_ROOT`, `AUTOHARNESS_PROJECT_DIR`, `AUTOHARNESS_STATE_HOME`을 설정했다면 실제 위치가 달라집니다. 공유 `~/.claude/skills/.archive/`나 스킬 루트 전체를 지우지 말고 `.ledger.jsonl`의 self-authored 표식과 소유권을 확인합니다. skill prefix를 썼다면 `.git/info/exclude`에 추가된 해당 한 줄도 검토합니다. 이 문서 작업에서는 제거하지 않았습니다.

## Verify

1. `claude plugin list`에서 등록·enabled 상태를 확인합니다. 이것만으로 child 성공이나 스킬 학습 성공을 입증하지 못합니다.
2. **별도 승인 후** child 실행·인증·실제 모델을 확인할 수 있습니다. 아래 호출도 플랜을 소비하며 권한 프롬프트를 건너뜁니다.

   ```sh
   AUTOHARNESS_CHILD_SESSION=1 claude -p --agent autoharness:reflector --dangerously-skip-permissions --output-format json
   ```

   `modelUsage`가 Haiku인지 확인합니다. 이 진단 호출은 훅이 자동으로 추가하는 격리 인자를 포함하지 않습니다. 격리를 직접 비교할 때에는 Caveats의 인자도 명시해야 합니다.
3. 대표 세션 이후 상태 디렉터리의 `runs/`·`last_run.json`, 생성 스킬의 ledger와 실제 사용 횟수를 구분해 확인합니다. 제안 성공과 promoter 적용 성공도 다릅니다.

사용자 보고(2026-11-11): 설치·enabled와 reflector의 Haiku 실행 확인. 같은 날 child 컨텍스트는 격리 ON 약 **11.9k**, OFF 약 **18.2k 토큰**이었습니다. 개인 환경의 측정이며 일반 성능 보장이나 독립 재현 결과가 아닙니다. 전체 학습 효과는 미검증이므로 `unverified`를 유지합니다.

## Caveats

- **Child 격리는 기본 OFF:** `AUTOHARNESS_CHILD_ISOLATION=1`일 때 reflector·curator에 `--setting-sources "" --plugin-dir <autoharness-plugin-root> --no-session-persistence`를 추가합니다. 사용자·프로젝트 settings를 읽지 않고 이 plugin만 로드하며 child 세션을 보존하지 않습니다. upstream [PR #168](https://github.com/tigerless-labs/autoharness/pull/168)은 **2026-11-10** 병합됐습니다. README는 `apiKeyHelper` 같은 settings 기반 인증 의존성 때문에 기본값을 OFF로 둔다고 설명합니다. 격리가 인증·모든 외부 통신을 없애는 것은 아닙니다.
- 기본 bundle carrier의 reflector와 curator는 **Haiku**입니다. child는 `--dangerously-skip-permissions`로 실행되지만 agent 도구는 `Read/Grep/Glob/stage_skill`로 제한되고, 실제 쓰기는 별도 promoter 검증을 거칩니다. 이는 완전한 보안 sandbox나 전체 감사 결과가 아닙니다. 선택형 fork carrier는 부모 대화를 재개·분기하므로 기본 subagent와 같은 컨텍스트·모델 조건으로 가정하지 않습니다.
- 기본 reflection은 **tool call 50회**(`AUTOHARNESS_REFLECT_EVERY_N`), consolidation은 **250회**(`AUTOHARNESS_CONSOLIDATE_EVERY_N`)입니다. 턴 수가 아닙니다. cadence를 낮추면 child 비용이 늘 수 있습니다.
- transcript에는 민감 정보와 신뢰할 수 없는 지시가 섞일 수 있습니다. redaction·제안 검증이 모든 누출·prompt injection을 막는다고 보장하지 않습니다.

## Privacy & Updates

2026-11-11 upstream **`57a8f4ef9e4d414e64c31c8111a6af882d23375e`**의 README·manifest·child 실행 경로 및 `src/` 정적 검색을 확인했습니다. 자체 사용 통계 전송이나 자체 버전 조회 구현은 찾지 못했으나, 부재를 입증하는 전체 소스·실행 감사는 아닙니다. 사용자도 같은 revision의 정적 검토를 보고했습니다.

주 기능은 transcript 일부·스킬 문맥을 `claude -p`로 모델 서비스(기본 Anthropic)에 전달하고 플랜/API 사용량을 소비합니다. 호스트 인증·provider 설정에 따라 실제 수신 경로는 달라질 수 있습니다. 학습을 유지하면서 이 모델 통신을 끄는 방법은 확인하지 못했으며, 중단하려면 plugin을 비활성화하거나 제거해야 합니다. `AUTOHARNESS_NOTIFY_CMD`를 별도로 설정하면 실행 기록을 사용자가 지정한 명령·외부 서비스에 전달할 수도 있습니다(기본 unset).

자체 코드 자동 갱신과 Claude Code marketplace 갱신은 다릅니다. 기본 OFF인 marketplace 자동 갱신과 고정 manifest 버전의 한계는 Update를 따릅니다. 통계 검색 결과를 Claude Code 자체 telemetry·업데이트 통신의 부재로 확대하지 않습니다.

## 보관 이력

- **Archived on:** 2026-11-06
- **Reason:** `low-value`

생성 스킬 30개 중 실제 사용 누적 1회, 학습 세션의 주간 비용 약 3%로 추정했습니다. 플러그인을 끄고 생성 스킬 30개를 개인 환경의 archive로 옮겼습니다. 기존 `250 / 1000`은 활성 설정이 아닙니다.

개인 환경의 평가이며 업스트림 전체의 결함이나 폐기를 뜻하지 않습니다.

2026-11-11 복원: 11-06 판단 이후 child 격리 옵션이 추가돼 같은 지표(생성 스킬 대비 사용 수, 주간 비용 비율)로 다시 측정 중이다.

## References

- [README · 고정 revision](https://github.com/tigerless-labs/autoharness/blob/57a8f4ef9e4d414e64c31c8111a6af882d23375e/README.md)
- [plugin manifest](https://github.com/tigerless-labs/autoharness/blob/57a8f4ef9e4d414e64c31c8111a6af882d23375e/.claude-plugin/plugin.json)
- [child 실행·격리](https://github.com/tigerless-labs/autoharness/blob/57a8f4ef9e4d414e64c31c8111a6af882d23375e/src/autoharness/hook/spawn.py)
- [reflector 모델·도구](https://github.com/tigerless-labs/autoharness/blob/57a8f4ef9e4d414e64c31c8111a6af882d23375e/agents/reflector.md)
- [상태·archive 경로](https://github.com/tigerless-labs/autoharness/blob/57a8f4ef9e4d414e64c31c8111a6af882d23375e/src/autoharness/lib/layer.py)
- [Claude Code plugin 버전·캐시 기준](https://code.claude.com/docs/en/plugins-reference#version-management)
- [Claude Code marketplace 자동 갱신 기본값](https://code.claude.com/docs/en/plugins/install)
