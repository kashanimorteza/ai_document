<!--------------------------------------------------------------------------------- RNN -->
# RNN : Recurrent Neural Network
[AI] > [Resolve] > [Learning] > [Algorithm] > [Neural network] > [Network]



<!--------------------------------------------------------------------------------- Description -->
<br><br>

## Definition
<!-------------------------- Definition -->
```
مشکلاتی که در آنها ترتیب ورودی اهمیت دارد
فرآیندی که نیاز به یک مرحله پردازش قبلی دارد
```
```
Problems where input order matters
A process that requires a previous processing step
```
```
Each of our processing units has two inputs instead of one: 
    the word itself 
    the vector resulting from processing all of the previous outputs
```
```
The first one is ruining the work because it has no past
    We consider a zero random vector to solve this problem and the system is integrated with two inputs
```
```
Self-supervised tarining
Backpropagation through time (BPTT)
Truncated BPTT
```

<!-------------------------- Disadvantages -->
Disadvantages
```
Simple RNN cell does not have Long-Term Dependence

Vanishing Gradient : 
    LSTM solved this problem

Exploding Gradient :
    Resolving with Gradient Clipping
    GRU solved this problem

```

<!-------------------------- Usage -->
Usage
```
NLP
Speech Recognition
Video Classification
Time series forecasting
Time series forecasting
```



<!--------------------------------------------------------------------------------- Resource -->
<br><br>

## Resource
```
Course : CS224n : Stanford NLP
```



<!--------------------------------------------------------------------------------- Architecture -->
<br><br>

## Architecture
[Simple](https://github.com/kashanimorteza/ai_document/blob/main/doc/rnn_simple.md)

[LSTM](https://github.com/kashanimorteza/ai_document/blob/main/doc/rnn_lstm.md)

[GRU](https://github.com/kashanimorteza/ai_document/blob/main/doc/rnn_gru.md)

[Encoder Decoder](https://github.com/kashanimorteza/ai_document/blob/main/doc/rnn_encoder_decoder.md)

[Transformer](https://github.com/kashanimorteza/ai_document/blob/main/doc/rnn_transformer.md)



<!--------------------------------------------------------------------------------- Structure -->
<br><br>

## Structure
```
Initial Hidden State 
Hidden State
```



<!--------------------------------------------------------------------------------- Link -->
[AI]: https://github.com/kashanimorteza/ai_document/blob/main/README.md
[Resolve]: https://github.com/kashanimorteza/ai_document/blob/main/doc/resolve.md
[Learning]: https://github.com/kashanimorteza/ai_document/blob/main/doc/learning.md
[Algorithm]: https://github.com/kashanimorteza/ai_document/blob/main/doc/learning.md#algorithm
[Neural network]: https://github.com/kashanimorteza/ai_document/blob/main/doc/neural_network.md
[Network]: https://github.com/kashanimorteza/ai_document/blob/main/doc/neural_network.md#network