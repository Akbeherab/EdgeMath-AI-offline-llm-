
from llama_cpp import Llama

# Load the model
llm = Llama(
    model_path="model/phi-2.Q4_K_M.gguf",  # Path to AI model
    n_ctx=512,       # Max memory context
    n_batch=256,     # Speed optimization
    n_threads=4,     # Use all CPU cores
    n_gpu_layers=0   # No GPU (Raspberry Pi)
)

print("\n🤖 **AI Math Solver** (Type 'exit' to quit)")
while True:
    user_input = input("\nYou: ")
    if user_input.lower() == "exit":
        print("👋 Exiting... Have a great day!")
        break
    
    # Generate response with step-by-step solution
    response = llm(
        f"Solve this math problem step by step: {user_input}",
        max_tokens=200
    )
    print(f"\n🤖 AI: {response['choices'][0]['text'].strip()}")
