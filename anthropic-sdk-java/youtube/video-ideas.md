# Claude SDK for Java Video Ideas

## Candidate 1 — Cross-language linting for Kotlin-to-Java contracts
- Source: `anthropic-java-detekt-rules/README.md`
- Topic: Encoding cross-language API contracts in static analysis
- Hook: You write idiomatic Kotlin, but Java callers see confusing signatures. Built-in linters reason about Kotlin idioms or Java interop, but not both.
- Key case: A public Kotlin method returns a sealed class (idiomatic Kotlin for exhaustive pattern matching), but Java callers see an abstract base with multiple subclasses and can't pattern-match. A custom detekt rule flags this violation.
- The Question: Why can't built-in detekt rules express constraints across the Kotlin-source / Java-caller boundary?
- Core idea: Custom `RuleSetProvider` that knows about the Kotlin-source / Java-caller boundary and enforces cross-language idioms (e.g., "public sealed classes break Java interop" or "builder chains must be method-reference compatible").
- Visual object: Detekt baseline file showing per-module violations grouped by rule ID.
- Manim move: scan
- Example seed: A `PaymentBuilder` interface with fluent methods (`paymentBuilder().amount(100).currency("USD")`). A custom rule ensures all chained methods return `this` or a builder type, not a union type that Java can't express.
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: Kotlin, detekt, Java interop
- Exclusions: AST traversal details, release-please CI automation, ktfmt formatting rules
- Score: 9/10

## Candidate 2 — Daemon threads and JVM shutdown semantics
- Source: `CHANGELOG.md` (v2.44.1)
- Topic: Threading lifecycle and when threads block JVM termination
- Hook: Bedrock client hangs after `close()`, even though the background thread pool stopped. Why does a stopped background thread block the entire JVM from exiting?
- Key case: SSE transcoding uses a non-daemon thread pool for message polling. On `close()`, the pool shuts down, but the JVM waits for non-daemon threads to finish; the poll thread is still alive, blocking exit.
- The Question: Why do some threads prevent JVM termination while others are cleanly reaped?
- Core idea: Non-daemon threads block JVM termination even if idle; daemon threads are reaped on shutdown. Background worker pools should use daemon threads unless they're critical to application lifecycle.
- Visual object: Thread lifecycle diagram showing non-daemon thread blocking shutdown vs. daemon thread being reaped.
- Manim move: decay
- Example seed: A background polling thread checking for messages. If non-daemon, `System.exit()` waits for the poll loop to finish. If daemon, it's reaped immediately.
- Length band: 2–3 min
- Still lanes: raster
- Prerequisites: Java threading, client lifecycle
- Exclusions: OkHttp internals, Bedrock-specific API design, SSE protocol details
- Score: 9/10

## Candidate 3 — Java backward-compat testing with conditional local skip
- Source: `CONTRIBUTING.md`
- Topic: Balancing developer friction with strict CI enforcement
- Hook: The SDK supports Java 8, but developers run Java 11 locally. Local tests pass, CI fails. How do you enforce Java 8 compat without forcing every dev to install two JDKs?
- Key case: Developer runs `./gradlew test` on Java 11; ecosystem tests are skipped (no JDK 8 available). A PR introduces a Java 9 API call in a silent code path. CI's Java 8 check fails, blocking the merge.
- The Question: How do you make CI stricter than the local environment without constantly breaking local builds?
- Core idea: Gradle toolchain API allows task-level JDK selection. Local builds skip Java 8 tests if absent (graceful degradation). CI always installs JDK 8 and fails if any test is skipped, enforcing the contract at publish time.
- Visual object: Build output showing "Skipped: ecosystem test (JDK 8 unavailable)" locally vs. "FAILED: ecosystem test" in CI.
- Manim move: split
- Example seed: A build that checks `maxSupport(Java.VERSION_8)` locally (skipped on Java 11) but runs on JDK 8 in CI (enforced).
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: Gradle, Java version compatibility, CI/CD
- Exclusions: Gradle plugin ecosystems (shadow, shade), Java ecosystem test module implementation, release automation
- Score: 8/10

## Candidate 04 — Skill files split instruction from knowledge so only one changes at a time
- Source: `anthropic-java-example/src/main/resources/greeting-SKILL.md`
- Topic: Separating AI behavior instructions from reference knowledge for independent evolution
- Hook: You want Claude to stay current with changing data (a pricing table, a product list) without re-engineering the instruction that uses it. A single combined system prompt makes instruction and knowledge a single atomic unit — both change together or neither does.
- Key case: The `greeting` skill injects a YAML-frontmatter markdown file as the instruction, paired with a separate `greeting-reference.md` that lists the actual greetings. Updating the reference swaps the vocabulary without touching the instruction logic. The model still follows the same rule ("greet nautically") but draws from updated examples.
- The Question: A single combined system prompt should produce identical output to a split skill+reference pair; this case splits them anyway. Why does the split matter if the concatenated context is the same?
- Core idea: Separating the instruction (stable contract) from the reference (live knowledge feed) means different roles own different files — a prompt engineer owns the skill; a content editor owns the reference. Combining them couples two change rates into one file, creating merge conflicts and versioning confusion at scale.
- Visual object: Two markdown files with arrows flowing into labeled segments of a context window — one segment highlighted as "instruction," one as "knowledge."
- Manim move: split
- Example seed: A `pricing` skill (instruction: "quote prices in USD, never negotiate") referencing a `pricing-table.md` (a 3-row table: Basic $9, Pro $29, Enterprise $99). When Enterprise bumps to $149, only the table file changes; the instruction is untouched. [illustrative]
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: Claude API basics, system prompts
- Exclusions: Managed Agents webhook events, vault credential injection, skill versioning APIs, SDK loading internals
- Score: 8/10

## Candidate 05 — Pinning a version doesn't pin the graph: Gradle lockfiles in strict mode
- Source: `CONTRIBUTING.md`
- Topic: Why direct-dependency pinning doesn't guarantee reproducible builds and how lockfiles fix it
- Hook: You wrote `anthropic-java:2.48.0` in your build file. Your colleague gets a different `jackson-databind` version than you do. Both builds succeed, but one has a subtle behavioral difference introduced by the transitive upgrade.
- Key case: The SDK adds `implementation("com.fasterxml.jackson.databind:2.15.0")`. A pre-existing transitive dep already declares `2.15.2+`. Gradle's conflict resolution silently picks `2.15.2`. Without a lockfile, this version can change again the next time any dep in the graph is updated. `CONTRIBUTING.md` requires all modules (including `buildSrc`) to commit `gradle.lockfile`; strict mode fails the build if any configuration resolves to a version not in the lockfile.
- The Question: Pinning `jackson-databind:2.15.0` should guarantee that version is used; this project uses `./scripts/lock` to regenerate a separate lockfile anyway. Why isn't the version constraint enough?
- Core idea: A version constraint expresses a minimum or range, not an exact resolved value. Gradle's conflict resolution algorithm picks a winner from all competing constraints in the full graph — the winner can change whenever any dependency in the graph is added or bumped. A lockfile records the actual resolved winner for every coordinate; strict mode makes any deviation a build failure, turning "best-effort reproducibility" into a hard guarantee.
- Visual object: A `gradle.lockfile` excerpt showing three coordinates, each pinned to an exact version — contrasted with the `libs.versions.toml` line that only declares a range.
- Manim move: accumulate
- Example seed: Module A needs `jackson:2.14`, module B needs `jackson:2.15+`. Without a lockfile, adding module B silently upgrades the resolved version across the build. The lockfile forces an explicit `./scripts/lock` regeneration before the build accepts the change. [illustrative]
- Length band: 2–3 min
- Still lanes: c2v
- Prerequisites: Gradle dependency management, semantic versioning
- Exclusions: `buildSrc` compilation order details, version catalog (TOML) syntax, Gradle config-cache interactions, publishing pipeline
- Score: 7/10
