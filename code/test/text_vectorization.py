from keras.layers import TextVectorization

text_vectorization = TextVectorization(output_mode="int", output_sequence_length=4)

dataset = ["I write, erase, rewrite", "Erase again, and then", "A poppy blooms"]

test_data = ["write for natural language processing"]
print(text_vectorization(test_data))

text_vectorization.adapt(dataset)

print(text_vectorization.get_vocabulary())

['', '[UNK]', 'erase', 'write', 'then', 'rewrite', 'poppy', 'i', 'blooms', 'and', 'again', 'a']