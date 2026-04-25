# Self-register on package import.
#
# cognee discovers adapters via runtime mutation of a `supported_databases`
# dict (no entry-point mechanism). The registration calls live in
# `register.py` as module-level side-effects: `use_vector_adapter("falkor", ...)`,
# `use_graph_adapter("falkor", ...)`, and the dataset-database-handler hooks.
#
# Without this re-export, `import cognee_community_hybrid_adapter_falkor` is
# a no-op (because __init__.py is empty), and any subsequent `cognee.add(...)`
# fails with `OSError: Unsupported vector database provider: falkor` even
# though the package is installed. The user has to know to explicitly
# `import cognee_community_hybrid_adapter_falkor.register` — surprising and
# undocumented behavior that breaks every usage path that doesn't read the
# adapter's source.
#
# Importing register here makes the package self-registering: any code that
# touches the package name fires the adapter wiring.
from . import register  # noqa: F401 — side-effect import (registration)
