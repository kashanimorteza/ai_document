<!--------------------------------------------------------------------------------- Description -->
# Loss
    AI : Resolve : Learning



<!--------------------------------------------------------------------------------- Structure -->
<br><br>

## Description
```
```



<!--------------------------------------------------------------------------------- Structure -->
<br><br>

## Structure
```
Definition | Function | Derivative | Input | Output | Shape | Advantages | Disadvantages | Where it’s used today
```



<!--------------------------------------------------------------------------------- MSE -->
<br><br>

## MSE
```
Mean Squared Error
More Gradient > Fast learning | Less stability
Not suitable when we have outlier data.
Problem : Regression
```



<!--------------------------------------------------------------------------------- MAE -->
<br><br>

## MAE
```
Mean Absolute Error
Less Gradient > Slow learning | More stability
Suitable for when we have outlier data.
Problem : Regression
```



<!--------------------------------------------------------------------------------- Huber -->
<br><br>

## Huber
```
Combination of MSE and MAE
Problem : Regression
```



<!--------------------------------------------------------------------------------- Cross-Entropy -->
<br><br>

## Cross-Entropy
```
```


<!--------------------------------------------------------------------------------- Contrastive -->
<br><br>

## Contrastive
```
Network   : Siamese
```
```
Input  = [A , A]
Label  = Positive
Output = 1
Loss   = Low

Input  = [A , A]
Label  = Positive
Output = 0
Loss   = High
```
```
Input  = [A , B]
Label  = Negative
Output = 1
Loss   = High

Input  = [A , B]
Label  = Negative
Output = 0
Loss   = Low
```
