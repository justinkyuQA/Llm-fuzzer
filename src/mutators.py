import random
import base64
import re

def mutate_case(prompt: str) -> str:
"""Randomly flips case of characters."""
return "".join(
c.upper() if random.random() > 0.5 else c.lower()
for c in prompt
)

def mutate_spacing(prompt: str) -> str:
"""Normalizes weird spacing."""
return " ".join(prompt.split())

def mutate_repetition(prompt: str) -> str:
"""Repeats prompt (stress test / duplication fuzzing)."""
return f"{prompt} {prompt}"

def mutate_punctuation(prompt: str) -> str:
"""Injects random punctuation noise."""
noise = random.choice(["!!!", "...", "???", "!!!???", "...."])
return f"{prompt} {noise}"

def mutate_base64(prompt: str) -> str:
"""Encodes prompt in base64 wrapper (common obfuscation vector)."""
encoded = base64.b64encode(prompt.encode()).decode()
return f"[b64]{encoded}[/b64]"

def mutate_unicode(prompt: str) -> str:
"""Simple unicode obfuscation (basic character substitution)."""
return prompt.replace("a", "а").replace("e", "е").replace("i", "і")

MUTATORS = [
mutate_case,
mutate_spacing,
mutate_repetition,
mutate_punctuation,
mutate_base64,
mutate_unicode,
]

def generate_variants(prompt: str, n: int = 5):
"""Generate n mutated versions of a seed prompt."""
return [
random.choice(MUTATORS)(prompt)
for _ in range(n)
]
