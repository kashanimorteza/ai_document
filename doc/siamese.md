<!--------------------------------------------------------------------------------- Description -->
# Siamese
    AI : Resolve : Learning : Algorithm : Neural network : Network



<!--------------------------------------------------------------------------------- Resource -->
<br><br>

## Resource
Code : [siamese_1.ipynb]
Code : [pyimagesearch]



<!--------------------------------------------------------------------------------- Description -->
<br><br>

## Description
```
Problem    : Classification : Binary
Resolve    : Learning : Deep Learning
Field      : Verification | Recognition
Algorithm  : Neural Network
Loss       : Contrastive
Activation : Swish relu
```



<!--------------------------------------------------------------------------------- Usage -->
<br><br>

## Usage
```
Verification : Face | Signature | Handwriting 
Recognition  : 
Text Similarity / NLP
```



<!--------------------------------------------------------------------------------- Project -->
<br><br>

## Project
```
Google : FaceNet
```



<!--------------------------------------------------------------------------------- Requirement -->
<br><br>

## Requirement
```
Embedding Vector
Euclidean distance
Squared Euclidean Distance
Cosine Distance
```



<!--------------------------------------------------------------------------------- How it works -->
<br><br>

## How it works
```
1 - convert inputA and inputB to Embedding Vector
2 - calculate distance of Embedding Vector of inputA and inputB
```



<!--------------------------------------------------------------------------------- Structure -->
<br><br>

## Structure
<!-------------------------- Input -->
### Input
```
Multi inputs
An input to this network consists of two data
```
<!-------------------------- Label -->
### Label
```
The labels of this network are similarity and dissimilarity
```
<!-------------------------- Loss -->
### Loss
[Contrastive]

<!-------------------------- Activation -->
### Activation
[Swish relu]



<!--------------------------------------------------------------------------------- Implementation -->
<br><br>

## Implementation
```
1 - Create image pairs : negative and positive
2 - Write Euclidean distance layer
3 - Write loss function
```



<!--------------------------------------------------------------------------------- Links -->
[siamese_1.ipynb]: https://github.com/kashanimorteza/ai_document/blob/main/code/siamese_1.ipynb
[Contrastive]: https://github.com/kashanimorteza/ai_document/blob/main/doc/loss.md#contrastive
[Swish relu]: https://github.com/kashanimorteza/ai_document/blob/main/doc/activation.md#swish-relu
[pyimagesearch]: https://pyimagesearch.com/2021/01/18/contrastive-loss-for-siamese-networks-with-keras-and-tensorflow/