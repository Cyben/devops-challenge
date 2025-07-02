# TROUBLE.md

This file documents the main issues I encountered during development of the **DevOps Challenge – thedoctor** project, and how I addressed them.

---
## 1. DynamoDB Key Schema Error

**Problem:**

When running this line in `get_secret()`:

```python
response = table.get_item(Key={'code_name': code_name})
```

I encountered the following error:
```
botocore.exceptions.ClientError: An error occurred (ValidationException) when calling the GetItem operation: 
The provided key element does not match the schema
```

I didn’t have permission to run dynamodb:DescribeTable, so I couldn’t inspect the key schema. This made it unclear whether code_name was really the primary key.

I reached out to confirm the key structure and was told every parameter in the exercise, including DynamoDB keys, should be written in `camelCase` instead of `snake_case`.

**Solution**  

Once I changed the key name from 'code_name' to 'codeName' the query worked correctly, and the issue was resolved.

## 2. Travis CI Not Free

**Problem:**

The instructions recommended using Travis CI, but as of 2025, Travis no longer offers a free plan for new users.

**Solution:**

Instead of using Travis CI, I migrated the pipeline to GitHub Actions, which:
- Integrates natively with GitHub
- Is free for public repositories
- Supports all the required steps (testing, Docker builds, pushing to Docker Hub)

I rewrote the CI/CD workflow in .github/workflows/cicd.yml, maintaining the same behavior as the original Travis setup.

