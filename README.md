# UCL Bank marketing

- Created: August 26, 2021 12:55 AM
- Last Edited Time: August 6, 2022 1:01 AM
- Status: In Progress 🙌
- Type: Technical Spec

# Summary

This aim of this project is to build a simple credit model using bank data from UCI. The goal is to get to a good model which runs end-to-end and play with some considerations as if we where to put it into production. This is a fun exercise and is more about skills development that "real ML" so we do not focus on the modelling but more the thought process behind building it.

## Data source

The original data is [Bank Marketing Data Set from UCI](https://archive.ics.uci.edu/ml/machine-learning-databases/00222/](https://archive.ics.uci.edu/ml/machine-learning-databases/00222/). This was added to this git repo in order to create an end-point to query throughout development.


# Background

What is the motivation for these changes? What problems will this solve? Include graphs, metrics, etc. if relevant. 


This was originally a case study given in an unsuccessful interview, but I enjoyed working on it so after gaining more experience, I have chosen to return to it a year later.

This is a binary classification with very imbalanced data.


- 

# Goals

What are the outcomes that will result from these changes? How will we evaluate success for the proposed changes? 

- Deal with class imbalance (SMOTE, undersampling, oversampling)

### Non-Goals

To narrow the scope of what we're working on, outline what this proposal will not accomplish.

- Split into Train-Validation-Test (our data is too small for this)
- Containerize our application

# Proposed Solution

Describe the solution to the problems outlined above. Include enough detail to allow for productive discussion and comments from readers.

- API that takes through data and outputs scores.


```mermaid
graph TD;
  A-->B;
  A-->C;
  B-->D;
  C-->D;
```

### Risks

Highlight risks so your reviewers can direct their attention here. 

- 

### Milestones

Break down the solution into key tasks and their estimated deadlines. 

- 

### Open Questions

Ask any unresolved questions about the proposed solution here.

- 

# Follow-up Tasks

What needs to be done next for this proposal? 

- [ ]

