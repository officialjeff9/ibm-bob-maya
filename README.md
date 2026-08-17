Viewport Bridge: AI-to-Maya Pipeline
Automating 3D graphics pipelines, asset organization, and geometry creation in Autodesk Maya through local AI agent orchestration, custom IBM Bob personas, and Python bridge integration.

Overview
In modern 3D visual production, technical artists spend hours translating reference photos, pre-visualization concepts, and design notes into initial 3D geometries and stage setups inside Autodesk Maya. Manually creating primitives, adjusting transformations, and configuring scene hierarchies creates friction and slows down the creative flow for film pre-vis and digital set design.

Solution Description
Viewport Bridge connects modern AI workflows, MCP servers, and a custom IBM Bob persona directly into Autodesk Maya. By establishing a direct communication link between Maya's Python environment and the local IBM Bob assistant, technical artists can analyze reference inputs, convert conceptual intent into structured data, and automatically drive geometry creation, lighting placement, and set layouts directly inside the Maya viewport.

Architecture & Workflow
- AI Agent / Client (IBM Bob): Configured as a specialized Technical Artist AI assistant powered by a custom IBM Bob persona capable of interpreting natural language prompts, scene descriptions, and spatial requirements.
- Bridge Layer (bridge.py): Acts as the execution bridge, parsing structured output from the IBM Bob persona into native Maya Python (maya.cmds) commands.
- Environment Setup (userSetup.py & File Watcher): Hooks into Autodesk Maya on startup, creating a persistent socket/listener or file-watching loop to receive commands seamlessly within the active viewport session.

Plaintext
+-------------------+      +-------------------+      +---------------------+
|  Reference Input  | ---> | IBM Bob AI Agent  | ---> |  bridge.py Engine   |
| & Designer Prompt |      | (Technical Artist)|      | (JSON -> Maya CMDs) |
+-------------------+      +-------------------+      +---------------------+
                                                                 |
                                                                 v
                                                      +---------------------+
                                                      |  Autodesk Maya      |
                                                      |  Viewport Geometry  |
                                                      +---------------------+

Core Capabilities
- Code Generation & Workflow Design: Automatically architectures the communication bridge between standard Python execution layers and Maya’s internal interpreter.
- Agentic Execution via IBM Bob: Translates high-level creative prompts into structured procedural modeling steps and lighting directives that bridge.py executes directly inside Maya using the custom IBM Bob persona.
- Background File Watching: Listens continuously for incoming script updates, enabling a hands-free feedback loop.

Installation & Setup
1. Clone the Repository
Bash
git clone https://github.com/officialjeff9/viewport-bridge.git
cd viewport-bridge

2. Prerequisites
- Autodesk Maya (2023+ recommended)
- Python 3.x installed in your local environment

3. Maya Integration
- Copy the setup files into your Maya scripts directory (~/Documents/maya/[version]/scripts/ or your custom script path).
- Configure your userSetup.py to initialize the listener/socket upon startup.
