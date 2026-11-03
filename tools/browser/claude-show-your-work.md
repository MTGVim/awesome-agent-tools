# Claude Show Your Work

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

## Caveats

터미널 그래픽 지원 및 ffmpeg 설치 여부에 따라 기능이 달라집니다. 시연 자료가 실제 테스트를 대체하지는 않습니다.

## References

- [Upstream](https://github.com/iamumeransari/claude-show-your-work)
