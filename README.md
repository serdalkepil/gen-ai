# gen-ai

A comprehensive collection of AWS Bedrock and generative AI examples demonstrating various AI/ML capabilities including foundation models, batch inference, RAG, LangChain, and AI agents.

## Overview

This repository contains hands-on examples and tutorials for working with AWS Bedrock and generative AI technologies. Each module focuses on specific capabilities and use cases.

## Modules

### Module 2: Foundation Models
- Listing available foundation models on AWS Bedrock
- Invoking models using `invoke_model` API
- Using the Converse API for unified model interaction
- Working with multiple model providers (Amazon Titan, Llama, Mistral, Claude, Nova)
- Streaming responses with `converse_stream`

### Module 4: Advanced Bedrock Features
- **Inference Profiles**: Cross-region inference and custom profiles
- **Batch Inference**: Processing large datasets asynchronously
- **Prompt Caching**: Optimizing costs with Nova Lite prompt caching
- **Converse on Documents**: Direct document analysis with PDF support
- **Conversation History**: Managing chat history with DynamoDB

### Module 5: RAG (Retrieval Augmented Generation)
- Building RAG systems from scratch
- PDF text extraction and chunking
- Vector embeddings with Amazon Titan
- OpenSearch Serverless integration
- Semantic search and document retrieval

### Module 6: LangChain Integration
- Basic LangChain invocation and chaining
- Prompt templates and output parsers
- Conversation history with DynamoDB
- Message history management

### Module 9: AI Agents
- **Converse with Tools**: Function calling and tool integration
- **Converse with MCP**: Model Context Protocol implementation
- **CrewAI Agents**: Multi-agent orchestration
- **Strands Agents**: Agent workflows with and without MCP

## Project Structure

```
gen-ai/
├── module2.ipynb              # Foundation models basics
├── module4.ipynb              # Advanced Bedrock features
├── module5.ipynb              # RAG implementation
├── module6.ipynb              # LangChain integration
├── module9-converse_with_tools.ipynb
├── module9-converse_mcp.ipynb
├── module9-crewai-agents.ipynb
├── module9-strands-agents.ipynb
├── module9-strands-agents-mcp.ipynb
├── module9-mcp_server.py      # MCP server implementation
├── input/                     # Sample data files
│   ├── AnyCompany_financial_10K.pdf
│   └── city-reviews-manifest.jsonl
├── email-gen-sls/            # Serverless email generation
│   ├── src/app.py
│   ├── template.yaml
│   └── README.md
├── generate_200_cities_non_batch.py
└── setup_batch_role.py
```

## Prerequisites

- Python 3.12+
- AWS Account with Bedrock access
- AWS CLI configured
- Required Python packages:
  - boto3
  - langchain
  - langchain-community
  - opensearchpy
  - PyPDF2

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd gen-ai
```

2. Install dependencies:
```bash
pip install boto3 langchain langchain-community opensearchpy PyPDF2
```

3. Configure AWS credentials:
```bash
aws configure
```

4. Enable required Bedrock models in your AWS account

## Usage

### Running Jupyter Notebooks

Open any module notebook in Jupyter:
```bash
jupyter notebook module2.ipynb
```

### Key Examples

**Invoke a model:**
```python
import boto3
import json

bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')
response = bedrock.converse(
    modelId='amazon.nova-lite-v1:0',
    messages=[{
        "role": "user",
        "content": [{"text": "Hello!"}]
    }]
)
```

**RAG with OpenSearch:**
```python
# Get embeddings
embedding = get_embedding(text)

# Search similar documents
results = opensearch_client.search(
    index=index_name,
    body={"query": {"knn": {"embedding": {"vector": embedding, "k": 3}}}}
)
```

**LangChain with conversation history:**
```python
from langchain_core.runnables.history import RunnableWithMessageHistory

chain_with_history = RunnableWithMessageHistory(
    chain,
    lambda session_id: DynamoDBChatMessageHistory(
        table_name="conversation-history",
        session_id=session_id
    )
)
```

## Features

- ✅ Multiple foundation model providers
- ✅ Batch inference for large-scale processing
- ✅ RAG implementation with vector search
- ✅ Conversation history management
- ✅ Prompt caching optimization
- ✅ Document analysis capabilities
- ✅ AI agent orchestration
- ✅ MCP integration
- ✅ Serverless deployment examples

## AWS Services Used

- **Amazon Bedrock**: Foundation models and inference
- **Amazon DynamoDB**: Conversation history storage
- **Amazon OpenSearch Serverless**: Vector search
- **Amazon S3**: Document and data storage
- **AWS Lambda**: Serverless functions
- **AWS SAM**: Serverless application deployment

## Cost Optimization

- Use inference profiles for cross-region routing
- Enable prompt caching for repeated contexts
- Leverage batch inference for large datasets
- Implement TTL for DynamoDB conversation history

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

This project is provided as-is for educational purposes.

## Resources

- [AWS Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [LangChain Documentation](https://python.langchain.com/)
- [OpenSearch Documentation](https://opensearch.org/docs/)
