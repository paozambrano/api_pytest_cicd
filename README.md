# api_pytest_cicd
# 🚀 GitHub API Testing Framework with Pytest & CI/CD

## 🎯 Project Overview
* **Objective:** Professional API testing framework using Pytest, focusing on security and automated execution.
* **API:** GitHub REST API v3.
* **Key Learning:** Handling Bearer Token authentication and managing API Rate Limits (429 errors).

## 🛠️ Tech Stack
* **Language:** Python 3.13
* **Testing Framework:** Pytest
* **Libraries:** `requests` (API calls), `python-dotenv` (Security), `pytest-html` (Reporting).
* **CI/CD:** GitHub Actions.

## 🛡️ Security Features
* **Environment Variables:** Used a `.env` file to prevent leaking sensitive Personal Access Tokens (PAT).
* **GitHub Secrets:** Configured repository secrets to securely inject tokens into the CI/CD pipeline.

## 🧪 Implemented Tests
1. **User Authentication:** Validates that the token correctly identifies the user (`/user`).
2. **Repository Discovery:** Verifies the ability to list private/public repositories with data validation.
