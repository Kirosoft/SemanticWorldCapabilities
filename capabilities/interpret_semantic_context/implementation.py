"""Conservative lexical interpretation over explicit, HG-validated context."""


def interpret_semantic_context(request):
    context = request["context"]
    material = request["material"]
    if context.get("modifier"):
        return {"interpretation": {"unresolved": {"reason": (
            "This implementation cannot establish modifier applicability.",)}}}
    if "lexical" not in material:
        return {"interpretation": {"unresolved": {"reason": (
            "Semantic-subject interpretation requires additional World evidence.",)}}}
    text = material["lexical"]["text"].strip()
    references = frozenset(text.split())
    matches = tuple(reference for reference in sorted(context.get("declaration", ()))
                    if reference in references or text == reference.rsplit("/", 1)[-1])
    if not matches:
        return {"interpretation": {"unresolved": {"reason": (
            "No exact declaration reference or leaf name matches in the supplied context.",)}}}
    return {"interpretation": {"hypotheses": {"hypothesis": tuple(
        {"candidate": reference, "confidence": "1" if reference in references else "0.5",
         "evidence": ("Exact lexical match in explicitly supplied declaration context; proposal only.",)}
        for reference in matches)}}}
