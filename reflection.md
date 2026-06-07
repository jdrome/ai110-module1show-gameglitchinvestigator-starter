# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  - Choosing the right answer yielded a congratulations message
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  1. In hard mode, the range is listed as being from 1-50, but it should be from 1-100
  2. All difficulties are the same difficulty (ranging from 1-100).

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior       | Actual Behavior       | Console Output / Error |
|-------|-------------------------|-----------------------|------------------------|
| No Input | New Game starts new game | New Game does nothing| No Error|
| 50 (when answer is 40 | Hint: go lower | Hint: go higher | No Error |
| No Input | Hard: 1-100 | Hard: 1-50 | No Error|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - I used Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - The AI pointed out the message saying "guess a number between 1 and 100" was hard coded, which was wrong. The AI pointed me to where the issue was, and I was able to resolve it.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - The AI's suggestions were correct due to the scope of the issues being relatively small.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - Running the app and seeing the changes go through verified the fixes
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  - One pytest was checking that the difficulty and ranges matched, and they did. So easy matches with 1,20. Normal matches with 1,50. Hard matches with 1,100. 
- Did AI help you design or understand any tests? How?
  - In this case, the AI created the tests in the test directory.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  - Steamlit reruns the entire app when ever an event occurs. So if a user presses a button, for example, then the whole session is restarted. 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  - I want to keep asking the AI clarifying questions so that I understand the code base and the changes. For example, I asked what "st" was, and it pointed out that it was, of course, and alias for streamlit. 
- What is one thing you would do differently next time you work with AI on a coding task?
  - I would ask the AI to explain to me some code a bit more. There were times when I could look at the code and clearly see what the issue was, but the issue's scope can be larger than I anticipate, so clarifying with AI is probably a good idea.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - AI generated code can be really fast and it can speed up production, but it can also encourage bad habits in the long term if you are not practicing discipline in real time.
