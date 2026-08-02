# Bayesian Probability

### Solving Every Problem Both Ways

**Nik Bear Brown**

*Bear Brown LLC*

---

## Copyright

Copyright © 2026 Nik Bear Brown. All rights reserved.

Published by Bear Brown LLC.

No part of this publication may be reproduced, distributed, or transmitted in any form or by any means without the prior written permission of the publisher, except in the case of brief quotations in critical reviews and certain other noncommercial uses permitted by copyright law.

ISBN: [INSERT ISBN]

First edition: 2026

---

## Dedication

*For the reader who would rather know why a method works than be told which one to use.*

---

## Preface

Most people learn statistics inside a single paradigm. They are handed p-values, confidence intervals, and significance tests as if these were simply *statistics* — the way arithmetic is arithmetic — and they never see the questions that machinery cannot answer. They leave a first course able to run a test and unable to say what the test refused to tell them.

This book takes a different path. It solves every problem twice: once the frequentist way, once the Bayesian way, set side by side on the same data. Not to crown a winner — the book argues there isn't one — but to make the choice visible. By the end, the answer to "frequentist or Bayesian?" is never reflexive. It depends on what the decision-maker needs, whether prior information exists and can be defended, how much data there is, and who will read the result. That judgment, not either toolkit, is the skill worth building.

The book is also written for the moment we are in. Implementation runs through AI-generated code throughout, taught explicitly in Chapter 2, so the reader spends effort on statistical reasoning and on *verifying* output rather than on coding from scratch. This is a deliberate division of labor — the machine executes, the human decides what to ask and whether the answer is right. That division is the spine of the Irreducibly Human series this book belongs to, and it is set out in full in the appendix, *The Fundamental Themes*.

A note on honesty: this is a working draft. Where a claim depends on a source still being verified, or where a debate in the field is genuinely unsettled, the text says so rather than papering over it. That is the habit the book is trying to teach.

---

## How This Book Fits Together

The book runs in three acts after a short prerequisites chapter (Chapter 0). Act One (Chapters 1–4) establishes that the two paradigms answer different questions and teaches the implementation skill the rest of the book leans on. Act Two (Chapters 5–9) builds the methods where the choice carries real consequences — regression, model comparison, priors made explicit, sparse data, and hierarchical models. Act Three (Chapters 10–13) applies the toolkit to time, decision, and a real dataset, and closes with a framework for choosing.

This book is built to integrate with **Medhavy** (also **Medhavi**; from Sanskrit मेधावी, "intelligent"), an AI-powered intelligent textbook system, where chapters can become adaptive practice — hints, quizzes, worked examples, and feedback. Even there, the learning target remains the human's judgment.
