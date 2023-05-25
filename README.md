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

What if we could automatically find out the intent of the user and responding likewise at earliest thus keeping the user sticking around the app? A win-win situation for both the user and the app creator.

Intent classification is the task of classifying the text into one of the many intents (multiclass-classification).

> <b>Aim of the project is to perform multiclass intent classification (and also subtask: topic modelling).</b>

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- PROJECT SUMMARY -->
## Summary

The <a href="Data">data file</a> contains approximately 15,000 data points. These data points are divided into three datasets: training, testing, and validation, and saved in three separate CSV files. <a href="1_data_analysis.ipynb">Data analysis</a> is performed on the training dataset. Data consists of two columns: text and intent. "Intent" is the target column, which contains 7 classes with an approximately equal distribution. It is also found that the text ranges from 10 to 125 characters approximately, and the range of words in the text ranges from 2 to 25. NER tag that was observed most across the documents: cardinal. There are also numerous "Date", "Person", and "GPE" - NER tags present across document. Further, we also found out the NER tags that dominated per class. <a href="2_topic_modelling.ipynb">Topic modelling</a> is performed using LDA, and results are plotted using pyLDAvis.

Utilizing MLP, LSTM, and BERT (along with various embedding algorithms), intent classification is carried out and comparasion analysis is completed. Summarizing results:

1.  <a href="3_mlp_intEncoding.ipynb"><b>MLP with Integer Encoding</b></a>

    * Model 1.1 :

    <div align='center'>
    
    ```
    INPUT => EMBEDDING (int encoding) => FLATTEN => FC => RELU => DO => FC => SOFTMAX
    ```
    
    </div>

     * Model 1.2 :
    <div align='center'>
    
    ```
      INPUT => EMBEDDING (int encoding) => GAP1D => FC => RELU => DO => FC => SOFTMAX
    ```
    
    </div>

Model 1.1's flatten layer leads to more trainable parameters compared to model 1.2 that uses GlobalAveragePooling1D. Better performance is achieved by model 1.2.

2.   <a href="4_mlp_gloveEmbedding.ipynb"><b>MLP with Glove Embedding</b></a>
    
      * Model 2.1 :
      <div align='center'>
      
      ```
      INPUT => EMBEDDING (Glove Embedding) => GMP1D => FC => RELU => DO => FC => RELU => DO => FC => SOFTMAX
      ```
      
      </div>
    
    
      * Model 2.2 :
      <div align='center'>
    
      ```
      INPUT => EMBEDDING (Glove Embedding) => GAP1D => FC => RELU => DO => FC => RELU => DO => FC => SOFTMAX
      ```
      
      </div>
    
Model 2.2 (uses GlobalAveragePool1D) is performing better than model 2.1 (uses GlobalMaxPool1D) in fewer epochs and in less wall time.

3.   <a href="5_lstm.ipynb"><b>LSTM</b></a>

      * Model 3.1 (Vanilla LSTM) :
      <div align='center'>
      
      ```
      INPUT => EMBEDDING (int encoding) => LSTM => FC => RELU => DO => FC => SOFTMAX
      ```
      
      </div>
    
    
      * Model 3.2 (BidirectionalLSTM) :
      
      <div align='center'>
    
      ```
      INPUT => EMBEDDING (int encoding) => BiLSTM => FC => RELU => DO => FC => SOFTMAX
      ```
    
      </div>

   
      * Model 3.3 (Stacked LSTM) :
      
      <div align='center'>

      
      ```
      INPUT => EMBEDDING (int encoding) => LSTM => LSTM => FC => RELU => DO => FC => SOFTMAX
      ```
      
      </div>

Model 3.3 (stacked LSTM) <b>with fewer parameters</b> can achieve approximately similar or even better performance compared to model 3.1 (vanilla LSTM), but requires more training epochs to achieve the same. Model 3.2 (BidirectionalLSTM) achieved better performance compared to other two models.

4. <a href="6_smallBERT.ipynb"><b>Small BERT</b></a> 

The model quickly overfits the data. Most likely because the data isn't difficult or sophisticated for a BERT-like model to learn.

Following table summarizes the results:

<div align="center">

Model No. | Trainable Params | Epochs| Train Acc | Train Loss | Valid Acc | Valid Loss | Test Acc | Test Loss | Wall Time
:----------------: | :----------------: | :----------------: | :----------------: | :----------------: | :----------------: | :----------------: | :----------------: | :----------------: | :----------------:
1.1 | 83,975 | 10 | 0.9690 | 0.1017 | 0.9675 | 0.1363 | 0.9671 | 0.1276 | 9.2s
1.2 | 76,039 | 15 | 0.9885 | 0.0437 | 0.9712 | 0.1214 | 0.9710 | 0.1055 | 12.9s
2.1 | 8,775 | 50 | 0.9604 | 0.1161 | 0.9420 | 0.1941 | 0.9406 | 0.2205 | 36.8s
2.2 | 8,775 | 30 | 0.9661 | 0.1063 | 0.9564 | 0.1215 | 0.9562 | 0.1206 | 22.1s
3.1 | 76,695 | 20 | 0.9677 | 0.0901 | 0.9658 | 0.3097 | 0.9617 | 0.3599 | 5m31s
3.2 | 77,799 | 20 | 0.9654 | 0.1004 | 0.9672 | 0.1602 | 0.9632 | 0.2153 | 7m29s
3.3 | 76,159 | 25 | 0.9549 | 0.1240 | 0.9447 | 0.3509 | 0.9499 | 0.3423 | 11m29s
4 | - | 5 | 0.9885 | 0.0437 | 0.9712 | 0.1214 | 0.9757 | 0.1063 | 2m33s

</div>

Overall, model 4, or the BERT model, provides the best performance. However, it has quite broad requirements. With fewer parameters, Model 1.2 produces performance that is nearly identical. 

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- Project Directory Structure -->
## Directory Structure
```
├── Data Files                            # Data files              
    └── ...         
├── Models                                # Saved models              
    └── ...         
├── Other Files                           # Miscellaneous files
    └── ...
├── 1_data_analysis                       # Data Analysis file
├── 2_topic_modelling                     # Topic Modelling file
├── 3_mlp_intEncoding                     # MLP Classifier (with int encoding) file
├── 4_mlp_gloveEmbedding                  # MLP Classifier (with glove embedding) file
├── 5_lstm                                # LSTM Classifier (vanilla, stacked, bidirectional) file
├── 6_smallBert                           # smallBert Classifier file
```

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- Tools and Libraries used -->
## Languge and Libraries

*   Language: <b>Python</b>
*   Libraries: <b>Tensorflow</b>, <b>Keras</b>, <b>Tensorflow-Hub</b>, <b>Scikit-Learn</b>, <b>Gensim</b>, <b>NLTK</b>, <b>Spacy</b>, <b>PyLDAviz</b>, <b>Re</b>, <b>WordCloud</b>, <b>Matplotlib</b>, <b>Seaborn</b>, <b>Numpy</b>, <b>Pandas</b>.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- Final Notes -->
## Final Notes

Notebooks can be run directly on google colab (make sure to upload required .py files in working directory if required).

The codebase has been meticulously documented, incorporating comprehensive docstrings and comments. Please review these annotations, as they provide valuable insights into the functionality and operation of the code. 

<p align="right">(<a href="#top">back to top</a>)</p>
