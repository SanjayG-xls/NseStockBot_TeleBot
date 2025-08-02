---
name: "\U0001F41B Bug Report \U0001F41B"
about: Share freely about any bugs related to codes
title: ''
labels: ''
assignees: ''

---

name: Bug report
description: Report a bug with the stock bot
title: "[BUG] <describe issue>"
labels: [bug]
assignees: []

body:
  - type: markdown
    attributes:
      value: |
        Thanks for reporting! Please provide as much detail as possible.

  - type: textarea
    id: what-happened
    attributes:
      label: What happened?
      description: Describe the bug, steps to reproduce, and what you expected.
      placeholder: "It crashed when I typed..."
    validations:
      required: true

  - type: textarea
    id: logs
    attributes:
      label: Logs or screenshots
      description: Paste logs or upload images that help explain the issue.
      placeholder: "Paste logs or attach screenshots here."
