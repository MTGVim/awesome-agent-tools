# Claude Show Your Work

- **Status:** Archived
- **Reason:** `low-value`
- **Archived on:** 2026-11-11
- **Upstream:** https://github.com/iamumeransari/claude-show-your-work

## Why archived

2026-11-11 기준 개인 사용 기록에서 923개 세션 중 22개 세션에 걸쳐 69회 사용했습니다. 대부분 정적 이미지였고, 미리보기 화질이 낮아 원본을 다시 열어야 했습니다. 데일리 셋업에서 제외하고 현재 추천 목록에서도 보관합니다. 이는 개인 사용 평가이며 업스트림 전체에 대한 결함 판정이 아닙니다.

## Historical guide

아래는 보관 당시의 가이드입니다. 설치·업데이트 명령은 현재 절차로 간주하지 말고 업스트림 문서를 확인합니다.

<!-- catalog: {"name": "Claude Show Your Work", "upstream": "https://github.com/iamumeransari/claude-show-your-work", "types": ["plugin"], "agents": ["Claude Code"], "category": "browser", "verification": "metadata", "install_mode": "agent-guide", "last_reviewed": "2026-11-03"} -->

> 미디어 재생 및 테스트 전후 비교

- **Upstream:** https://github.com/iamumeransari/claude-show-your-work
- **Types:** plugin
- **Agents:** Claude Code
- **Verification:** metadata
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-03

## Why use it?

Claude Code 대화 안에서 이미지와 동영상을 미리 보고, Playwright의 수정 전후 결과를 시각적으로 비교하도록 돕습니다.

## Requirements

Claude Code 2.1.286+, macOS 또는 Linux, kitty 그래픽 프로토콜을 사용하는 Ghostty·kitty 등이 필요합니다. 영상 기능은 ffmpeg가 필요합니다.

## Install

```text
/plugin marketplace add https://github.com/iamumeransari/claude-show-your-work.git#releases
/plugin install show-your-work@iamumeransari
```

## Update

공식 release 브랜치 마켓플레이스를 갱신하고 플러그인을 다시 로드합니다.

## Uninstall

`claude plugin uninstall show-your-work@iamumeransari` 후 임시 미디어 파일 유지 여부를 확인합니다.

## Verify

이미지 삽입과 Playwright QA 녹화 미리보기를 점검합니다.

## Privacy & Updates

- **Network and telemetry:** The upstream [privacy document](https://github.com/iamumeransari/claude-show-your-work/blob/main/PRIVACY.md) says the plugin checks its version on `raw.githubusercontent.com` at most once per day and can send anonymous usage counts to PostHog (`us.i.posthog.com`) when usage sharing is enabled. This does not establish that other plugins collect no data.
- **Opt out of usage statistics:** Run `/show-your-work` and choose **Don't share**, or set `SHOW_YOUR_WORK_TELEMETRY=0` before starting Claude Code. The in-app opt-out may send one final opt-out event, according to upstream. `DO_NOT_TRACK=1` is another supported option.
- **Disable self-update/version checks:** Set `SHOW_YOUR_WORK_AUTO_UPDATE=0` in the Claude Code process environment. Keep plugin updates under your chosen marketplace process instead. Upstream notes that the self-updater is expected to be retired when hosting moves to the regular plugin directory.
- **Renderer compatibility and ordering:** Show Your Work and Prismantis are not known to be mutually exclusive at installation. Both can be installed, but enabling multiple global renderers may cause output interception conflicts. When using them together, first place Show Your Work **before** Prismantis in `enabledPlugins`, restart Claude Code, and test both renderers. This ordering is an environment-specific workaround, not a universally verified fix. Do not conclude that installation or coexistence is impossible solely from an output conflict; check installation state, load order, and actual rendering first.

## Caveats

### 텔레메트리와 네트워크 (2026-11-04 문서 확인)

사용 통계 공유는 설정으로 선택하며 PostHog에 전송됩니다. `SHOW_YOUR_WORK_TELEMETRY=0` 또는 `DO_NOT_TRACK=1`로 중단할 수 있습니다. 별도의 하루 1회 자체 버전 확인은 `SHOW_YOUR_WORK_AUTO_UPDATE=0`으로 끕니다. [Privacy](https://github.com/iamumeransari/claude-show-your-work/blob/main/PRIVACY.md)

상태 비교: [Privacy, Telemetry & Updates](../../docs/privacy-and-updates.md). 실제 설치된 버전의 설정을 다시 확인합니다.

### 개인 셋업 메모 (2026-11-03)

Prismantis·Skins 등 전역 렌더러와 동시 활성화할 때 출력 충돌이 발생할 수 있습니다. 이것이 설치 자체가 불가능하다는 의미는 아닙니다. Prismantis와 함께 사용한다면 위의 **Renderer compatibility and ordering** 안내에 따라 로드 순서를 조정하고 실제 출력을 검증합니다. Kitty 그래픽 프로토콜을 지원하는 터미널이 필요하고 영상 재생에는 ffmpeg가 필요합니다. Claude Code 2.1.317에서 Take a tour 버튼 대신 `/show-your-work tour`를 사용했습니다. 자체 업데이트와 통계 전송은 선택적으로 `SHOW_YOUR_WORK_AUTO_UPDATE=0`, `SHOW_YOUR_WORK_TELEMETRY=0`으로 끌 수 있습니다.

터미널 그래픽 지원 및 ffmpeg 설치 여부에 따라 기능이 달라집니다. 시연 자료가 실제 테스트를 대체하지는 않습니다.

## References

- [Upstream](https://github.com/iamumeransari/claude-show-your-work)
