# SRA AI Server

SRA AI Server based on MAIST Flask API:  
[Basic MAIST Flask API](https://github.com/Yonsei-Maist/flask-api.git)

## Relative work
[Electron Desktop Client](https://github.com/Yonsei-Maist/electron-systematic-review-automation.git)

## About the Project

### Summary
- use pre-trained BERT for sentence embedding
- train and test for Topic modeling
- Research about Topic modeling

### Functions
- Train and test
- Predict Topic from Text

## Environment
```
python 3.8 ~
tensorflow 2.4 ~
maist-model-core 1.0 ~
flask 2.0.1 ~
flask-blueprint 1.3.0 ~
flask-cors 3.0.10 ~
flask_marshmallow 0.14.0 ~
flask_migrate 3.0.1 ~
flask_sqlalchemy 2.5.1 ~
marshmallow-sqlalchemy 0.26.1 ~
```

## Install
```
pip install -U git+https://git@github.com/Yonsei-Maist/maist-flask-api-sra.git
```

## Install Custom Library
```
pip install -U git+https://git@github.com/Yonsei-Maist/maist-model-core.git
```

## Run
```
python serve.py {some options}
```

## Author
```
Chanwoo Gwon, Yonsei Univ. Researcher, since 2020.05 ~
```

## maintainer
```
Chanwoo Gwon, arknell@yonsei.ac.kr (2021.08. ~)
```
