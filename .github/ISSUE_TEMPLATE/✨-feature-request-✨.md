---
name: "✨ Feature Request ✨"
about: Did you try any workarounds or different approaches? Mention them here.
title: ''
labels: ''
assignees: ''

---

name: Feature request
description: Suggest a new idea or improvement
title: "[FEATURE] <brief title>"
labels: [enhancement]
assignees: []

body:
  - type: markdown
    attributes:
      value: |
        Want something new? Let's discuss it!

  - type: textarea
    id: feature
    attributes:
      label: What’s the feature?
      description: Describe the feature you'd like to see added.
      placeholder: "I’d like to get Telegram alerts for intraday breakout stocks..."
    validations:
      required: true

  - type: textarea
    id: benefits
    attributes:
      label: Why is it useful?
      description: Explain how this would help users or improve the project.
      placeholder: "It helps users act on signals faster..."
