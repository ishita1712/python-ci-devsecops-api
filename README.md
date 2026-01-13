# python-ci-devsecops-api

FastAPI DevSecOps CI Pipeline
Overview

This project demonstrates a production-style CI pipeline for a containerized FastAPI service, focusing on security-first automation, deployment simulation, and environment awareness.

The pipeline validates that the application is:
Secure (no high/critical vulnerabilities)
Runnable (container starts successfully)
Correctly configured per environment

Architecture
Developer Push
      ↓
GitHub Actions CI
      ↓
Docker Image Build
      ↓
Trivy Security Scan (fail-fast)
      ↓
Container Run (dev environment)
      ↓
Health Check (/health)
      ↓
Cleanup

Tech Stack

FastAPI – Python web framework
Docker – Containerization
GitHub Actions – CI automation
Trivy – Container vulnerability scanning

CI Pipeline Stages

1. Build
Builds Docker image using python:3.11-slim

2. Security Scan (DevSecOps)
Scans image with Trivy
Pipeline fails on HIGH or CRITICAL CVEs

3. Deployment Simulation
Runs container in CI
Injects environment variables
Executes runtime health check

4. Cleanup
Ensures containers are removed even on failure
