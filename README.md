# PCA-ICA-LSTM-A-Hybrid-Deep-Learning-Model

[![Paper](https://img.shields.io/badge/Paper-Springer%20Link-blue)](https://link.springer.com/article/10.1007/s10614-024-10629-x)
[![DOI](https://img.shields.io/badge/DOI-10.1007%2Fs10614--024--10629--x-green)](https://doi.org/10.1007/s10614-024-10629-x)
[![Python](https://img.shields.io/badge/Python-3.8%2B-brightgreen)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository contains the Python/TensorFlow implementation of the hybrid **PCA-ICA-LSTM** framework proposed in the following study:

> **Paper:** PCA-ICA-LSTM: A Hybrid Deep Learning Model Based on Dimension Reduction Methods to Predict S&P 500 Index Price  
> **Journal:** Computational Economics (Springer), 2025  
> **Direct Link:** https://link.springer.com/article/10.1007/s10614-024-10629-x  
> **DOI:** https://doi.org/10.1007/s10614-024-10629-x


## 📌 Overview


Financial time series data are non-linear, non-stationary, and prone to high dimensionality and multicollinearity. This study introduces the PCA-ICA-LSTM architecture, a two-stage hybrid framework combining statistical dimensionality reduction techniques with deep recurrent neural networks:

Dimensionality Reduction and Denoising:

Principal Component Analysis (PCA): Eliminates multicollinearity and maximizes variance retention across orthogonal components.

Independent Component Analysis (ICA): Extracts statistically independent, non-Gaussian latent features from mixed market signals.

Sequential / Temporal Modeling:

Long Short-Term Memory (LSTM): Captures temporal dependencies and long-term sequential relationships using the distilled, low-dimensional feature space.

Experimental findings show that the PCA-ICA-LSTM model consistently outperforms benchmark deep neural networks (SimpleRNN, GRU, CNN and standard LSTM) across both high-dimensional and compressed feature spaces, demonstrating superior noise robustness and improved forecasting accuracy on the S&P 500 index.


📂 Repository Structure

```monospace
.
├── models/
│   └── pca_ica_lstm.py       # Hybrid PCA-ICA-LSTM model
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation


⚙️Core Dependencies

Python >= 3.8
TensorFlow >= 2.10
scikit-learn
pandas
numpy
matplotlib


📊 Evaluation Metrics


Model forecasting accuracy and financial performance are evaluated using the following statistical and economic metrics:

* Coefficient of Determination (**R²**)
* Mean Squared Error (**MSE**)
* Mean Absolute Error (**MAE**)
* Mean Absolute Percentage Error (**MAPE**)
* Maximum Residual Error (**Max Error**)
* Cumulative / Investment Return Ratio (**Return Ratio**)


📄 Citation

If you find this research or codebase helpful, please cite the original article:

@article{sarikoc2025pca,
  title={PCA-ICA-LSTM: A Hybrid Deep Learning Model Based on Dimension Reduction Methods to Predict S\&P 500 Index Price},
  author={Sar{\i}ko{\c{c}}, M. and Celik, M.},
  journal={Computational Economics},
  volume={65},
  pages={2249--2315},
  year={2025},
  publisher={Springer},
  doi={10.1007/s10614-024-10629-x}
}


📝 License

This project is licensed under the MIT License.