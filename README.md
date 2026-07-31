# Bob's Viewport: Agentic Technical Art in Maya

> **Automating 3D graphics pipelines and geometry creation in Autodesk Maya through custom IBM Bob AI agent orchestration.**

---

## Challenge Theme
**Category:** Reimagine Creative Industries with AI (July 2026 Challenge)

## Problem Statement
In modern 3D visual production, technical artists spend hours translating reference photos, pre-visualization concepts, and design notes into initial 3D geometries and stage setups inside Autodesk Maya. Manually creating primitives, adjusting transformations, and configuring scene hierarchies creates friction and slows down the creative flow for film pre-vis and digital set design.

## Solution Description
**Bob's Viewport** bridges generative AI and real-time 3D creation. By establishing a direct communication link between Maya's python environment and a custom IBM Bob persona, technical artists can analyze reference inputs, convert conceptual intent into structured data, and automatically drive geometry creation, lighting placement, and set layouts directly inside the Maya viewport.

## AI Approach & Architecture
1. **Agent Persona (IBM Bob):** Configured as a specialized Technical Artist AI assistant capable of interpreting natural language prompts, scene descriptions, and spatial requirements.
2. **Bridge Layer (`bridge.py`):** Acts as the execution bridge, parsing structured output from the IBM Bob agent persona into native Maya Python (`maya.cmds`) commands.
3. **Environment Setup (`userSetup.py`):** Hooks into Autodesk Maya on startup, creating a persistent socket/listener to receive commands seamlessly within the active viewport session.

```text
+-------------------+      +-------------------+      +---------------------+
|  Reference Input  | ---> |   IBM Bob Agent   | ---> |  bridge.py Engine   |
| & Designer Prompt |      | (Technical Artist)|      | (JSON -> Maya CMDs) |
+-------------------+      +-------------------+      +---------------------+
                                                                 |
                                                                 v
                                                      +---------------------+
                                                      |  Autodesk Maya      |
                                                      |  Viewport Geometry  |
                                                      +---------------------+


How IBM Bob Was Used
IBM Bob served as the core development intelligence and runtime agent backbone:

Code Generation & Workflow Design: IBM Bob was used to architect the communication bridge between standard python execution layers and Maya’s internal interpreter.

Agentic Execution: A custom IBM Bob persona translates high-level creative prompts into structured procedural modeling steps and lighting directives that bridge.py executes directly inside Maya.

Installation & Setup
Clone the Repository:

Bash
git clone [https://github.com/officialjeff9/ibm-bob-maya.git](https://github.com/officialjeff9/ibm-bob-maya.git)
cd ibm-bob-maya
Prerequisites:

Autodesk Maya (2023+ recommended)

Python 3.x installed in your environment

Maya Integration:

Place bridge.py and userSetup.py into your Maya scripts directory:

macOS: ~/Library/Preferences/Autodesk/maya/202X/scripts/

Windows: C:\Users\<Username>\Documents\maya\202X\scripts\

Restart Maya or execute userSetup.py directly inside the Maya Script Editor (Python Tab) to initialize the connection listener.

Acknowledgments
Developed for the July AI Builders Challenge sponsored by IBM SkillsBuild and organized by BeMyApp.
