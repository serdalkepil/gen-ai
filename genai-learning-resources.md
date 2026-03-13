# 🚀 Generative AI Development — Learning Resources

> A curated reference guide covering AWS Bedrock, Amazon SageMaker, and integrations with LangChain, Strands Agents, and CrewAI — including documentation, code examples, and GitHub repositories.

---

## 📌 Table of Contents
- [AWS Amazon Bedrock](#-aws-amazon-bedrock)
- [Amazon SageMaker & JumpStart](#-amazon-sagemaker--jumpstart)
- [Strands Agents SDK (AWS)](#-strands-agents-sdk-aws)
- [LangChain + LangGraph + AWS](#-langchain--langgraph--aws)
- [CrewAI + AWS Bedrock](#-crewai--aws-bedrock)
- [Multi-Framework Integration Examples](#-multi-framework-integration-examples)
- [Courses & Tutorials](#-courses--tutorials)

---

## ☁️ AWS Amazon Bedrock

| Title | Description | URL |
|-------|-------------|-----|
| **Amazon Bedrock — Product Page** | Official AWS product page; overview of foundation models, features, pricing, and enterprise capabilities. | https://aws.amazon.com/bedrock/ |
| **Bedrock User Guide (Official Docs)** | Comprehensive developer reference: API quickstart, model IDs, Converse API, Agents, Knowledge Bases, Guardrails, and more. | https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html |
| **Bedrock FAQs** | Answers to common questions covering fine-tuning, RAG, Agents, security, and when to choose Bedrock vs SageMaker. | https://aws.amazon.com/bedrock/faqs/ |
| **Bedrock Python SDK Quickstart (boto3)** | Code example: invoke Claude via boto3 in Python in under 5 minutes. Includes model IDs and API structure. | https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started-api.html |
| **AWS Bedrock AgentCore** | Fully managed agent platform to build, deploy, and scale AI agents in production with enterprise-grade security and observability. | https://aws.amazon.com/bedrock/agentcore/ |
| **Bedrock Agents — Official Docs** | Build and configure autonomous agents with action groups, Knowledge Bases, Lambda integrations, and multi-agent collaboration. | https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html |
| **Bedrock Knowledge Bases** | Managed RAG: connect your data to FMs using vector databases and natural language queries with built-in citations. | https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html |
| **Bedrock Guardrails** | Add content filtering, PII redaction, grounding checks, and hallucination reduction to your generative AI apps. | https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html |
| **OpenAI-Compatible Mantle API on Bedrock** | Bedrock now supports OpenAI-compatible Projects, Responses, and Chat Completions APIs via the Mantle inference engine. | https://aws.amazon.com/about-aws/whats-new/2026/03/amazon-bedrock-projects-api-mantle-inference-engine/ |
| **AWS AI/ML Landscape 2026 — Deep Dive** | Community article explaining the full AWS AI/ML stack including Bedrock, AgentCore, and real-world architecture patterns. | https://dev.to/aws-builders/the-aws-aiml-landscape-in-2026-simplified-17i3 |
| **Amazon Bedrock Complete Guide — DataCamp** | Step-by-step tutorial: choosing foundation models, inference jobs, RAG, and best practices for production deployment. | https://www.datacamp.com/tutorial/aws-bedrock |
| **GitHub: aws-samples (Bedrock)** | Official AWS code samples repository; hundreds of notebooks and projects covering Bedrock use cases. | https://github.com/aws-samples?q=bedrock |
| **GitHub: amazon-bedrock-samples** | Curated sample code for Bedrock Agents, Knowledge Bases, model fine-tuning, RAG pipelines, and more. | https://github.com/aws-samples/amazon-bedrock-samples |
| **GitHub: generative-ai-on-aws (O'Reilly Book)** | Code notebooks from the O'Reilly book *Generative AI on AWS* — RAG, RLHF, fine-tuning, and deployment examples. | https://github.com/generative-ai-on-aws/generative-ai-on-aws |
| **AWS Certified Generative AI Developer — Exam Guide** | Official exam guide (PDF) covering skills in Bedrock Agents, SageMaker, Strands, MCP, and enterprise integration patterns. | https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/certification/approved/pdfs/docs-aip/AWS-Certified-Generative-AI-Developer-Pro_Exam-Guide.pdf |

---

## 🧠 Amazon SageMaker & JumpStart

| Title | Description | URL |
|-------|-------------|-----|
| **SageMaker JumpStart — Product Page** | ML hub with 600+ pretrained and foundation models, one-click deployment, and example notebooks for GenAI use cases. | https://aws.amazon.com/sagemaker/ai/jumpstart/ |
| **SageMaker JumpStart — Foundation Models Docs** | Official guide to accessing, deploying, fine-tuning, and evaluating foundation models (Llama, Mistral, Stable Diffusion, etc.) via JumpStart. | https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models.html |
| **SageMaker JumpStart — Pretrained Models Reference** | Browse all available models by type, framework, and task; links to example notebooks and Python SDK usage. | https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html |
| **Get Started with GenAI on SageMaker JumpStart (AWS Blog)** | Walkthrough of deploying GPT-2, Stable Diffusion 2.0, and FLAN-T5 using SageMaker JumpStart with example notebooks. | https://aws.amazon.com/blogs/machine-learning/get-started-with-generative-ai-on-aws-using-amazon-sagemaker-jumpstart/ |
| **Deploy GenAI Models from JumpStart using AWS CDK** | Tutorial: deploy Stable Diffusion and text generation models programmatically using CDK with Streamlit, Lambda, and API Gateway. | https://aws.amazon.com/blogs/machine-learning/deploy-generative-ai-models-from-amazon-sagemaker-jumpstart-using-the-aws-cdk/ |
| **SageMaker Guidance: GenAI Deployments via JumpStart** | AWS Solutions guidance: asynchronous SageMaker endpoints with CDK pipelines for production GenAI deployments. | https://aws.amazon.com/solutions/guidance/generative-ai-deployments-using-amazon-sagemaker-jumpstart/ |
| **Jupyter AI in SageMaker Notebooks** | Enable Jupyter AI in SageMaker Studio for code generation, notebook creation, and LLM-powered Q&A using Bedrock or JumpStart models. | https://docs.aws.amazon.com/sagemaker/latest/dg/jupyterai.html |
| **Advanced Tracing & Evaluation with LangChain + SageMaker MLflow** | Build and evaluate LangGraph agents on SageMaker using MLflow for experiment tracking, RAGAS metrics, and observability. | https://aws.amazon.com/blogs/machine-learning/advanced-tracing-and-evaluation-of-generative-ai-agents-using-langchain-and-amazon-sagemaker-ai-mlflow/ |
| **GitHub: llms-amazon-bedrock-sagemaker** | Notebooks using both Bedrock and SageMaker for RAG, embeddings, LLamaIndex, and LangChain integration. | https://github.com/aws-samples/llms-amazon-bedrock-sagemaker |
| **SageMaker Python SDK Docs** | API reference and usage guides for the SageMaker Python SDK: training, deployment, pipelines, and JumpStart model access. | https://sagemaker.readthedocs.io/en/stable/ |

---

## 🤖 Strands Agents SDK (AWS)

| Title | Description | URL |
|-------|-------------|-----|
| **Strands Agents — Official Site** | Homepage for AWS's open-source model-driven agent SDK, with customer testimonials and quickstart links. | https://strandsagents.com/ |
| **Strands Agents — Official Documentation** | Complete SDK docs: agents, tools, memory, multi-agent patterns, MCP integration, and model provider configuration. | https://strandsagents.com/docs/ |
| **Introducing Strands Agents (AWS Blog)** | Original launch post explaining the model-driven approach, ReAct-style reasoning, and design philosophy of Strands. | https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/ |
| **GitHub: strands-agents/sdk-python** | Source code for the Python SDK. Includes quickstart, tool definitions (`@tool` decorator), MCP client examples, and bi-directional audio (Nova Sonic). | https://github.com/strands-agents/sdk-python |
| **GitHub: strands-agents organization** | All 11+ official Strands repositories: Python SDK, TypeScript SDK, tools, samples, and community resources. | https://github.com/strands-agents |
| **Introducing Strands Labs (AWS Blog)** | Announcement of the experimental Strands Labs GitHub org, covering AI Functions, Strands Robots, and VLA robotics integration. | https://aws.amazon.com/blogs/opensource/introducing-strands-labs-get-hands-on-today-with-state-of-the-art-experimental-approaches-to-agentic-development/ |
| **GitHub: strands-labs organization** | Experimental Strands projects: Strands Robots, Strands Robots Sim (Libero benchmark), and AI Functions (@ai_function decorator). | https://github.com/strands-labs |
| **GitHub: cloudeng-strands-agent (sample)** | AWS cloud engineer agent built with Strands SDK + Bedrock + MCP (AWS Docs MCP Server + Diagram MCP). Includes Docker deployment and health check endpoints. | https://github.com/awsdataarchitect/cloudeng-strands-agent |
| **Strands Agents SDK Releases (GitHub)** | Release notes tracking all new features: A2AAgent protocol, Gemini tool fixes, Bedrock thinking mode, context window management, and more. | https://github.com/strands-agents/sdk-python/releases |
| **Strands Agents + Bedrock AgentCore (AWS Dev Blog)** | Guide to deploying Strands-built agents using the Bedrock AgentCore managed runtime with persistent memory and Docker packaging. | https://dev.to/aws/building-production-ready-ai-agents-with-crewai-and-amazon-bedrock-agentcore-2g36 |

---

## 🔗 LangChain + LangGraph + AWS

| Title | Description | URL |
|-------|-------------|-----|
| **LangChain AWS Integrations Docs** | Official LangChain docs page for all AWS integrations: Bedrock, SageMaker endpoints, S3, Kendra, Lambda, Knowledge Bases, and more. | https://python.langchain.com/docs/integrations/providers/aws/ |
| **GitHub: langchain-ai/langchain-aws** | Official LangChain-AWS monorepo: `ChatBedrockConverse`, SageMaker LLMs, AgentCore tools, LangGraph checkpointers (DynamoDB, ElastiCache), and vector stores. | https://github.com/langchain-ai/langchain-aws |
| **Build Multi-Agent Systems with LangGraph + Bedrock (AWS Blog)** | Tutorial building a multi-agent travel assistant using LangGraph supervisor patterns, LangGraph Studio, and Amazon Bedrock. | https://aws.amazon.com/blogs/machine-learning/build-multi-agent-systems-with-langgraph-and-amazon-bedrock/ |
| **GitHub: langgraph-agents-with-amazon-bedrock** | Workshop adapted from the DeepLearning.AI LangGraph course — runs locally or in SageMaker Studio; covers ReAct, planning, memory, and reflection patterns. | https://github.com/aws-samples/langgraph-agents-with-amazon-bedrock |
| **GitHub: amazon-bedrock-claude-langchain-samples** | Sample Jupyter notebooks using Claude on Bedrock with LangChain: chatbots, Q&A, summarization, and agents with tool use. | https://github.com/aws-samples/amazon-bedrock-claude-2-and-3-with-langchain-popular-use-cases |
| **LangChain ChatBedrockConverse — Code Example** | Quickstart code snippet using `ChatBedrockConverse` with Claude 4 Sonnet — the recommended approach replacing the deprecated Bedrock LLM class. | https://github.com/langchain-ai/langchain-aws#readme |
| **LangChain + Bedrock + Elasticsearch RAG (Notebook)** | Jupyter notebook: build a RAG pipeline with LangChain, Bedrock Titan embeddings, and Elasticsearch as the vector store. | https://github.com/elastic/elasticsearch-labs/blob/main/notebooks/integrations/amazon-bedrock/langchain-qa-example.ipynb |
| **Advanced Evaluation: LangGraph + SageMaker AI + MLflow** | Trace and evaluate LangGraph agents on SageMaker using MLflow and RAGAS, with code in the aws-samples GitHub repository. | https://aws.amazon.com/blogs/machine-learning/advanced-tracing-and-evaluation-of-generative-ai-agents-using-langchain-and-amazon-sagemaker-ai-mlflow/ |

---

## 🛸 CrewAI + AWS Bedrock

| Title | Description | URL |
|-------|-------------|-----|
| **CrewAI Official Documentation** | Full CrewAI docs: agents, tasks, crews, flows, memory, tools, and Amazon Bedrock integration toolkit with cookbook examples. | https://docs.crewai.com/ |
| **CrewAI on AWS — Prescriptive Guidance** | AWS prescriptive guidance page covering CrewAI architecture, role-based agent design, Bedrock FM selection, and observability stack. | https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-frameworks/crewai.html |
| **Deploy Agentic Systems on Bedrock with CrewAI + Terraform** | Step-by-step guide to deploying a multi-agent AWS security audit crew using CrewAI, Bedrock, Lambda, and Terraform. | https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-agentic-systems-on-amazon-bedrock-with-the-crewai-framework.html |
| **Build Agentic Systems with CrewAI + Bedrock (AWS ML Blog)** | AWS blog post: build a multi-agent AWS security assessment system using CrewAI crews, Bedrock Claude/Nova models, and CloudWatch observability. | https://aws.amazon.com/blogs/machine-learning/build-agentic-systems-with-crewai-and-amazon-bedrock/ |
| **AWS Powers Bedrock Agents with CrewAI — Case Study** | CrewAI case study on the AWS partnership: reference blueprints, security audit crew, code modernization flows, and ROI metrics (70% faster execution). | https://www.crewai.com/case-studies/aws-powers-bedrock-agents-with-crewai |
| **GitHub: sample-multi-agent-builder-bedrock-crewai** | Full-stack sample app: CrewAI backend (FastAPI on Fargate) + React UI + CDK infrastructure; uses Claude 3 and Stable Diffusion on Bedrock. | https://github.com/aws-samples/sample-multi-agent-builder-bedrock-crewai |
| **GitHub: aim323 — Build Agents with Bedrock OSS (CrewAI Notebook)** | Jupyter notebook: CrewAI travel destination agent with Bedrock LLM, RAG via Knowledge Bases, and DuckDuckGo search tool. | https://github.com/aws-samples/aim323_build_agents_with_bedrock_oss/blob/main/05_Optional_find_dream_destination_with_crewaI.ipynb |
| **Building Production-Ready Agents with CrewAI + AgentCore (DEV Blog)** | Tutorial: deploy a CrewAI multi-agent crew to Bedrock AgentCore with persistent memory, Docker packaging, and real-time log monitoring. | https://dev.to/aws/building-production-ready-ai-agents-with-crewai-and-amazon-bedrock-agentcore-2g36 |
| **CrewAI GitHub Repository** | Official CrewAI open-source framework repo: framework code, tools, examples, and the crewai-tools package with Bedrock integrations. | https://github.com/crewAIInc/crewAI |

---

## 🔀 Multi-Framework Integration Examples

| Title | Description | URL |
|-------|-------------|-----|
| **GitHub: sample-simple-bedrock-proxy-enterprise** | Enterprise Bedrock proxy supporting LangChain, LangGraph, Strands, and CrewAI through a single API Gateway with Cognito JWT auth, request tracking, and streaming. | https://github.com/aws-samples/sample-simple-bedrock-proxy-enterprise |
| **GitHub: aws-samples (all GenAI samples)** | Search across all AWS sample repositories — hundreds of notebooks and projects for Bedrock, SageMaker, and framework integrations. | https://github.com/aws-samples?q=generative-ai |
| **GitHub: generative-ai-on-aws (Book Repo)** | Full code companion for the O'Reilly book *Generative AI on AWS* — covers LangChain, SageMaker, Bedrock, RAG, fine-tuning, and RLHF. | https://github.com/generative-ai-on-aws/generative-ai-on-aws |
| **3P Agentic Frameworks on Bedrock (aws-samples)** | Multi-framework examples: Strands, CrewAI, LangGraph, and AutoGen running on Bedrock — side-by-side comparisons for security audit and automation crews. | https://github.com/aws-samples/3P-Agentic-Frameworks |
| **AWS AI/ML Landscape 2026 (DEV Community)** | Comprehensive overview of the entire AWS AI stack, including how Bedrock AgentCore works with LangChain, LangGraph, CrewAI, and Strands. | https://dev.to/aws-builders/the-aws-aiml-landscape-in-2026-simplified-17i3 |

---

## 🎓 Courses & Tutorials

| Title | Description | URL |
|-------|-------------|-----|
| **Generative AI on AWS with Bedrock, RAG & LangChain (Udemy)** | Hands-on course: 7+ use cases including chatbots, RAG apps, Bedrock Agents, Amazon Q, and MCP integration. Includes LangChain and Streamlit projects. | https://www.udemy.com/course/amazon-bedrock-aws-generative-ai-beginner-to-advanced/ |
| **Amazon Bedrock Complete Tutorial — Spacelift** | Article-format guide covering Bedrock architecture, pricing, use cases, playground walkthrough, and getting started steps. | https://spacelift.io/blog/what-is-amazon-bedrock |
| **Amazon Bedrock Complete Guide — DataCamp** | In-depth tutorial: choosing foundation models, running inference, building RAG, and best practices for scalable GenAI apps on AWS. | https://www.datacamp.com/tutorial/aws-bedrock |
| **LangGraph Agents Workshop (AWS + DeepLearning.AI)** | Adapted from the official DeepLearning.AI LangGraph course — runs in SageMaker JupyterLab; covers planning, tool use, reflection, and multi-agent communication. | https://github.com/aws-samples/langgraph-agents-with-amazon-bedrock |
| **AWS Machine Learning Blog — Generative AI Tag** | Ongoing series of production-grade tutorials from AWS engineers covering Bedrock, SageMaker, LangChain, CrewAI, Strands, and agentic architectures. | https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/generative-ai/ |
| **AWS Open Source Blog — Agentic AI** | AWS open source blog covering Strands Labs, Strands Agents releases, and emerging patterns in agentic AI development. | https://aws.amazon.com/blogs/opensource/ |
| **Strands Agents Quickstart Guide** | Official Strands quickstart: install the SDK, define your first `@tool`, create an `Agent`, and run it with Bedrock in under 10 lines of Python. | https://strandsagents.com/docs/getting-started/ |
| **CrewAI Quickstart & Cookbooks** | Official getting started guide and end-to-end cookbooks covering crew creation, task design, tool integration, and Bedrock LLM configuration. | https://docs.crewai.com/introduction |

---

## 📦 Key Python Packages

| Package | Purpose | Install |
|---------|---------|---------|
| `boto3` | AWS SDK for Python — core client for Bedrock, SageMaker, S3, and all AWS services | `pip install boto3` |
| `langchain-aws` | Official LangChain integration for Bedrock, SageMaker, Knowledge Bases, and AgentCore tools | `pip install langchain-aws` |
| `langgraph` | Graph-based multi-agent orchestration framework from LangChain | `pip install langgraph` |
| `strands-agents` | AWS model-driven agent SDK with built-in MCP, multi-agent A2A, and Bedrock support | `pip install strands-agents strands-agents-tools` |
| `crewai` | Role-based multi-agent framework with Bedrock LLM support via LiteLLM | `pip install crewai crewai-tools` |
| `sagemaker` | SageMaker Python SDK for JumpStart deployment, training, and endpoint management | `pip install sagemaker` |

---

*Last updated: March 2026 — Resources verified against current AWS documentation and GitHub repositories.*
