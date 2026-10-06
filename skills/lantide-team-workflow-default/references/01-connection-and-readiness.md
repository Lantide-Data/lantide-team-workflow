# Connection and readiness

Use this procedure when Lantide is not yet connected, the connection state is unclear, the session is unbound, or work resumes after a restart or context loss.

## Choose the handoff

Try the existing MCP connection first unless the client explicitly reports that no Lantide connection is configured. A deep link is a Desktop UI handoff, not readiness evidence. Continue only after MCP initialization succeeds.

Use the smallest route that matches the user's situation:

- **First onboarding or an explicit request for a new connection:** open `lantidedata://agent-integration/pair?source=team-workflow`. Add an allowlisted `client=codex`, `client=claude`, `client=cursor`, or `client=other` only when the client identity is known.
- **Existing connection fails:** open `lantidedata://agent-integration`. This opens connection management without starting a replacement pairing flow. Do not infer from a transport error that a profile is expired, revoked, unexposed, or misconfigured, and do not create a replacement profile merely because initialization failed.
- **User only wants to open, return to, or inspect Lantide:** open `lantidedata://open`. Do not use the pairing route, because it would interrupt the current work with connection setup.

Opening any route may cold-launch Lantide or focus the existing Desktop window. It does not prove that Desktop, the backend, the listener, or the current MCP client is ready.

## Complete first onboarding safely

1. Open the generic pairing route with `source=team-workflow`.
2. If a supported local opener can identify Codex and Lantide should perform its GUI-confirmed config handoff, `client=codex&action=configure` may be used. Use `action=configure` only for Codex. Claude, Cursor, and other clients must use the generic pairing route without that action.
3. Tell the user that Lantide may open and may require legal consent plus confirmation of scope, Access Mode, expiry, and client setup. Wait for the user to complete or cancel those decisions; the skill does not approve them.
4. Prefer a client-specific secure configuration flow or the client's official MCP settings. Do not ask the user to paste a bearer credential or complete config into ordinary chat.
5. If the user elects to hand a one-time config to a trusted local Agent, use a secure secret or configuration input supplied by that runtime. Never repeat the credential in a reply, place it in command arguments, write it to the repository, or include it in ordinary logs or error messages. If no secure input exists, ask the user to install the config through the client's own settings instead.
6. If credential exposure is suspected, stop and direct the user to rotate or revoke the connection in Agent Integration.
7. After the user confirms setup, reload the MCP connection as the client supports. If the client requires a restart or a new session, do that instead of retrying an unchanged session. In a new session, reload this skill before continuing.
8. If the client supports live reload, retry initialization at most three times, waiting 2 seconds, 4 seconds, then 8 seconds. Do not poll before the user confirms completion, retry forever, or reopen the deep link on every failure.
9. If the user cancels pairing, stop. Do not reopen the deep link, create another profile, or claim that a connection exists.

## Handle protocol and surface limits

For a web-only Agent or any surface without local protocol-opening capability, provide a clickable deep link when supported or the manual fallback: open **Lantide Data → Agent Integration**. Do not claim that the app opened.

If an OS opener reports failure, do not scan arbitrary processes, ports, filesystems, app bundles, or the registry, and do not guess whether Lantide is missing, outdated, damaged, or blocked. Ask the user to confirm that the latest Desktop is installed from the official download path linked from the documentation hub, then use the manual fallback.

If the opener gives no result, say only that an open request was made and wait for user confirmation. Do not present the request as a successful launch.

## Establish context

1. Initialize the MCP connection and inspect its instructions and stable tool catalog. MCP initialization succeeds is the only connection-readiness proof.
2. Call `get_analysis_context` immediately after initialization.
3. If an All-workspaces connection is unbound, list available workspaces and select the intended workspace. Confirm ambiguous choices with the user. Do not create a workspace merely to imitate switching to an existing one.
4. Use the analysis context returned by workspace selection when present; do not re-list tools unless live guidance explicitly requires it.
5. Confirm connection scope, access mode, selected workspace, focused project, artifact state, and recommended next actions.
6. If `methodology.playbook.must_read` is true, read `lantide://external_agent_playbook`.
7. Load the runtime skills whose context entry has `next_action=load_skill` when relevant to the task.

## Recovery

After reconnect, app restart, workspace switch, new Agent session, or context compression, call `get_analysis_context` again. When continuing formal work, read the named Plan or Report and its current evidence state rather than reconstructing identifiers or facts from chat memory.

After the bounded retries fail, stop and report the MCP-client-visible error. Do not repeatedly relaunch Desktop or infer hidden profile state. Use `lantidedata://agent-integration` once for user-led recovery when appropriate, then follow the client reload rules above.

## Ready state

The connection is ready only when:

- MCP initialization succeeded;
- scope and access mode are known;
- a workspace is selected when required;
- the intended project or absence of one is explicit;
- live Playbook and runtime-skill requirements are satisfied;
- no credential was exposed in chat, command arguments, logs, or repository files.
