| **Column**    | **Definition**                                                                                             |
|---------------|-----------------------------------------------------------------------------------------------------------|
| `sample_id`   | Unique numeric ID for each sample (e.g., 1, 2, 3, …).                                                    |
| `gene_id`     | Synthetic gene identifier (e.g., `ENSG1000000`), representing a unique gene in the dataset.               |
| `read_count`  | Raw RNA-seq read counts (integer value), indicating the abundance of reads mapped to a particular gene.   |
| `fpkm`        | Normalized expression measure (Fragments per Kilobase of transcript per Million mapped reads).            |
| `condition`   | Experimental condition or treatment (e.g., `Control`, `TreatmentA`, `TreatmentB`).                        |
| `species`     | Organism source of the sample (e.g., `Human`, `Mouse`).                                                  |
| `replicate`   | Replicate number (1, 2, or 3) to differentiate multiple experimental runs or biological replicates.       |


import numpy as np
import pandas as pd

# Set seed for reproducibility (optional)
np.random.seed(42)

# Number of synthetic RNA-seq records
num_records = 2000

# Generate sample IDs
sample_ids = np.arange(1, num_records + 1)

# Create a small pool of synthetic gene IDs
gene_pool = [f"ENSG{1000000 + i}" for i in range(100)]  # 100 synthetic gene IDs

# Randomly select gene IDs for each record
gene_ids = np.random.choice(gene_pool, size=num_records)

# Simulate read counts (integer range)
read_counts = np.random.randint(0, 100001, size=num_records)

# Simulate FPKM values from a log-normal-like distribution (clip to ensure no negative values)
fpkm_values = np.abs(np.random.normal(loc=5, scale=2, size=num_records))

# Possible conditions
conditions = ["Control", "TreatmentA", "TreatmentB"]
condition_assignments = np.random.choice(conditions, size=num_records)

# Possible species
species_list = ["Human", "Mouse"]
species_assignments = np.random.choice(species_list, size=num_records)

# Replicates (1, 2, or 3)
replicates = np.random.randint(1, 4, size=num_records)

# Create the DataFrame
df_rnangs = pd.DataFrame({
    "sample_id": sample_ids,
    "gene_id": gene_ids,
    "read_count": read_counts,
    "fpkm": fpkm_values,
    "condition": condition_assignments,
    "species": species_assignments,
    "replicate": replicates
})

# Display the first few rows
print(df_rnangs.head())

# Save to CSV (remove or comment out if not needed)
df_rnangs.to_csv("RNANGS_data.csv", index=False)
