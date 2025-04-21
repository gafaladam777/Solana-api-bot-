services:
  - type: web
    name: solana-api-bot
    env: python
    buildCommand: ""
    startCommand: python main.py
    plan: free
    branch: main
    autoDeploy: true
