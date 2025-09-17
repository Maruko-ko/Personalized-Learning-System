# AI-powered Personalised Learning Material
## Overview
The purpose of this project is to create a web application that help learner improve their English usage by inputting the required information. Our application will process that input with the internal existing materials and generate the customed / personalised Learning Material that can be adjust along their learning jorney.
## Table of content
### Project structure
frontend
- src
    - styles
    - pages
    - components
backend
- models
- data
- preprocessing_data
### Data processing
#### Type of data
1. ``Student's profile``: With all the personal confidential data was getting rid of. Only the anonymous data which is helpful for the project is remained.
2. ``Learning Material``: Act as the reference Learning Material for the model to generate personalised learning material.
3. ``Pre-scheduled time plan``: Acts as the reference schedule for the model to generate the personalised timeline for each learner.
### How to run 
#### Backend
```bash
cd backend/
```
#### Frontend
Move to the correct location
```bash
cd frontend/
```

```bash
npm start
```


## Limitation and disclaimer
This project is not fully developed yet, instead it show the approach that a developer might get when creating a web application with OpenAI API integrated.