---
name: prefer-minimal-infra
description: "User wants infra/deploy work (Docker, Airflow) kept as simple as possible"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 0b6ca1a1-8865-4765-bd71-2a383c535b8d
  modified: 2026-10-10T13:17:22.491Z
---

For containerisation, DAGs and deployment, propose the minimal setup first (single Dockerfile, single-container compose, one-task DAG), not production-grade stacks with many services, params and future-proofing.

**Why:** User rejected a plan with postgres + multi-service Airflow, DAG params and ECS/S3 seams: "i want the containerization to be as simple as possible, simple dag, deploy and stuff".

**How to apply:** Start with the smallest working version; mention future steps (ECS, S3) in a line, don't design for them.
