# ComfyUI-MiniCPM

🖼️ A ComfyUI custom node for MiniCPM vision-language models, enabling high-quality image captioning and analysis.

- MiniCPM-V-4
[![MiniCPM-V-4](example_workflows/MiniCPM-V-4.jpg)](https://github.com/1038lab/ComfyUI-MiniCPM/blob/main/example_workflows/MiniCPM-V-4.json)
- MiniCPM-V-4 GGUF
[![MiniCPM-V-4-GGUF](example_workflows/MiniCPM-V-4-GGUF.jpg)](https://github.com/1038lab/ComfyUI-MiniCPM/blob/main/example_workflows/MiniCPM-V-4-GGUF.json)
- MiniCPM-V-4 Batch Images
[![MiniCPM-V-4_batchImages](example_workflows/MiniCPM-V-4_batchImages.jpg)](https://github.com/1038lab/ComfyUI-MiniCPM/blob/main/example_workflows/MiniCPM-V-4_batchImages.json)
- MiniCPM-V-4 video
[![MiniCPM-V-4_video](example_workflows/MiniCPM-V-4_video.jpg)](https://github.com/1038lab/ComfyUI-MiniCPM/blob/main/example_workflows/MiniCPM-V-4_video.json)

---

## Features

- Supports both **MiniCPM-V-4 (Transformers)** and **MiniCPM-V-4 (GGUF)** models
- Multiple caption types to suit different use cases (Describe, Caption, Analyze, etc.)
- Memory management options to balance VRAM usage and speed
- Auto-downloads model files on first use for easy setup
- Customizable parameters: max tokens, temperature, top-p/k sampling, repetition penalty
- Advanced node with full parameter control
- Legacy node for backward compatibility

---

## Installation

Clone the repo into your ComfyUI custom nodes folder:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/1038lab/comfyui-minicpm.git
```

Install required dependencies:

```bash
ComfyUI\python_embeded\python pip install -r ComfyUI/custom_nodes/comfyui-minicpm/requirements.txt
```

> [!note]
> `llama-cpp-python` CUDA Installation for ComfyUI Portable
> - [llama_cpp_install.md](https://github.com/1038lab/ComfyUI-MiniCPM/blob/main/llama_cpp_install.md)
---

## Supported Models

### Transformers Models
| Model              | Description                            |
| ------------------ | -------------------------------------- |
| MiniCPM-V-4-int4   | 4-bit quantized version, smaller memory footprint |
| MiniCPM-V-4        | Full precision version, higher quality |

https://huggingface.co/openbmb/MiniCPM-V-4

### GGUF Models
| Model              | Description                            |
| ------------------ | -------------------------------------- |
| MiniCPM-V-4 (GGUF) | Latest stable GGUF model, best quality |

https://huggingface.co/openbmb/MiniCPM-V-4-gguf

> The models will be automatically downloaded on first run.
> Manual download and placement into `models/LLM` (transformers) or `models/LLM/GGUF` (GGUF) is also supported.

---

## Available Nodes

### 1. MiniCPM-4-V-Transformers
- Basic transformers-based node with essential parameters
- Supports image and video input
- Memory management options
- Preset prompt types

### 2. MiniCPM-4-V-Transformers Advanced
- Full-featured transformers-based node
- All parameters customizable
- System prompt support
- Advanced video processing options

### 3. MiniCPM-4-V-GGUF
- GGUF-based node with essential parameters
- Optimized for performance

### 4. MiniCPM-4-V-GGUF Advanced
- Full-featured GGUF-based node
- All parameters customizable

### 5. MiniCPM (Legacy)
- Original node for backward compatibility
- Basic functionality

---

## Usage

1. Add the **MiniCPM** node from the `🧪AILab` category in ComfyUI.
2. Connect an image or video input node to the MiniCPM node.
3. Select the model variant (default is MiniCPM-V-4-int4 for transformers).
4. Choose caption type and adjust parameters as needed.
5. Execute your workflow to generate captions or analysis.

---

## Configuration Defaults

```json
{
  "context_window": 4096,
  "gpu_layers": -1,
  "cpu_threads": 4,
  "default_max_tokens": 1024,
  "default_temperature": 0.7,
  "default_top_p": 0.9,
  "default_top_k": 100,
  "default_repetition_penalty": 1.10,
  "default_system_prompt": "You are MiniCPM-V, a helpful, concise and knowledgeable vision-language assistant. Answer directly and stay on task."
}
```

---

## Caption Types

* **Describe:** Describe this image in detail.
* **Caption:** Write a concise caption for this image.
* **Analyze:** Analyze the main elements and scene in this image.
* **Identify:** What objects and subjects do you see in this image?
* **Explain:** Explain what's happening in this image.
* **List:** List the main objects visible in this image.
* **Scene:** Describe the scene and setting of this image.
* **Details:** What are the key details in this image?
* **Summarize:** Summarize the key content of this image in 1-2 sentences.
* **Emotion:** Describe the emotions or mood conveyed by this image.
* **Style:** Describe the artistic or visual style of this image.
* **Location:** Where might this image be taken? Analyze the setting or location.
* **Question:** What question could be asked based on this image?
* **Creative:** Describe this image as if writing the beginning of a short story.

---

## Memory Management Options

* **Keep in Memory:** Model stays loaded for faster subsequent runs
* **Clear After Run:** Model is unloaded after each run to save memory
* **Global Cache:** Model is cached globally and shared between nodes

---

## Tips

* Adjust temperature (0.6–0.8) for balancing creativity and coherence.
* Use top-p (0.9) and top-k (80) sampling for natural output diversity.
* Lower max tokens or precision (bf16/fp16) for faster generation on less powerful GPUs.
* Memory modes help optimize VRAM usage: default, balanced, max savings.
* Transformers models offer better quality but use more memory.
* GGUF models are more memory-efficient but may have slightly lower quality.

---

## License

GPL-3.0 License
