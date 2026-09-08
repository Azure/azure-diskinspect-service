# Windows Guest Analyzer Gap Closure for Mini Diagnostic

`diagnostic-wga-gap-closure` is a targeted add-on for `min-diagnostic`. It adds the artifacts needed by known Windows Guest Analyzer coverage gaps found by comparing WGA rule dependencies against the Windows mini diagnostic manifest. Some extension rules depend on runtime path matching rather than a literal collected filename, so this module targets the needed artifact family rather than guaranteeing every rule can be proven by filename alone.

| Manifest | Area | Description | PII Risk |
|----------|------|-------------|----------|
| `diagnostic-wga-gap-closure` | WGA | Targeted add-on for known min-diagnostic WGA gaps | Medium |
