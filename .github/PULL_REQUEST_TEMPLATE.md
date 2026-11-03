## What changes and why

Describe the problem and how this change helps the reader. Link a related issue if there is one.

## Source and meaning

Link the source sections, controls, or definitions affected. Explain whether this is an editorial clarification, a transcription correction, or a proposal to change the framework. For a proposal, state which obligations or scope boundaries would change.

## Validation

Describe the source comparison and checks you ran, including any limits. For documentation, run `python3 scripts/check-docs.py` and `git diff --check`. If you changed the checker, also run `python3 -m unittest discover -s scripts -p 'test_*.py'`.

## Review checklist

- [ ] The wording follows the editorial guide and preserves the intended meaning.
- [ ] Source links, control references, and navigation are correct.
- [ ] The changelog describes the change and its effect.
- [ ] The source coverage map reflects any changes to framework pages.
