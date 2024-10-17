## 4.4 Precision and Recall

## Notes

**Precision** tell us the fraction of positive predictions that are correct. It takes into account only the **positive class** (TP and FP - second column of the confusion matrix), as is stated in the following formula:


$$P = \cfrac{TP}{TP + FP}$$


**Recall** measures the fraction of correctly identified postive instances. It considers parts of the **postive and negative classes** (TP and FN - second row of confusion table). The formula of this metric is presented below: 


$$R = \cfrac{TP}{TP + FN}$$


 In this problem, the precision and recall values were 67% and 54% respectively. So, these measures reflect some errors of our model that accuracy did not notice due to the **class imbalance**. 


**MNEMONICS:**

- Precision : From the `pre`dicted positives, how many we predicted right. See how the word `pre`cision is similar to the word `pre`diction? 

- Recall : From the `real` positives, how many we predicted right. See how the word `re`c`al`l is similar to the word `real`?