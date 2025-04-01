# EdgeMath-AI-offline-llm-

## Overview

**EdgeMath AI** is a locally hosted AI model designed to solve algebraic equations offline on a Raspberry Pi 4. Utilizing edge computing, it processes math problems in real-time without internet access, making it ideal for resource-constrained environments. This lightweight math solver supports algebra, geometry (area and volume), and linear equations with 2-3 variables, tailored to the Class 10th math syllabus.

- **Duration**: March 2025 – Present  
- **Author**:Amit Kumar Behera ([GitHub])(https://github.com/Akbeherab)  
- **Institution**: Indian Institute of Technology (IIT) Patna  

## Key Features

- **Fully Offline**: No cloud dependency, ensuring privacy and autonomy.
- **Low Latency**: Solves equations within seconds on Raspberry Pi 4.
- **Math Capabilities**:  
  - Basic algebra (linear, quadratic equations)  
  - Area and volume calculations  
  - Linear algebra (solving 2-3 variable equations, e.g., x + y = 10)  
- **Edge Computing**: Optimized for low-end hardware like Raspberry Pi 4.
- **Terminal Interface**: Simple, text-based interaction for ease of use.

## Tools & Technologies

- **Hardware**:  
  - Raspberry Pi 4 (4GB or 8GB RAM recommended)  
  - MicroSD card (32GB+ recommended)  
  - Power supply (5V, 3A)  
- **Software**:  
  - Raspberry Pi OS (64-bit)  
  - Python 3.11+  
  - Llama.cpp (optimized inference engine)  
  - Phi-2.Q4_K_M.gguf (lightweight LLM model)  
  - Python Libraries: `llama-cpp-python`, `numpy`, `sympy`, `uvicorn`  

## System Architecture

EdgeMath AI leverages a quantized LLM (Phi-2) optimized with Llama.cpp:
1. **Model Loading**: Loads `phi-2.Q4_K_M.gguf` into memory on Raspberry Pi.
2. **Input Processing**: Parses user math queries via a terminal interface.
3. **Inference**: Uses Llama.cpp to solve equations step-by-step.
4. **Output**: Displays solutions with intermediate steps in the terminal.


## System Requirements

- **Hardware**: Raspberry Pi 4 (4GB or 8GB), MicroSD card (32GB+), 5V/3A power supply  
- **Software**: Raspberry Pi OS (64-bit), Python 3.11+, Llama.cpp, Phi-2.Q4_K_M.gguf  

## Installation & Setup

### Step 1: Update Raspberry Pi
```bash
sudo apt update && sudo apt upgrade -y
## Installation
###  Install Dependencies
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip -y
pip3 install llama-cpp-python sympy numpy
```

###  Download AI Model (Quantized)
```bash
wget https://huggingface.co/TheBloke/Phi-2-GGUF/resolve/main/phi-2.Q4_K_M.gguf
```

### Run the math_Solve.py

## Performance
### Results
| Metric | Value |
|--------|--------|
| **Inference Time** | ~10-20s per query (varies by complexity) |
| **Total Processing Time** | ~80-100s for 200 tokens |
| **Power Consumption** | ~30% lower compared to unoptimized models |
| **Accuracy** | Reliable for Class 10th-level math (algebra, geometry, linear equations) |

## Potential Applications
- **Education:** Offline math tutoring in remote schools.
- **Defense:** Portable computation tool for field engineers.
- **Rural Development:** Math solver for areas without internet.

## Future Enhancements
- Add **geometry & trigonometry** problem-solving.
- Integrate a **web-based UI** using Flask/FastAPI.
- Optimize response time with **tensor acceleration**.
- Extend support for **Raspberry Pi 3 & other low-end devices and jetsonano NVIDIA**.

## Contributing
Contributions are welcome! **Fork the repo, make changes, and submit a pull request.** Open an issue for major updates.

---
