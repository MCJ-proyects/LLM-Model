context = "El gato se sentó sobre el"
candidate_probabilities = {"sofá": 0.14, "árbol": 0.10, "coche": 0.20, "tejado": 0.30, "PC": 0.26}

print(f"Context: {context}\n")

for candidate, score in candidate_probabilities.items():
    print(f"{candidate}: {score:.1%}")

print(f"\nTotal: {sum(candidate_probabilities.values()):.1%}")
