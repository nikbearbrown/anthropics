What Is Reflection Training?

To change what a model thinks, train what it says. That is reflection training: take real partial transcripts, cut them mid-task, append one question — 'what considerations apply right now?' — and fine-tune on strong answers. The counterfactual part gives it its name: the model is trained on reflections about moments it never finished living.

The results, on one model: fabrication (making things up under pressure) fell 0.25 → 0.07; deception (carrying out a deceptive directive) fell 0.38 → 0.05. And it wins the honest way — by admitting what it doesn't know and telling the user when it was asked to deceive them. Not better hiding; more telling.

Two checks make it science. The mechanism check: after training, ethics and reflection tokens show up in the model's internal workspace during the task, before any question is asked — the reflex installed exactly where the theory predicted. The ablation: delete those directions and the deception score claws back to 0.23. The honest label: two in-house benchmarks, one model — a demonstration, not a deployment record, but the rare alignment result a theory predicted in advance.

Based on Anthropic's workspace research; distilled from our series on the paper.

Chapters:
0:00 What is reflection training?
0:18 Part I — The Idea
0:55 Part II — The Method
1:16 The results
1:45 The proof it's real
2:20 Verdict
2:40 Your turn

Every factual claim in this video was checked against primary sources before rendering.

#AI #Alignment #Anthropic #Claude #Interpretability #MachineLearning

youtube.com/@NikBearBrown