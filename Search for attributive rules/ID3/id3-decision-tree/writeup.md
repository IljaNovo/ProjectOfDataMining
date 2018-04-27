1. How did you handle missing attributes in examples?

    We left missing attributes alone (i.e. left them as `None`).

    - For nominal variables, this amounts to treating `None` as its own attribute value, which makes sense because it's possible the missing nature of the value is itself meaningful.
    - For numerical variables, this amounts to always classifying missing values as below the splitting threshold, since Python will always evaluate `None` < `i` for any integer `i` .

    We decided to handle missing attributes this way because it increased our accuracy significantly over the original, more involved implementation, which was to assign the mode (for nominal) or mean (for numerical) attribute value among examples sorted to the current node.

2. Apply your algorithm to the training set, without pruning. Print out a Boolean formula in disjunctive normal form that corresponds to the unpruned tree learned from the training set. For the DNF assume that group label "1" refers to the positive examples. NOTE: if you find your tree is cumbersome to print in full, you may restrict your print-out to only 16 leaf nodes.

    ```
    
    ( oppnuminjured < 3.0 AND numinjured < 2.0 AND oppnuminjured < 2.0 AND numinjured < 1.0 AND numinjured < -1.0 AND oppwinningpercent < 0.361665214232 AND winpercent < 0.889456415392 AND winpercent < 0.448454638411 AND opprundifferential < 102.0 AND temperature < 77.6698869602 AND oppnuminjured < -2.0 AND dayssincegame >= 1.0 AND winpercent < 0.363909225157 AND oppwinningpercent < 0.341659335759 )
    OR
    ( oppnuminjured < 3.0 AND numinjured < 2.0 AND oppnuminjured < 2.0 AND numinjured < 1.0 AND numinjured < -1.0 AND oppwinningpercent < 0.361665214232 AND winpercent < 0.889456415392 AND winpercent < 0.448454638411 AND opprundifferential < 102.0 AND temperature < 77.6698869602 AND oppnuminjured < -2.0 AND dayssincegame >= 1.0 AND winpercent >= 0.363909225157 AND winpercent < 0.442079863237 AND rundifferential >= 100.0 )
    OR
    ( oppnuminjured < 3.0 AND numinjured < 2.0 AND oppnuminjured < 2.0 AND numinjured < 1.0 AND numinjured < -1.0 AND oppwinningpercent < 0.361665214232 AND winpercent < 0.889456415392 AND winpercent < 0.448454638411 AND opprundifferential < 102.0 AND temperature < 77.6698869602 AND oppnuminjured < -2.0 AND dayssincegame >= 1.0 AND winpercent >= 0.363909225157 AND winpercent >= 0.442079863237 )
    OR
    ( oppnuminjured < 3.0 AND numinjured < 2.0 AND oppnuminjured < 2.0 AND numinjured < 1.0 AND numinjured < -1.0 AND oppwinningpercent < 0.361665214232 AND winpercent < 0.889456415392 AND winpercent < 0.448454638411 AND opprundifferential < 102.0 AND temperature < 77.6698869602 AND oppnuminjured >= -2.0 AND oppwinningpercent < 0.345258664161 AND winpercent < 0.23209489273 AND opprundifferential < 74.0 AND rundifferential < 32.0 AND rundifferential < 30.0 )
    OR
    ( oppnuminjured < 3.0 AND numinjured < 2.0 AND oppnuminjured < 2.0 AND numinjured < 1.0 AND numinjured < -1.0 AND oppwinningpercent < 0.361665214232 AND winpercent < 0.889456415392 AND winpercent < 0.448454638411 AND opprundifferential < 102.0 AND temperature < 77.6698869602 AND oppnuminjured >= -2.0 AND oppwinningpercent < 0.345258664161 AND winpercent < 0.23209489273 AND opprundifferential < 74.0 AND rundifferential >= 32.0 )
    OR
    ( oppnuminjured < 3.0 AND numinjured < 2.0 AND oppnuminjured < 2.0 AND numinjured < 1.0 AND numinjured < -1.0 AND oppwinningpercent < 0.361665214232 AND winpercent < 0.889456415392 AND winpercent < 0.448454638411 AND opprundifferential < 102.0 AND temperature < 77.6698869602 AND oppnuminjured >= -2.0 AND oppwinningpercent < 0.345258664161 AND winpercent < 0.23209489273 AND opprundifferential >= 74.0 AND winpercent >= 0.110717487512 )
    OR
    ( oppnuminjured < 3.0 AND numinjured < 2.0 AND oppnuminjured < 2.0 AND numinjured < 1.0 AND numinjured < -1.0 AND oppwinningpercent < 0.361665214232 AND winpercent < 0.889456415392 AND winpercent < 0.448454638411 AND opprundifferential < 102.0 AND temperature < 77.6698869602 AND oppnuminjured >= -2.0 AND oppwinningpercent < 0.345258664161 AND winpercent >= 0.23209489273 AND opprundifferential < 75.0 AND oppwinningpercent < 0.344227511991 AND oppwinningpercent < 0.338446357558 AND oppwinningpercent < 0.330499374229 AND winpercent < 0.446802642009 AND oppdayssincegame < 1.0 )
    OR
    ( oppnuminjured < 3.0 AND numinjured < 2.0 AND oppnuminjured < 2.0 AND numinjured < 1.0 AND numinjured < -1.0 AND oppwinningpercent < 0.361665214232 AND winpercent < 0.889456415392 AND winpercent < 0.448454638411 AND opprundifferential < 102.0 AND temperature < 77.6698869602 AND oppnuminjured >= -2.0 AND oppwinningpercent < 0.345258664161 AND winpercent >= 0.23209489273 AND opprundifferential < 75.0 AND oppwinningpercent < 0.344227511991 AND oppwinningpercent < 0.338446357558 AND oppwinningpercent < 0.330499374229 AND winpercent < 0.446802642009 AND oppdayssincegame >= 1.0 AND rundifferential < 86.0 )
    OR
    ( oppnuminjured < 3.0 AND numinjured < 2.0 AND oppnuminjured < 2.0 AND numinjured < 1.0 AND numinjured < -1.0 AND oppwinningpercent < 0.361665214232 AND winpercent < 0.889456415392 AND winpercent < 0.448454638411 AND opprundifferential < 102.0 AND temperature < 77.6698869602 AND oppnuminjured >= -2.0 AND oppwinningpercent < 0.345258664161 AND winpercent >= 0.23209489273 AND opprundifferential < 75.0 AND oppwinningpercent < 0.344227511991 AND oppwinningpercent < 0.338446357558 AND oppwinningpercent < 0.330499374229 AND winpercent < 0.446802642009 AND oppdayssincegame >= 1.0 AND rundifferential >= 86.0 )
    OR
    ( oppnuminjured < 3.0 AND numinjured < 2.0 AND oppnuminjured < 2.0 AND numinjured < 1.0 AND numinjured < -1.0 AND oppwinningpercent < 0.361665214232 AND winpercent < 0.889456415392 AND winpercent < 0.448454638411 AND opprundifferential < 102.0 AND temperature < 77.6698869602 AND oppnuminjured >= -2.0 AND oppwinningpercent < 0.345258664161 AND winpercent >= 0.23209489273 AND opprundifferential < 75.0 AND oppwinningpercent < 0.344227511991 AND oppwinningpercent < 0.338446357558 AND oppwinningpercent < 0.330499374229 AND winpercent >= 0.446802642009 )
    OR
    ( oppnuminjured < 3.0 AND numinjured < 2.0 AND oppnuminjured < 2.0 AND numinjured < 1.0 AND numinjured < -1.0 AND oppwinningpercent < 0.361665214232 AND winpercent < 0.889456415392 AND winpercent < 0.448454638411 AND opprundifferential < 102.0 AND temperature < 77.6698869602 AND oppnuminjured >= -2.0 AND oppwinningpercent < 0.345258664161 AND winpercent >= 0.23209489273 AND opprundifferential < 75.0 AND oppwinningpercent < 0.344227511991 AND oppwinningpercent < 0.338446357558 AND oppwinningpercent >= 0.330499374229 )
    OR
    ( oppnuminjured < 3.0 AND numinjured < 2.0 AND oppnuminjured < 2.0 AND numinjured < 1.0 AND numinjured < -1.0 AND oppwinningpercent < 0.361665214232 AND winpercent < 0.889456415392 AND winpercent < 0.448454638411 AND opprundifferential < 102.0 AND temperature < 77.6698869602 AND oppnuminjured >= -2.0 AND oppwinningpercent < 0.345258664161 AND winpercent >= 0.23209489273 AND opprundifferential < 75.0 AND oppwinningpercent < 0.344227511991 AND oppwinningpercent >= 0.338446357558 )
    OR
    ( oppnuminjured < 3.0 AND numinjured < 2.0 AND oppnuminjured < 2.0 AND numinjured < 1.0 AND numinjured < -1.0 AND oppwinningpercent < 0.361665214232 AND winpercent < 0.889456415392 AND winpercent < 0.448454638411 AND opprundifferential < 102.0 AND temperature < 77.6698869602 AND oppnuminjured >= -2.0 AND oppwinningpercent < 0.345258664161 AND winpercent >= 0.23209489273 AND opprundifferential >= 75.0 )
    OR
    ( oppnuminjured < 3.0 AND numinjured < 2.0 AND oppnuminjured < 2.0 AND numinjured < 1.0 AND numinjured < -1.0 AND oppwinningpercent < 0.361665214232 AND winpercent < 0.889456415392 AND winpercent < 0.448454638411 AND opprundifferential < 102.0 AND temperature < 77.6698869602 AND oppnuminjured >= -2.0 AND oppwinningpercent >= 0.345258664161 )
    OR
    ( oppnuminjured < 3.0 AND numinjured < 2.0 AND oppnuminjured < 2.0 AND numinjured < 1.0 AND numinjured < -1.0 AND oppwinningpercent < 0.361665214232 AND winpercent < 0.889456415392 AND winpercent < 0.448454638411 AND opprundifferential < 102.0 AND temperature >= 77.6698869602 )
    OR
    ( oppnuminjured < 3.0 AND numinjured < 2.0 AND oppnuminjured < 2.0 AND numinjured < 1.0 AND numinjured < -1.0 AND oppwinningpercent < 0.361665214232 AND winpercent < 0.889456415392 AND winpercent >= 0.448454638411 AND dayssincegame < 5.0 AND opprundifferential < 99.0 AND oppwinningpercent < 0.360286025994 AND rundifferential < 84.0 AND oppwinningpercent < -0.152536582405 AND temperature < 63.7591012091 AND oppnuminjured >= 1.0 AND rundifferential >= 48.0 AND opprundifferential < 66.0 )
    ```

3. Explain in English one of the rules in this (unpruned) tree.

    If oppnuminjured < 3.0, and numinjured < 2.0, and oppnuminjured < 2.0, and numinjured < 1.0, and numinjured < -1.0, and oppwinningpercent < 0.361665214232, and winpercent < 0.889456415392, and winpercent < 0.448454638411, and opprundifferential < 102.0, and temperature >= 77.6698869602, then winner = 1.

4. How did you implement pruning?
  
    Originally we used greedy reduced-error pruning, converting each non-leaf node to a leaf, assigning the mode classification over examples at that node, and computing the resulting accuracy on the validation set. We greedily selected the node whose pruning contributed to the greatest increase in accuracy. This process continued until the accuracy gain was zero.

    Since this was computationally intractable for the larger data set, we switched to non-greedy reduced error pruning, which repeatedly the first node starting from the root that contributed to an increase in accuracy.

5. Apply your algorithm to the training set, with pruning. Print out a Boolean formula in disjunctive normal form that corresponds to the pruned tree learned from the training set.

    ```

    ( oppnuminjured < 3.0 AND numinjured < 2.0 AND oppnuminjured < 2.0 AND numinjured < 1.0 AND numinjured < -1.0 )
    OR
    ( oppnuminjured < 3.0 AND numinjured < 2.0 AND oppnuminjured < 2.0 AND numinjured < 1.0 AND numinjured >= -1.0 AND oppnuminjured < 1.0 AND numinjured >= 0.0 AND oppnuminjured >= -1.0 AND winpercent < 1.20544531474 AND oppwinningpercent < 0.229985544719 AND winpercent < 0.491452152261 )
    OR
    ( oppnuminjured < 3.0 AND numinjured < 2.0 AND oppnuminjured < 2.0 AND numinjured < 1.0 AND numinjured >= -1.0 AND oppnuminjured < 1.0 AND numinjured >= 0.0 AND oppnuminjured >= -1.0 AND winpercent < 1.20544531474 AND oppwinningpercent < 0.229985544719 AND winpercent >= 0.491452152261 AND oppwinningpercent < 0.0068583423205 )
    OR
    ( oppnuminjured < 3.0 AND numinjured < 2.0 AND oppnuminjured < 2.0 AND numinjured < 1.0 AND numinjured >= -1.0 AND oppnuminjured < 1.0 AND numinjured >= 0.0 AND oppnuminjured >= -1.0 AND winpercent < 1.20544531474 AND oppwinningpercent >= 0.229985544719 )
    OR
    ( oppnuminjured < 3.0 AND numinjured < 2.0 AND oppnuminjured < 2.0 AND numinjured < 1.0 AND numinjured >= -1.0 AND oppnuminjured >= 1.0 AND opprundifferential < 18.0 AND opprundifferential >= -3.0 AND rundifferential < 38.0 AND opprundifferential < 8.0 )
    OR
    ( oppnuminjured < 3.0 AND numinjured < 2.0 AND oppnuminjured < 2.0 AND numinjured < 1.0 AND numinjured >= -1.0 AND oppnuminjured >= 1.0 AND opprundifferential < 18.0 AND opprundifferential >= -3.0 AND rundifferential < 38.0 AND opprundifferential >= 8.0 AND rundifferential < 3.0 )
    OR
    ( oppnuminjured < 3.0 AND numinjured < 2.0 AND oppnuminjured < 2.0 AND numinjured < 1.0 AND numinjured >= -1.0 AND oppnuminjured >= 1.0 AND opprundifferential < 18.0 AND opprundifferential >= -3.0 AND rundifferential < 38.0 AND opprundifferential >= 8.0 AND rundifferential >= 3.0 AND rundifferential >= 19.0 AND opprundifferential < 11.0 )
    OR
    ( oppnuminjured < 3.0 AND numinjured < 2.0 AND oppnuminjured < 2.0 AND numinjured < 1.0 AND numinjured >= -1.0 AND oppnuminjured >= 1.0 AND opprundifferential < 18.0 AND opprundifferential >= -3.0 AND rundifferential < 38.0 AND opprundifferential >= 8.0 AND rundifferential >= 3.0 AND rundifferential >= 19.0 AND opprundifferential >= 11.0 AND temperature < 75.5465290668 AND oppwinningpercent < 0.744614772184 AND oppwinningpercent >= 0.538869174358 AND rundifferential >= 33.0 )
    OR
    ( oppnuminjured < 3.0 AND numinjured < 2.0 AND oppnuminjured < 2.0 AND numinjured < 1.0 AND numinjured >= -1.0 AND oppnuminjured >= 1.0 AND opprundifferential < 18.0 AND opprundifferential >= -3.0 AND rundifferential < 38.0 AND opprundifferential >= 8.0 AND rundifferential >= 3.0 AND rundifferential >= 19.0 AND opprundifferential >= 11.0 AND temperature < 75.5465290668 AND oppwinningpercent >= 0.744614772184 )
    OR
    ( oppnuminjured < 3.0 AND numinjured < 2.0 AND oppnuminjured < 2.0 AND numinjured < 1.0 AND numinjured >= -1.0 AND oppnuminjured >= 1.0 AND opprundifferential < 18.0 AND opprundifferential >= -3.0 AND rundifferential < 38.0 AND opprundifferential >= 8.0 AND rundifferential >= 3.0 AND rundifferential >= 19.0 AND opprundifferential >= 11.0 AND temperature >= 75.5465290668 )
    OR
    ( oppnuminjured < 3.0 AND numinjured < 2.0 AND oppnuminjured < 2.0 AND numinjured < 1.0 AND numinjured >= -1.0 AND oppnuminjured >= 1.0 AND opprundifferential < 18.0 AND opprundifferential >= -3.0 AND rundifferential >= 38.0 )
    OR
    ( oppnuminjured < 3.0 AND numinjured < 2.0 AND oppnuminjured < 2.0 AND numinjured < 1.0 AND numinjured >= -1.0 AND oppnuminjured >= 1.0 AND opprundifferential >= 18.0 AND opprundifferential < 21.0 )
    OR
    ( oppnuminjured < 3.0 AND numinjured < 2.0 AND oppnuminjured < 2.0 AND numinjured < 1.0 AND numinjured >= -1.0 AND oppnuminjured >= 1.0 AND opprundifferential >= 18.0 AND opprundifferential >= 21.0 AND rundifferential < 100.0 AND opprundifferential < 40.0 AND rundifferential < 62.0 AND oppwinningpercent < 0.628065698071 AND winpercent < 0.692990167813 AND oppdayssincegame >= 1.0 AND rundifferential < 8.0 AND winpercent < 0.241416698888 )
    OR
    ( oppnuminjured < 3.0 AND numinjured < 2.0 AND oppnuminjured < 2.0 AND numinjured < 1.0 AND numinjured >= -1.0 AND oppnuminjured >= 1.0 AND opprundifferential >= 18.0 AND opprundifferential >= 21.0 AND rundifferential < 100.0 AND opprundifferential < 40.0 AND rundifferential >= 62.0 AND winpercent < 0.922647755797 AND opprundifferential < 22.0 )
    OR
    ( oppnuminjured < 3.0 AND numinjured < 2.0 AND oppnuminjured < 2.0 AND numinjured < 1.0 AND numinjured >= -1.0 AND oppnuminjured >= 1.0 AND opprundifferential >= 18.0 AND opprundifferential >= 21.0 AND rundifferential < 100.0 AND opprundifferential < 40.0 AND rundifferential >= 62.0 AND winpercent < 0.922647755797 AND opprundifferential >= 22.0 AND winpercent < 0.835894061014 AND temperature < 75.0707088364 AND homeaway=0 AND winpercent < 0.0433625972576 )
    OR
    ( oppnuminjured < 3.0 AND numinjured < 2.0 AND oppnuminjured < 2.0 AND numinjured < 1.0 AND numinjured >= -1.0 AND oppnuminjured >= 1.0 AND opprundifferential >= 18.0 AND opprundifferential >= 21.0 AND rundifferential < 100.0 AND opprundifferential < 40.0 AND rundifferential >= 62.0 AND winpercent < 0.922647755797 AND opprundifferential >= 22.0 AND winpercent < 0.835894061014 AND temperature < 75.0707088364 AND homeaway=0 AND winpercent >= 0.0433625972576 AND temperature < 74.0985596821 AND numinjured >= 0.0 AND winpercent < 0.101794655402 )
    ```

6. What is the difference in size (number of splits) between the pruned and unpruned trees?
    
    The unpruned tree has 7004 nodes. The pruned tree has 485. This was potentially too aggressive, since we're pruning from the top instead of the bottom, but makes for a relatively speedy runtime, and an increase in accuracy of roughly 1.5% in contrast with the 2.9% garnered from greedy pruning (which took 2 hours and pruned down to 1926 nodes).

7. Test the unpruned and pruned trees on the validation set. What are the accuracies of each tree? Explain the difference, if any.

    Unpruned: 0.904831932773
    Pruned: 0.92006302521

    The pruned tree fits the validation set much better.

8. Create learning curve graphs for both unpruned and pruned trees. Is there a difference between the two graphs?

    ![Unpruned performance](https://cldup.com/PnGb4MSOz0-3000x3000.png)
    ![Pruned performance](https://cldup.com/ukRpo9BsRN-3000x3000.png)
    ![Comparison](https://cldup.com/YSK4v01y08-3000x3000.png)

    The pruned tree performs better on the validation set.

9. Which tree do you think will perform better on the unlabeled test set? Why? Run this tree on the test file and submit your predictions as described in the submission instructions.
    
    The pruned tree will perform better.

    | Tree     | CCI (Training) | CCI (Validation) | Difference |
    |==========|================|==================|============|
    | Unpruned | 0.994854600283 | 0.904831932773   | ~.00075    |
    | Pruned   | 0.920815672381 | 0.92006302521    | ~.09       |

    The above table summarizes the difference between the pruned and unpruned trees. For the pruned tree, CCI_training - CCI_validation is roughly 0.075 percentage points; in contrast, this difference is roughly 9 percentage points for the unpruned tree. This suggests that the pruned tree avoids overfitting the training data.

10. Which members of the group worked on which parts of the assignment?

    - Sarah implemented the main ID3 function, pruning, and various utility functions (create_predictions, Node.print_tree)
    - Aiqi implemented the ID3 helper functions, Node.print_dnf, and the learning curve graphs