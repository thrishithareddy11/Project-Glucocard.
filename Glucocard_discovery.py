import pubchempy as pcp

def evaluate_molecule(name):
    try:
        print(f"\n[SCANNING] Fetching data for {name}...")
        results = pcp.get_compounds(name, 'name')
        if not results:
            print(f" {name} not found.")
            return

        compound = results[0]
        mw = float(compound.molecular_weight)
        donors = int(compound.h_bond_donor_count or 0)
        acceptors = int(compound.h_bond_acceptor_count or 0)
        smiles = compound.canonical_smiles

        score = 0
        if mw < 500: score += 1
        if donors <= 5: score += 1
        if acceptors <= 10: score += 1

        status = {3: "EXCELLENT", 2: "GOOD", 1: "POOR", 0: "REJECTED"}[score]

        print(f" RESULTS FOR {name.upper()}")
        print(f" MW: {mw} Da | SMILES: {smiles}")
        print(f" SCORE: {score}/3 | STATUS: {status}")
        print("-" * 55)

    except Exception as e:
        print(f"Error: {e}")

# REPLACEMENT FOR THE MAIN BLOCK
print("=" * 60)
print("🧬 PROJECT GLUCOCARD: MULTI-TARGET DISCOVERY ENGINE")
print("=" * 60)

molecules = ["Berberine", "Acarbose", "Cinnamaldehyde"]
for molecule in molecules:
    evaluate_molecule(molecule)

print("\n[FINISH] Discovery Phase Complete.")
