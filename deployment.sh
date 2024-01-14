sudo apt update && sudo apt install ffmpeg
pip install -r requirements.txt
pip install git+https://github.com/m-bain/whisperx.git --upgrade
conda install pytorch==2.0.0 torchaudio==2.0.0 pytorch-cuda=11.8 -c pytorch -c nvidia

nohup python3 grpcServer.py > salida.log 2>&1 &