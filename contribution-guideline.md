# Contribution guidelines 

## BRANCHES NAMING CONVENTIONS
- New features    -> `Feature/feature-name`
- Enhancements -> `Enhancements/enhancements-description`
- Bug fixes           -> `Fixes/small-description`

**IMPORTANT FOR NAMING BRANCHES**
- **kabab-case** for names/descriptions
- **Uppercase** for the first letter
- **Lowercase** for all the remaining letter
- **No** spaces

## APIs development
- Models **MUST** always have `CreateDateTime` and `CreateUser`
- Models **SHOULD**  have `LastModificationUser` and `LastModificationDateTime`
- **GET** (ALL/ BY ID) + Filters + OrderBy  
- **POST** CREATE (without ID) **AND** UPDATE (with ID)
- **PUT/PATCH** Update record 
- **DELETE** Delete record
- **Endpoints** should be **significant names** in **kabab-case**
- **JSON** keys returned fom endpointd must be in **snake_case**

## Naming conventions 
Naming is very important in programming, it simplify code understanding and reduce the need for documentations.
Here is some rules :
- Names should be **SIGNIFICANT**
- **VARIABLES** : *name* add `s` to lists/arrays || boolean should start with [`is`, `has`, `alllow`] 
- **FUNCTIONS** :  *verb + noun* (ex query_neo4j)
- **CLASSES** : *noun + type* (Api, Model, Service, Prompt, ...)
- **FILES** : *noun + content type* (controler, view, api, widget, container, ...)
- **COMMIT** : verb + subject + object (ex add ... to ... | delete .. from ...)
- **BRANCH** : (Fixes | Enhancements | Feature)/**noun** (nous should be taken from Gitlab issues or Backlogs


## Cleaning code is important before push or merge
- *FORMAT* code,
- Remove unnecessary *LOGS*,
- Remove unnecessary *IMPORTS*,
- Resolve *WARNINGS*,
- Check *VERSIONS*


## Code refactoring tasks (**breath**):
- Clean code
- Add **Exception** handling (ex Python try/except/else)
- Check names (variables, functions, classes, files, ...)
- Remove unused files (old code)
- Check TODOs
- Update Issues in Gitlab
- Documentation (comments for important functions)

## Files and variables naming conventions

### Javascript / NextJS
- **PascalCase** for Interfaces
- **camelCase** for file names, variabes (including object instances) and React components
- No **spaces** are allowed

### Python / Django
- **snake_case** for folders, file names and variables
- **PascalCase** for classes
- No **spaces** are allowed
