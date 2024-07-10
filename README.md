# 🕵️‍♂️ sherlock model eval
#### context: [x/twitter](https://x.com/dwarkesh_sp/status/1773437856448680049)

### model selection
selected top five unique model architectures as of 7/8/24 from [lmsys arena](https://arena.lmsys.org/) to evaluate.

### riddle generation
each model was tasked with generating one riddle in the sherlock style (total of five riddles). models were limited to 2048 output tokens wherever possible.

### answering riddles
each model was asked to solve the riddles in two separate attempts (for a total of ten attempts per model). models were asked to begin their response with the name of the culprit and the weapon used.

### results

| model             | fully correct (%) | identified culprit correctly (%) | identified weapon correctly (%) |
| ----------------- | ----------------- | -------------------------------- | ------------------------------- |
| gpt-4o            | 
| claude-3.5-sonnet |
| gpt-4-turbo       |
| gemini-1.5-pro   |
| llama-3-70b       |