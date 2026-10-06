# Connection and readiness

Use this procedure when Lantide is not yet connected, the connection state is unclear, the session is unbound, or work resumes after a restart or context loss.

## Connect safely

1. Confirm that Lantide Data Desktop is installed and running. If it is not installed, use the official download path linked from the documentation hub.
2. Ask the user to create or expose a connection through **Agent Integration** in Lantide. Never invent a URL, recover a bearer credential, or ask the user to paste a secret into chat.
3. Use the team's approved connection profile when one exists. If no profile policy is defined, let the user choose scope and access mode in Lantide rather than treating this skill as authorization.
4. Initialize the MCP connection and inspect its instructions and stable tool catalog.

## Establish context

1. Call `get_analysis_context`.
2. If an All-workspaces connection is unbound, list available workspaces and select the intended workspace. Confirm ambiguous choices with the user. Do not create a workspace merely to imitate switching to an existing one.
3. Use the analysis context returned by workspace selection when present; do not re-list tools unless live guidance explicitly requires it.
4. Confirm connection scope, access mode, selected workspace, focused project, artifact state, and recommended next actions.
5. If `methodology.playbook.must_read` is true, read `lantide://external_agent_playbook`.
6. Load the runtime skills whose context entry has `next_action=load_skill` when relevant to the task.

## Recovery

After reconnect, app restart, workspace switch, or context compression, call `get_analysis_context` again. When continuing formal work, read the named Plan or Report and its current evidence state rather than reconstructing identifiers or facts from chat memory.

## Ready state

The connection is ready only when:

- initialization succeeded;
- scope and access mode are known;
- a workspace is selected when required;
- the intended project or absence of one is explicit;
- live Playbook and runtime-skill requirements are satisfied;
- no credential was exposed in chat, logs, or repository files.
