#requiere python 3.10.12 y ffmpeg
sudo apt update && sudo apt install ffmpeg python3 python3-pip
#dependencias
pip install -r requirements.txt
pip install git+https://github.com/m-bain/whisperx.git --upgrade
pip install torch==2.0.0 torchvision==0.15.1 torchaudio==2.0.1 --index-url https://download.pytorch.org/whl/cu118   o conda install pytorch==2.0.0 torchaudio==2.0.0 pytorch-cuda=11.8 -c pytorch -c nvidia

