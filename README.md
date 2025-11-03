# LVMC-HeartSeg

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC--BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/)
[![Framework: nnU-Net v2](https://img.shields.io/badge/framework-nnU--Net%20v2-brightgreen.svg)](https://github.com/MIC-DKFZ/nnUNet)
[![Status: Academic Research](https://img.shields.io/badge/status-Academic%20Research-orange.svg)]()
[![Made with ❤️ at DKFZ/NCT Heidelberg](https://img.shields.io/badge/made%20with%E2%9D%A4-DKFZ%2FNCT%20Heidelberg-red.svg)]()

Automatic segmentation of cardiac substructures (**left ventricular myocardial walls and coronary arteries**)  
on non-angiographic contrast CT (cCT), based on **nnU-Net v2**.

---

## 🧩 Features
- nnU-Net v2–based 3D full-resolution architecture for non-angiographic cCT
- Segmentation of LV myocardial walls (apical, septal, inferior, anterior, lateral), coronary arteries (LMCA, LAD, LCx, RCA), and major chambers/vessels
- Iterative AI-assisted annotation workflow with human-in-the-loop refinement
- Complete hyperparameter configurations in `configs/training_hyperparameters.yaml`

---

## ⚙️ Environment Setup
```bash
conda env create -f environment.yml
conda activate radai
```

---

## 🚀 Usage
```bash
python train.py --config configs/training_hyperparameters.yaml
python inference.py --input data/example_case/CT.nii.gz --output results/LVMC_mask.nii.gz
```

---

## 🧠 Citation

If you use **LVMC-HeartSeg** in your research or publications, please cite:

> Wei J, Knoll M, Furkel J, Abdollahi A, *et al.*  
> **LVMC-HeartSeg: Automatic left ventricular myocardial and coronary artery segmentation on non-angiographic cCT using nnU-Net v2.**  
> 2025. *Manuscript in preparation.*  
> [https://github.com/jielinwei/LVMC-HeartSeg](https://github.com/jielinwei/LVMC-HeartSeg)

```bibtex
@software{Wei2025_LVMC_HeartSeg,
  author  = {Wei, Jielin and Knoll, Maximilian and Furkel, Jennifer and Abdollahi, Amir},
  title   = {LVMC-HeartSeg: Automatic LV myocardial wall and coronary artery segmentation on non-angiographic cCT using nnU-Net v2},
  year    = {2025},
  url     = {https://github.com/jielinwei/LVMC-HeartSeg},
  note    = {Code released under CC BY-NC-SA 4.0 for academic use}
}
```

---

## 🧩 License
This project is licensed under **CC BY-NC-SA 4.0** (academic and research use only).  
Commercial use is **not permitted** without explicit permission.  
License: https://creativecommons.org/licenses/by-nc-sa/4.0/  
Commercial contact: jielin.wei@dkfz-heidelberg.de

---

## 🔒 Intended Use & Data Privacy

**Intended Use.**  
This repository is provided **for academic research and method reproduction only**.  
It is **not** intended for clinical diagnosis, treatment planning, or any other clinical decision-making.

**Data Privacy.**  
This repository does **not** include any protected health information (PHI).  
The directory `data/example_case/` is reserved for **anonymized demo samples only**.  
Do not upload or share real patient data through this repository.

---

## 🧑‍💻 Contact
**Jielin Wei, MD**  
Postdoctoral Researcher, DKFZ/NCT Heidelberg  
📧 jielin.wei@dkfz-heidelberg.de
