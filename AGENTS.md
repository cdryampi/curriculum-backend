# AGENTS.md

## Project scope

This directory contains the Django / Django REST Framework backend for the CV project. Agents working in this repository must only modify files inside `backend/` (specifically `curriculum-backend/` in this repository) unless the user explicitly requests otherwise.

## Development rules

- Do not modify `frontend/` (specifically `curriculum-frontend/`) files.
- Keep changes focused and minimal.
- Prefer small, reviewable pull requests.
- Do not commit secrets, tokens, API keys, credentials, database dumps, local `.env` values, or generated private files.
- Do not change public API behavior unless the task explicitly requires it.
- Do not perform broad refactors unrelated to the task.
- Follow the existing Django app structure and naming conventions.
- Add tests for security-sensitive behavior.
- Run the backend test/check commands before opening a PR when possible.

## Django / DRF conventions

- Keep authentication and permission logic explicit.
- Use serializers to whitelist editable fields.
- Never trust client-provided ownership fields such as `user`, `profile`, or `user_profile`.
- Scope querysets by the authenticated user when exposing private resources.
- Return 404 for resources outside the authenticated user's scope.
- Keep OpenAPI schemas accurate and stable when adding API endpoints.

## GPT Actions integration conventions

- GPT Actions endpoints must live under `/gpt-actions/`.
- GPT Actions endpoints must require authentication.
- GPT Actions endpoints must accept `Authorization: Bearer <token>`.
- GPT Actions serializers must expose only fields that ChatGPT is allowed to edit.
- GPT Actions endpoints must not expose media upload fields, admin-only fields, authentication endpoints, comments, contact/email endpoints, or unrelated app data.
- Use clear and stable OpenAPI `operationId` values.
