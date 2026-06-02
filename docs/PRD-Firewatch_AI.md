# Product Requirements Document (PRD)

## FireWatch AI

**Version:** 1.0 (MVP)  
**Date:** June 2026  
**Status:** Draft

---

### 1. Product Overview

**Product Name:** FireWatch AI

**Description:**  
A dual-interface system that detects wildfires early using satellite imagery. It provides a technical dashboard for ML developers and a simple, actionable interface for emergency responders and firefighters.

**Objective:**  
Bridge the gap between machine learning models and real-world emergency response by delivering fast, accurate, and usable wildfire detections.

---

### 2. Input Data & Resources

- **Main Dataset:** [Wildfire Prediction Dataset](https://www.kaggle.com/datasets/abdelghaniaaba/wildfire-prediction-dataset/data)
- **Models:** 2 pre-trained model versions (provided in `models.zip`)
- **Additional Data:**
  - Training history and evaluation metrics (CSV files)
  - Validation and Test datasets
  - Satellite images (RGB + Infrared when available)

---

### 3. User Personas & User Stories

#### **User 1: Developer / ML Engineer** (Developer Dashboard)

**As a Developer I want to:**

1. View and compare all available models with their performance metrics
2. Browse training logs, loss curves, and evaluation history
3. Upload new models or new versions easily
4. Run inference on single images or entire test datasets
5. Analyze model weaknesses (especially False Negatives)
6. Compare multiple models side-by-side
7. Export reports and prediction results
8. View dataset statistics and class distribution
9. Track experiments and training runs

---

#### **User 2: Emergency Responder** (Responder Interface)

**As an Emergency Responder I want to:**

1. Receive immediate alerts when a fire is detected
2. See the exact geographic location of the fire on a map
3. View the original satellite image with highlighted fire area
4. See confidence score, estimated fire size, and severity level
5. Understand whether the fire is growing
6. Mark detections as “Verified”, “False Positive”, or “Handled”
7. View history of fires in my area
8. Generate quick incident reports

---

### 4. Technology Stack (MVP)

| Component                    | Tool                  | Purpose |
|-----------------------------|-----------------------|--------|
| Developer Dashboard         | **Streamlit**         | Technical interface |
| Responder Interface         | **Gradio**            | Simple & mobile-friendly UI |
| Backend / Inference         | Python + PyTorch/ONNX | Model serving |
| Data Storage                | Local + Google Sheets | MVP persistence |
| Mapping                     | Folium / Leaflet      | Interactive maps |
| Communication               | Google Sheets API     | Between interfaces |

---

### 5. Functional Requirements

#### Developer Dashboard (Streamlit)
- Model Registry / Leaderboard
- Training History & Metrics Visualization
- Inference Playground
- Misclassification Explorer
- Model Upload & Versioning
- Performance Comparison Tool

#### Responder Interface (Gradio)
- Fire Detection Feed
- Interactive Map View
- Image Viewer with Overlay
- Alert System with Severity Levels
- Feedback Mechanism
- Incident History

---

### 6. Non-Functional Requirements

- **Inference Speed:** < 3 seconds per image (target)
- **Usability:** Responder interface must be intuitive under pressure
- **Reliability:** Prioritize high Recall (minimize missed fires)
- **Mobile Support:** Responder interface must work well on tablets/phones
- **Security:** Basic authentication for both interfaces

---

### 7. Success Metrics

**Developer Dashboard:**
- Can compare models in under 30 seconds
- Can run inference on new image in under 10 seconds

**Responder Interface:**
- Time to understand a detection < 15 seconds
- High user satisfaction among test responders

---

### 8. Next Steps

1. Finalize folder structure and project architecture
2. Build Developer Dashboard (Streamlit)
3. Build Responder Interface (Gradio)
4. Implement Google Sheets integration
5. Create unified inference service
6. Test end-to-end workflow

---

### 9. Open Questions

- Should both interfaces run in one app or as two separate apps?
- Do we migrate from Google Sheets to a proper database (PostgreSQL/Supabase) in Stage 2?
- What is the target deployment environment? (Local, Server, Cloud)

---

**Resources:**
- Kaggle Dataset: https://www.kaggle.com/datasets/abdelghaniaaba/wildfire-prediction-dataset/data
- Models & Training Data: `models.zip`

---

*End of Document*