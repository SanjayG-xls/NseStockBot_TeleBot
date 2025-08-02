---
name: "\U0001F914 Question or Support \U0001F914"
about: Share your questions here ! dont be shy :>
title: ''
labels: ''
assignees: ''

---

name: Question
description: Ask a question or request clarification
title: "[QUESTION] <your question>"
labels: [question]
assignees: []

body:
  - type: input
    id: topic
    attributes:
      label: Topic
      description: What's your question about?
      placeholder: "Telegram bot / NSE fetch / yfinance..."
    validations:
      required: true

  - type: textarea
    id: question
    attributes:
      label: Ask your question
      description: Provide as much context as possible.
      placeholder: "How do I set up API keys?"
