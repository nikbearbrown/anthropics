What Is the J-Space?

Somewhere in the middle of a language model there is a thin slice of activity where the model holds what it is thinking about — before it says a word. Anthropic found it with one instrument: for every word in the vocabulary, the gradient that would push the model to say it. One vector per word; a dictionary of directions. Project the model's live activations onto that dictionary and you get a ranking — what this layer, right now, is most ABOUT.

The space those directions span is the J-space: a wide middle band (roughly layers 38–92 in one production model), about twenty-five sparse slots carrying under ten percent of everything the model computes. It stores ideas, not items — read it an eighty-word animal list and it holds the CATEGORY, which predicts the rest. And it is causally real: swap a held concept (spider → ant) and the model's answer follows; delete the space and flexible reasoning collapses while grammar keeps flowing.

The honest label, in the paper's own print: the lens reads one token at a time ('blackmail' registers as 'black'), every reading so far comes from one vendor's models, and a forward pass has no recurrence. Real, tested, young.

Based on Anthropic's workspace research; distilled from our six-part series on the paper.

Chapters:
0:00 What is the J-Space?
0:15 Part I — The Instrument
1:04 Part II — The Space
2:00 The proof it's real
2:34 The honest label
2:52 Verdict
3:09 Your turn

Every factual claim in this video was checked against primary sources before rendering.

#AI #Interpretability #Anthropic #Claude #NeuralNetworks #MachineLearning

youtube.com/@NikBearBrown