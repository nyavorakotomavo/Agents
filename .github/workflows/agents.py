name: Autonomous Agents

on:
  workflow_dispatch:
    inputs:
      objective:
        description: "Objectif des agents"
        required: true
        default: "Trouver une idée révolutionnaire de site ou application"
  schedule:
    - cron: "0 18 * * *"

jobs:
  run-agents:
    runs-on: ubuntu-latest
    timeout-minutes: 350

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
          cache: "pip"

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run Autonomous Agents
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
          MODEL: ${{ vars.MODEL }}
          OBJECTIVE: ${{ inputs.objective }}
        run: python main.py

      - name: Save results
        uses: actions/upload-artifact@v4
        with:
          name: agent-results
          path: outputs/
          if-no-files-found: ignore