# Autoharness Codex

<!-- catalog: {"name": "Autoharness Codex", "upstream": "https://github.com/arm092/autoharness-codex", "types": ["skill"], "agents": ["Codex"], "category": "workflows", "verification": "unverified", "install_mode": "agent-guide", "last_reviewed": "2026-11-11"} -->

> tigerless-labs/autoharness에서 영감을 받은 Codex용 독립 구현(fork 아님)

- **Upstream:** https://github.com/arm092/autoharness-codex
- **Types:** skill
- **Agents:** Codex
- **Verification:** unverified
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-11

## Why use it?

Codex 세션 로그에서 반복 교훈을 추출하고, 근거·소유권을 검증한 스킬을 보관·검색·통합하는 자동 유지보수 도구입니다. 자체 라이브러리만 관리하며 복구 가능한 이력을 유지합니다. Claude Code판의 fork가 아니라 그 설계에서 영감을 받은 독립 구현입니다.

## Requirements

- 로그인된 Codex CLI의 native plugin·hook 기능과 해당 child 격리 플래그 지원이 필요합니다. 최소 버전은 일반화하지 않으며 설치 전 CLI 도움말·doctor 결과를 확인합니다.
- macOS 설치 패키지는 **macOS 14+**, arm64·x86_64용 Python runtime을 포함합니다. Windows 설치 패키지도 Python을 동봉합니다. source/manual 설치는 PATH의 **Python 3.11+**가 필요합니다.
- 백그라운드 `codex exec` 학습은 사용자의 Codex 플랜 사용량을 소비합니다.

## Install

공식 README는 macOS DMG의 설치 앱과 Windows Setup을 제공합니다. Codex를 종료하고 릴리스 출처·checksum·등록 범위를 먼저 확인합니다. macOS 패키지는 ad-hoc 서명이며 Developer ID 서명·Apple 공증이 아니므로 OS 보호 기능을 우회하지 않습니다.

무인 설치가 필요하면 다음 두 경로를 검토할 수 있습니다. **어느 경로도 설치 실행은 검증하지 않았습니다.**

### 1. macOS 릴리스 ZIP의 bundled installer

[Releases](https://github.com/arm092/autoharness-codex/releases)에서 아키텍처에 맞는 `AutoHarness-<ver>-macOS-<arch>.zip`과 대응 `-SHA256.txt`를 받고 SHA256을 대조한 뒤 **새 폴더**에 압축을 풉니다. 예를 들어 1.3.1 ZIP은 `distribution/Install AutoHarness.app/Contents/Resources/payload`를 포함합니다. 압축을 푼 폴더에서 payload를 지정하면 launcher와 같은 설치 경로를 GUI 없이 호출할 수 있습니다.

```sh
payload="$PWD/distribution/Install AutoHarness.app/Contents/Resources/payload"
"$payload/plugin/runtime/bin/python3" -I "$payload/plugin/scripts/macos_install.py" install --payload "$payload"
```

공식 launcher에서 `--gui`만 제외한 source 기반 절차입니다. Codex 자동 탐색이 실패하면 검토한 실행 파일을 `--codex <absolute-path>`로 지정하고, 별도 profile은 `--codex-home <path>`로 지정합니다. 기본 프로그램 경로는 `~/Library/Application Support/AutoHarness for Codex`입니다. 시스템 Python·Homebrew cask를 설치하는 경로가 아닙니다.

사용자는 2026-11-11 1.3.1 ZIP·checksum·launcher를 확인했다고 보고했습니다. 이번 문서 작업에서도 **arm64 ZIP의 SHA256과 내부 launcher·payload 경로만 정적 확인**했으며 설치기나 bundled runtime을 실행하지 않았습니다. x86_64 ZIP 내부는 별도 미확인입니다.

### 2. source/manual 등록

영구 보존할 새 폴더에 clone한 뒤 공식 README의 local marketplace 경로를 사용합니다.

```sh
git clone https://github.com/arm092/autoharness-codex
cd autoharness-codex
python3 scripts/entry.py doctor
codex plugin marketplace add .
codex plugin add autoharness-codex@autoharness-codex-local
```

위 명령은 설치 안내이며 이 문서 작업에서 실행하지 않았습니다. 설치 후 Codex를 다시 열고 `/hooks`에서 다섯 훅을 검토·신뢰합니다. 설치 자체가 hook trust를 부여하지 않습니다. installer판과 source판을 중복 등록하지 않습니다.

## Update

Homebrew cask나 자체 self-update 명령은 확인하지 못했습니다.

- **릴리스 설치형:** Codex를 종료하고 새 ZIP·checksum을 검증해 새 폴더에 풉니다. 위 bundled installer 또는 공식 GUI 설치기를 같은 profile·프로그램 경로에 실행하는 방식입니다. source상 이전 프로그램 release를 덮어쓰거나 삭제하지 않고 새 release 폴더를 만들며 지식 데이터도 보존합니다. 실제 업데이트·등록 성공은 미검증입니다.
- **source형:** 사용자 변경과 branch를 확인한 뒤 checkout에서 `git pull --ff-only origin master`로 갱신합니다. **2026-11-11 upstream 기본 branch는 `main`이 아니라 `master`**입니다. pull 뒤 Codex 캐시에 다시 반영하려면 재등록이 필요한지, 정확한 재등록 순서는 미확인입니다. pull만으로 활성 plugin이 갱신됐다고 단정하지 말고 등록 source·버전을 확인합니다.

두 방식 모두 Codex를 재시작하고 hook trust·등록 상태를 다시 확인합니다.

## Uninstall

- source/manual: `codex plugin remove autoharness-codex@autoharness-codex-local`로 해당 등록을 해제합니다.
- macOS 설치형: 공식 **Uninstall AutoHarness.app**로 소유 plugin·marketplace 등록을 해제합니다. 프로그램 release는 남으며 등록 해제 뒤 프로그램 폴더를 별도 정리할 수 있습니다.
- Windows 설치형: Windows 앱 설정의 AutoHarness 제거 기능을 사용합니다.

지식은 기본 `CODEX_HOME/autoharness-codex`(기본 profile이면 `~/.codex/autoharness-codex`) 또는 `AUTOHARNESS_CODEX_DATA`에 남습니다. 프로젝트별 scope·SQLite·revisions·증거·snapshot도 이 데이터 루트 아래에 보존됩니다. 저장소 식별은 linked worktree별로 다릅니다. 저장소 코드·AGENTS.md·기존 외부 스킬을 지우지 않습니다. 사용자 정의 경로를 먼저 확인하고 데이터 삭제는 별도로 승인받습니다.

## Verify

Codex plugin 목록에서 실제 source·버전을 확인하고 `/hooks`에서 다섯 훅의 등록·신뢰를 확인합니다. CLI doctor·저장된 인덱스 검사는 존재·환경 검증이며 실제 학습 성공과 다릅니다. 대표 학습 후 queued/proposed/applied/rejected 상태와 증거를 구분해야 합니다. 이번 작업에서는 설치·doctor·모델 호출을 실행하지 않았고 `unverified`를 유지합니다.

## Caveats

- child는 기본부터 `codex exec --ignore-user-config --ignore-rules --ephemeral --sandbox read-only`를 사용합니다. source `model.py:114–124`는 **hooks, plugins, apps, shell_tool, unified_exec, multi_agent, memories, browser_use, browser_use_external, computer_use, image_generation** 11개 기능을 `--disable`하고, `skip_host_skill_discovery`를 켜며 `web_search="disabled"`로 설정합니다. 별도의 worker 디렉터리에서 제안만 반환하고 적용은 검증 파이프라인이 담당합니다. 지원하지 않는 CLI에서 이 보호 플래그를 임의로 빼지 않습니다.
- 모델 기본값은 **Codex CLI default**이며 `AUTOHARNESS_CODEX_MODEL`로 지정할 수 있습니다. Claude Code판처럼 Haiku라고 가정하지 않습니다. 이 호출도 Codex 플랜을 소비합니다.
- reflection 기본 cadence는 완료된 **tool call 50회**(`AUTOHARNESS_CODEX_CADENCE`), 시간당 프로젝트별 시도 기본 **4회**(`AUTOHARNESS_CODEX_HOURLY_LIMIT`), scope별 UTC-day admission budget은 **200,000토큰**(`AUTOHARNESS_CODEX_DAILY_TOKENS`)입니다. 일일 예산은 사전 추정으로 호출을 허용하는 한도이지 provider 측 hard cap이나 과금 보장이 아닙니다.
- model 입력의 transcript는 untrusted data이며 redaction·증거 검증이 모든 누출·오판을 막지는 않습니다. 자동 retirement는 기본 OFF이고 데이터는 자동 hard-delete되지 않아 저장량이 늘 수 있습니다.

## Privacy & Updates

2026-11-11 **`f48cd10314c59918b33e5c74442e1d94cc98be53`**의 README·model carrier·macOS installer/build 경로와 `src/` 정적 검색을 확인했습니다. 자체 telemetry·버전 조회·자동 코드 교체 구현은 검색에서 찾지 못했지만 전체 감사나 런타임 무전송 증명은 아닙니다. 기본값·수신자·opt-out의 독립 정책은 미확인입니다.

정상 학습 기능은 선택된 transcript 기록·관련 스킬을 `codex exec`를 통해 Codex 모델 서비스로 보내며 플랜을 소비합니다. 실제 수신 경로는 호스트 인증·provider에 따릅니다. `AUTOHARNESS_CODEX_AUTO=0`은 자동 queueing을 끄는 설정이지 수동 학습·기존 작업·Codex 자체 통신을 모두 차단하는 설정은 아닙니다. 릴리스 다운로드·marketplace 등록 통신과 학습 통신, telemetry는 구분합니다. 코드 갱신은 Update의 수동 절차를 참고합니다.

## References

- [README · 고정 revision](https://github.com/arm092/autoharness-codex/blob/f48cd10314c59918b33e5c74442e1d94cc98be53/README.md)
- [child 격리·모델](https://github.com/arm092/autoharness-codex/blob/f48cd10314c59918b33e5c74442e1d94cc98be53/src/autoharness_codex/model.py#L114-L124)
- [macOS 설치·해제](https://github.com/arm092/autoharness-codex/blob/f48cd10314c59918b33e5c74442e1d94cc98be53/scripts/macos_install.py)
- [macOS launcher·패키징](https://github.com/arm092/autoharness-codex/blob/f48cd10314c59918b33e5c74442e1d94cc98be53/scripts/build_macos.py)
- [1.3.1 릴리스·checksum](https://github.com/arm092/autoharness-codex/releases/tag/v1.3.1)
- [Security](https://github.com/arm092/autoharness-codex/blob/f48cd10314c59918b33e5c74442e1d94cc98be53/SECURITY.md)
