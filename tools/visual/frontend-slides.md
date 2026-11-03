# Frontend Slides

<!-- catalog: {"name": "Frontend Slides", "upstream": "https://github.com/zarazhangrui/frontend-slides", "types": ["skill", "tool"], "agents": ["Claude Code"], "category": "visual", "verification": "trial", "install_mode": "agent-guide", "last_reviewed": "2026-11-03"} -->

> 프론트엔드 슬라이드 제작 도구

- **Upstream:** https://github.com/zarazhangrui/frontend-slides
- **Types:** skill/tool
- **Agents:** Claude Code (plugin); other agents can read SKILL.md manually, behavior not validated
- **Verification:** trial
- **Install mode:** agent-guide
- **Last reviewed:** 2026-11-03

## Why use it?

에이전트와 대화해 디자인 스타일을 비교하고 HTML 슬라이드를 만들며, 기존 PowerPoint의 콘텐츠·이미지를 웹 프레젠테이션으로 변환합니다.

## Requirements

Claude Code에는 플러그인으로 배포됩니다. 다른 에이전트도 SKILL.md와 보조 파일을 읽을 수 있지만 전체 기능 검증은 별도입니다. 완성 산출물은 HTML 기반입니다.

## Install

Claude Code에서는 원본 README의 마켓플레이스 경로로 설치합니다.

```text
/plugin marketplace add https://github.com/zarazhangrui/frontend-slides
/plugin install frontend-slides@frontend-slides
```

다른 에이전트에는 SKILL.md와 참조 파일을 해당 스킬 위치에 복사하도록 안내합니다.

## Update

원본 파일과 기존에 수정한 프리셋 및 템플릿을 비교해 업데이트합니다. 생성한 슬라이드는 별도 파일로 보관합니다.

## Uninstall

설치한 스킬·플러그인만 제거합니다. 이미 생성한 HTML 발표자료나 변환 콘텐츠는 삭제하지 않습니다.

## Verify

시각적 스타일 선택을 포함한 짧은 슬라이드를 생성하고 브라우저에서 레이아웃과 키보드 이동을 확인합니다.

## Caveats

PPT 가져오기 시 원본 애니메이션이나 레이아웃을 완전하게 재현한다고 가정하면 안 됩니다. 생성된 콘텐츠의 접근성과 화면 크기를 검증합니다.

## References

- [Upstream](https://github.com/zarazhangrui/frontend-slides)
