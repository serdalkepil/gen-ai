# Generative AI Development: Resource Guide & Framework Comparison

This guide outlines the essential resources and framework comparisons for building advanced Generative AI applications using **Amazon Bedrock**, **Amazon SageMaker**, and leading orchestration layers.

---

## 1. Resource Directory for Generative AI Development

| Category | Resource Title | Description | URL / GitHub Reference |
| :--- | :--- | :--- | :--- |
| **AWS Core** | **Amazon Bedrock Samples** | Official repository for RAG, prompt engineering, and agent deployment examples. | [GitHub - Bedrock Samples](https://github.com/aws-samples/amazon-bedrock-samples) |
| **AWS Core** | **SageMaker GenAI Examples** | End-to-end notebooks for fine-tuning LLMs and deploying production endpoints. | [GitHub - SageMaker GenAI](https://github.com/aws-samples/generative-ai-on-amazon-sagemaker) |
| **Orchestration** | **LangChain AWS Integration** | Documentation for integrating LangChain with Bedrock and SageMaker. | [LangChain AWS Docs](https://python.langchain.com/docs/integrations/platforms/aws/) |
| **Multi-Agent** | **CrewAI Framework** | Role-based multi-agent orchestration for collaborative AI workflows. | [GitHub - CrewAI](https://github.com/crewAIInc/crewai) |
| **AWS Native** | **AWS Strands SDK** | Graph-based orchestration optimized for AWS-native serverless agents. | [GitHub - Agent Dev Toolkit](https://github.com/awslabs/agent-dev-toolkit) |
| **Data/RAG** | **LlamaIndex AWS** | Specialized framework for connecting private data sources to Bedrock models. | [GitHub - LlamaIndex AWS](https://github.com/run-llama/llama_index) |

---

## 2. Framework Comparison Matrix (2026)

| Feature | **AWS Strands** | **LangGraph** | **CrewAI** |
| :--- | :--- | :--- | :--- |
| **Core Concept** | **Autonomous Logic:** Model-driven loops via tools. | **State Machine:** Explicit nodes/edges for precision. | **Role-Based Team:** Collaborative "employees." |
| **Orchestration** | Dynamic Reasoning (Plan → Act). | Graph-based (Cyclic/Acyclic). | Process-driven (Sequential/Hierarchical). |
| **Persistence** | Lightweight/Ephemeral. | **Durable:** Full check-pointing & time-travel. | Contextual: Shared short/long-term memory. |
| **Standard** | **MCP** (Model Context Protocol). | Custom Tool/LangChain Ecosystem. | Built-in Crew Tools & Search tools. |
| **Infrastructure** | **AWS-Native:** Optimized for Bedrock/Lambda. | Agnostic: Integrates via `langchain-aws`. | Agnostic: High portability across clouds. |

---

## 3. Decision Guide: Which One Should You Pick?

* **Go with CrewAI** if you are building an **automated agency** (e.g., a "Content Crew" where a Researcher finds facts, a Writer drafts, and an Editor checks for SEO). It feels the most "human" to build and is perfect for rapid prototyping where roles are clearly defined.
* **Go with LangGraph** if your process is **non-linear and high-stakes** (e.g., a "Financial Audit" where an agent must loop back, re-verify data if a specific threshold is met, and wait for a human signature).
* **Go with AWS Strands** if you need a **lightweight, autonomous worker** that lives inside your AWS VPC and needs to interact with S3, DynamoDB, or external APIs using the Model Context Protocol (MCP) without a complex graph setup.

---

## 4. Code Implementation Samples

### Sample 1: CrewAI with Amazon Bedrock
CrewAI treats agents like specialized team members with "backstories."

```python
from crewai import Agent, Task, Crew, LLM

# Configure Bedrock (Claude 3.5 Sonnet)
bedrock_llm = LLM(
    model="bedrock/anthropic.claude-3-5-sonnet-20241022-v2:0",
    region_name="us-east-1"
)

# Define Agent with Persona
researcher = Agent(
  role='Cloud Architect',
  goal='Analyze AWS infrastructure cost optimizations',
  backstory='Expert in FinOps with 15 years of AWS experience.',
  llm=bedrock_llm
)

# Define Task & Execution
task = Task(
    description='Analyze EBS volume sprawl and suggest cleanup.', 
    agent=researcher, 
    expected_output="A 3-step cost optimization plan."
)

crew = Crew(agents=[researcher], tasks=[task])
print(crew.kickoff())
