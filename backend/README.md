``` bash
personalised_learning_app/backend/
│
├── data/
│   ├── raw/                 # PDF scan, CSV 
│   ├── processed/           # cleaned Data (JSON/CSV)
│   └── embeddings/          # Vector data
│
├── src/
│   ├── __init__.py
│   │
│   ├── materials_pipeline/           # process learning materials
│   │   ├── pdf_to_images.py
│   │   ├── ocr_engine.py
│   │   ├── chunker.py
│   │   └── material_pipeline.py
│   │
│   ├── profiles_pipeline/            # process student profiles
│   │   ├── profile_cleaner.py
│   │   ├── feature_extractor.py
│   │   └── profile_pipeline.py
│   │
│   ├── structures_pipeline/          # process learning structures
│   │   ├── parser.py
│   │   └── structure_pipeline.py
│   │
│   ├── utils/              
│   │   ├── text_cleaner.py
│   │   ├── spell_corrector.py
│   │   └── saver.py
│   │
│   └── pipeline_orchestrator.py   # connect multiple pipelines
│
├── requirements.txt
│
├── run_materials.py          # Entry point for material pipeline
├── run_profiles.py           # Entry point for profile pipeline
└── run_full_pipeline.py      # Entry point for toàn bộ system
```

git command:
- tesseract --version
- 