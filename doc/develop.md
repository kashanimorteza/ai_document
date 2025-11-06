# ai_examples
    this is ai_examples

<!--------------------------------------------------------------------------------- Resource -->
<br><br>

## Resource  
<!-------------------------- Website -->
Website
```
tensorflow : www.tensorflow.org
pytorch    : pytorch.org
keras      : keras.io
sklearn    : scikit-learn.org
opencv     : opencv.org

Google Colab : colab.research.google.com
jupyter      : jupyter.org

stanford     : cs.stanford.edu/people/karpathy/convnetjs/index.html
playground   : playground.tensorflow.org
```

<!--------------------------------------------------------------------------------- Source -->
<br><br>

## Source
<!-------------------------- Download -->
Download
```bash
git clone --depth=1 git@github.com:kashanimorteza/ai_examples.git
cd ai_examples
```
<!-------------------------- Install python -->
Install python
```bash
brew install openssl

```
<!-------------------------- Install python -->
Install python
```bash
add-apt-repository ppa:deadsnakes/ppa
apt update -y
apt install python3 -y
apt install python3-pip -y
apt install python3-venv -y
```
<!-------------------------- Virtual Environment -->
Virtual Environment
```bash
python3 -m venv .myenv3
.myenv3/bin/python3 -m pip install --upgrade pip  
source .myenv3/bin/activate
pip install -r requirements.txt
pip install --upgrade pip setuptools wheel
pip install "urllib3<2"
```
<!--------------------------------------------------------------------------------- Examples -->
<br><br>

<!-------------------------- TensorFlow -->
## TensorFlow

<!-------------------------- PyTorch -->
## PyTorch

<!-------------------------- Keras -->
## Keras


<!--------------------------------------------------------------------------------- Linux -->
<br><br>

## Linux
```
sudo apt install libgl1
pip install urllib3==1.26.18
```


<!--------------------------------------------------------------------------------- Examples -->
<br><br>

## Examples

### 001 : Filter
### 002 : Regression




<!--------------------------------------------------------------------------------- Save -->
<br><br>

## Save Model
Model Architecture 
```
json | yaml
```

Model Weights
```
Befor/After Training
During Training
```

Entire Model
```
Befor/After Training
During Training
```



<!--------------------------------------------------------------------------------- Examples -->
<br><br>

## ExamObject detectionples

pip uninstall -y protobuf tensorflow object-detection tf-models-official
pip uninstall -y protobuf object-detection

pip install "protobuf<=3.20.3"

cd /Volumes/data/documents/ai_document/develop/models/research
pip install .


export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python

python object_detection/builders/model_builder_tf2_test.py



<!--------------------------------------------------------------------------------- Clear github -->
<br><br>

## Clear github
```bash
rm -rf .git
git init
git add .
git commit -m "Initial commit (reset history)"
git branch -M main
git remote add origin https://github.com/kashanimorteza/ai_document.git
git branch -M main
git remote -v
git push -u origin main --force
```