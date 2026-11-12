"""Morphism library of the manuscript package: text morphisms, admitted from their signatures.

No morphism here knows about a Manuscript, a binding, or how a collection is reached. Nothing in this
package carries a mapping strategy; LIFT-002 asks the Computer to derive one, with the same machinery
that derived the accounting lifts, over a domain with no Quantity, no Ratio and no sequence.
"""
import re

from semanticworld.swi.library import realiser

TITLE, SLUG, KEY = "property/label/chaptertitle", "property/identifier/slug", "property/identifier/manuscriptkey"
NOTE, TAG = "property/label/annotation", "property/identifier/tag"


@realiser("node/capability/slugify")
def slugify(chaptertitle: "property/label/chaptertitle"):
    """Morphism: a chapter title to its URL-safe slug."""
    return re.sub(r"[^a-z0-9]+", "-", chaptertitle.lower()).strip("-")


@realiser("node/capability/assemblekey")
def assemble_key(slug: "property/identifier/slug"):
    """Morphism: one or more slugs to the manuscript key. Declared over a collection; order-free."""
    return "+".join(sorted(slug))


@realiser("node/capability/keyword")
def keyword(annotation: "property/label/annotation"):
    """Morphism: an editorial note to its leading keyword."""
    return re.sub(r"[^a-z]", "", annotation.split()[0].lower())
