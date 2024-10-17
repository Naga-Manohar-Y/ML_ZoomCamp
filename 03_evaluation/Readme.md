
## 4.2 Accuracy and dummy model


## Notes

**Accuracy** measures the fraction of correct predictions. Specifically, it is the number of correct predictions divided by the total number of predictions. 

We can change the **decision threshold**, it should not be always 0.5. But, in this particular problem, the best decision cutoff, associated with the hightest accuracy (80%), was indeed 0.5. 

Note that if we build a **dummy model** in which the decision cutoff is 1, so the algorithm predicts that no clients will churn, the accuracy would be 73%. Thus, we can see that the improvement of the original model with respect to the dummy model is not as high as we would expect. 

Therefore, in this problem accuracy can not tell us how good is the model because the dataset is **unbalanced**, which means that there are more instances from one category than the other. This is also known as **class imbalance**. 

**Classes and methods:**

* `np.linspace(x,y,z)` - returns a numpy array starting at `x` until `y` with `z` evenly spaced samples 
* `Counter(x)` - collection class that counts the number of instances that satisfy the `x` condition
* `accuracy_score(x, y)` - sklearn.metrics class for calculating the accuracy of a model, given a predicted `x` dataset and a target `y` dataset.



## 4.3 Confusion table

## Notes

Confusion table is a way of measuring different types of errors and correct decisions that binary classifiers can make. Considering this information, it is possible to evaluate the quality of the model by different strategies.

When comes to a prediction of an LR model, each falls into one of four different categories:

* Prediction is that the customer WILL churn. This is known as the **Positive class**
    * And Customer actually churned - Known as a **True Positive (TP)**
    * But Customer actually did not churn - Known as a **False Positive (FP)**
* Prediction is that the customer WILL NOT churn' - This is known as the **Negative class**
    * Customer did not churn - **True Negative (TN)**
    * Customer churned - **False Negative (FN)**

'Confusion Table' is a way to summarize the above results in a tabular format, as shown below: 

<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="2"><b>Predictions</b></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Actual</b></td>
      <td><b>Negative</b></td>
      <td><b>Positive</b></td>
    </tr>
   <tr>
      <td><b>Negative</b></td>
      <td>TN</td>
      <td>FP</td>
    </tr>
    <tr>
      <td><b>Positive</b></td>
      <td>FN</td>
      <td>TP</td>
    </tr>
  </tbody>
</table>


The **accuracy** corresponds to the sum of TN and TP divided by the total of observations. 


