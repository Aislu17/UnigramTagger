# UnigramTagger
In this project I have built my unigram morphological analyzer (Russian) from scratch
The UnigramMorphAnalyzer() class has the following methods:
1. train(): reads words from the tagged corpus and accumulates POS-statistics according to word endings (4, 3, 2, 1 last characters)
2. predict(): outputs a list of probabilities of different POS for a given token
3. save(): saves the model with the pickle library
4. load(): loads the model

5. eval(): outputs the analyzer's accuracy on open corpora test data (the dataset is split into train/test data beforehand)
When UnigramMorphAnalyzer['ending'] is called, it prints the particle statistics for the given ending