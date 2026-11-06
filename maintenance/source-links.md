# Source link restoration

The internal source directory is ignored and no longer tracked. Local copies may remain. Earlier Git history still contains the source; this change does not rewrite history.

[Removed source links](removed-source-links.json) records every removed link outside the withdrawn directory, including its original Markdown, destination, label, file, line, column, and surrounding line. Locations refer to the baseline commit recorded in that file; use the context and label to locate links after later edits. Links inside the local source files are unchanged.

When public AAF 1.0 is available:

1. Confirm the approved source and publication terms before adding it to version control.
2. Review each recorded claim and destination against 1.0; do not assume draft anchors or controls remain valid.
3. Restore citations at their recorded contexts and update the coverage map, authoring guidance, and repository navigation.
4. Restore source fidelity validation and run documentation checks in a fresh checkout.

The inventory stores inactive strings, not navigable source links. Existing framework requirements and definitions have not been rewritten by this withdrawal.
