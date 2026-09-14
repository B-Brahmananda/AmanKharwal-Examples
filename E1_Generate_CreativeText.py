from transformers import pipeline
generator = pipeline("text-generation", model="distilgpt2")
prompt = "the AI Agnet quickly analysed the data stream, and its core decision was to"
output = generator(
    prompt,
    max_length=100,
    num_return_sequences=1,
    do_sample=True,
    top_k=50,
    top_p=0.95,
    temperature=0.75, 
    repetition_penalty=1.2,
    no_repeat_ngram_size=3   
)
print("prompt")
print(prompt)
print("\nGenerated Output")
print(output[0]['generated_text'])