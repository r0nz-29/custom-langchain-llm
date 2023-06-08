# Custom GPT  
This is an experiment to create a gpt like model using [LangChain Agents](https://python.langchain.com/en/latest/modules/agents.html) that can carry-out generic conversations with the user. Additionally, the model can trigger an API request to [fakestoreapi.com](https://fakestoreapi.com/products) to retrieve some dummy JSON, if the input prompt demands it.  
client repo: [customgpt-client](https://github.com/r0nz-29/customgpt-client)

## Demo  
### Generic Interaction  
![generic-gpt](https://github.com/r0nz-29/custom-langchain-llm/assets/76162540/06872784-6b33-4352-b78d-3aaf86ce6eb2)

### API call based on input prompt  
Since `return_direct=True`, the agent returns the JSON response as-is. We can further extend it to process the JSON and return a summary to the user  

![api-call-gpt](https://github.com/r0nz-29/custom-langchain-llm/assets/76162540/01d630eb-4d68-4eed-a34f-f2884fe47add)

### References  
https://python.langchain.com/en/latest/modules/agents.html  
