
CATEGORIES = ["Membrane","Cytoplasm","Nucleus","Extracellular","Cell membrane","Mitochondrion","Plastid","Endoplasmic reticulum","Lysosome/Vacuole","Golgi apparatus","Peroxisome"]
SS_CATEGORIES = ["NULL", "SP", "TM", "MT", "CH", "TH", "NLS", "NES", "PTS", "GPI"] 

FAST = "Fast"
ACCURATE = "Accurate"
HPA = "Hpa"
ONEHOT = "onehot"
SEQVEC = "seqvec"
BEPLER = "bepler"
CPCPROT = "cpcprot"

EMBEDDINGS = {
    FAST: {
        "embeds": "data_files/embeddings/esm1b_swissprot.h5",
        "config": "swissprot_esm1b.yaml",
        "source_fasta": "data_files/deeploc_swissprot_clipped1k.fasta",
        "available_embeds": "OneHot_deeploc_swissprot_clipped1k.npy"
    },
    ACCURATE: {
        "embeds": "data_files/embeddings/prott5_swissprot.h5",
        "config": "swissprot_prott5.yaml",
        "source_fasta": "data_files/deeploc_swissprot_clipped4k.fasta",
        "available_embeds": "OneHot_deeploc_swissprot_clipped1k.npy"
    },
    HPA: {
        "embeds": "data_files/embeddings/esm1b_swissprot.h5",
        "config": "hpa_esm1b.yaml",
        "source_fasta": "data_files/deeploc_hpa_clipped1k.fasta",
        "available_embeds": "OneHot_deeploc_swissprot_clipped1k.npy"
    },
    ONEHOT: {
        "embeds": "data_files/embeddings/esm1b_swissprot.h5",
        "config": "swissprot_esm1b.yaml",
        "source_fasta": "data_files/deeploc_swissprot_clipped1k.fasta",
        "available_embeds": "OneHot_deeploc_swissprot_clipped1k.npy"
    },
    SEQVEC: {
        "embeds": "data_files/embeddings/esm1b_swissprot.h5",
        "config": "swissprot_esm1b.yaml",
        "source_fasta": "data_files/deeploc_swissprot_clipped1k.fasta",
        "available_embeds": "SeqVec_deeploc_hpa_clipped1k.npy"
    },
    BEPLER: {
        "embeds": "data_files/embeddings/esm1b_swissprot.h5",
        "config": "swissprot_esm1b.yaml",
        "source_fasta": "data_files/deeploc_swissprot_clipped1k.fasta",
        "available_embeds": "Bepler_deeploc_swissprot_clipped1k.npy"
    },
    CPCPROT: {
        "embeds": "data_files/embeddings/esm1b_swissprot.h5",
        "config": "swissprot_esm1b.yaml",
        "source_fasta": "data_files/deeploc_swissprot_clipped1k.fasta",
        "available_embeds": "CPCProt_deeploc_swissprot_clipped1k.npy"
    },
}

SIGNAL_DATA = "data_files/multisub_ninesignals.pkl"
LOCALIZATION_DATA = "./data_files/multisub_5_partitions_unique.csv"

BATCH_SIZE = 128
SUP_LOSS_MULT = 0.1
REG_LOSS_MULT = 0.1

