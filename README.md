<!-- PROJECT NAME -->

<br />
<div align="center">
  <h3 align="center">Intentium</h3>
  <p align="center">
    Multiclass Classification | Topic Modelling | Model Serving
  </p>
</div>

<!-- ABOUT PROJECT -->
## What Is It?
<div align="center">

    HARRY: Ron, please play 'Tere Naina'...
    RON: Ummm.. Okay.. Playing 'Tere Naina'...
    
</div>

Question is - how did Ron completed the task here? Roughly, he first found the intent of the task, i.e., what needs to be done? Here, intent was 'PlayMusic'. So, Ron thus started a music app and played the above mentioned song.

Extending this concept little further; what if we could automatically find out the intent of the user and responding likewise at earliest thus keeping the user sticking around the app? A win-win situation for both the user and the app creator.

Intent classification is the task of classifying the text into one of the many intents (multiclass-classification).

> <b>Aim of the project is to perform multiclass intent classification (and also subtask: topic modelling).</b>

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- PROJECT SUMMARY -->
## Summary

Summarizing results:

<div align="center">

Model Architecture | Accuracy
:----------------: | :----------------:
 

</div>

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- Project Directory Structure -->
## Directory Structure
```
├── Data Files                            # Data files              
    └── ...         
├── Other Files                           # Miscellaneous files
    └── ...
├── 1_data_analysis                       # Data Analysis
├── 2_topic_modelling                     # Topic Modelling
├── 3_mlp_intEncoding                     # MLP Classifier (with int encoding)
├── 4_mlp_gloveEmbedding                  # MLP Classifier (with glove embedding)
├── 5_lstm                                # LSTM Classifier (vanilla, stacked, bidirectional)
├── 6_smallBert                           # smallBert Classifier
```

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- Tools and Libraries used -->
## Languge and Libraries

*   Language: Python
*   Libraries: Tensorflow, Keras, Tensorflow-Hub, Scikit-Learn, Gensim, NLTK, Spacy, PyLDAviz, Re, WordCloud, Matplotlib, Seaborn, Numpy, Pandas, String, OS.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- Final Notes -->
## Final Notes

Notebooks can be run directly on google colab (make sure to upload required .py files in working directory if required).

<p align="right">(<a href="#top">back to top</a>)</p>
