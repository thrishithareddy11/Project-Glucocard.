# Project-Glucocard🧬
●**Automated In-Silico Pipeline for Natural Alpha-Glucosidase Inhibitor Discovery**

## 📍Overview
Glucocard is a computational drug discovery framework developed to identify natural alternatives for Type 2 Diabetes management. The project integrates Python-based chemical screening with structural bioinformatics to evaluate the efficacy of Berberine against the human **3W37** enzyme.

## ~ Pipeline Workflow
1. **Data Acquisition:** Automated retrieval of chemical data via the `PubChemPy` API.
2. **Lipinski Screening:** Evaluating drug-likeness (MW, H-bond donors/acceptors).
3. **Bioavailability:** Utilizing the **BOILED-Egg model** for GI absorption prediction.
4. **Docking Analysis:** Comparative binding affinity analysis (Berberine vs. Acarbose).

## 🌐 Key Findings
| Molecule | Binding Energy (ΔG) | Status |
| **Berberine** | **-8.4 kcal/mol** | **Potent Inhibitor** |
| **Acarbose** | **-6.2 kcal/mol** | Standard Drug |

## 📝 Project Results

### **Summary of Analysis**
The automated pipeline successfully screened potential inhibitors for Alpha-glucosidase. The lead candidate, **Berberine**, demonstrated superior drug-likeness compared to traditional controls.
[Click here to view the raw execution output](./output.log.txt)

**Final Data Points:**
* **Target Protein:** 3W37 (Alpha-glucosidase)
* **Lead Molecule:** Berberine
* **Best Binding Score:** -8.4 kcal/mol
* **Lipinski's Rule of 5:** 100% Compliance

  
### **Key Conclusion**
Based on the binding energy of **-8.4 kcal/mol**, Berberine shows a significantly higher affinity for the target enzyme (Alpha-glucosidase) than the traditional drug Acarbose. This suggests it has high potential as a natural therapeutic agent for Type-2 Diabetes management.


##  Tech Stack:
- **Language:** Python
- **Database:** PubChem
- **Analysis:** SwissADME, PDBe, SwissDock

