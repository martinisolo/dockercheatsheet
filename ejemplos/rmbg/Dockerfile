FROM ubuntu:latest
WORKDIR /app

# Install OS-level dependencies
RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive \
    apt-get install --no-install-recommends --assume-yes \
    build-essential python3 python3-pip python3-dev curl python3.12-venv wget

# Create the virtual environment
RUN python3 -m venv /venv
ENV PATH=/venv/bin:$PATH

#COPY ./app /app/

# Le decimos que escuche en el puerto 80 para el servidor Web
EXPOSE 80

#RUN  pip install autotrain-advanced

#RUN bash -c "source ~/miniconda3/bin/activate"
#ENV PATH=~/miniconda3/bin/activate:$PATH
#RUN ~/miniconda3/bin/conda init --all



#RUN ~/miniconda3/bin/conda create -n autotrain -y python=3.10 \
#&& ~/miniconda3/bin/conda init --all \
#&& ~/miniconda3/bin/conda activate autotrain \
#&& pip install autotrain-advanced \
#&& ~/miniconda3/bin/conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia \
#&& ~/miniconda3/bin/conda install -c "nvidia/label/cuda-12.1.0" cuda-nvcc

# Create the virtual environment
#RUN python3 -m venv /venv
#ENV PATH=/venv/bin:$PATH

#RUN pip install autotrain-advanced

#RUN pip install -U openai-whisper

#WORKDIR /app

#RUN apt-get update && apt install python3 python3-pip ffmpeg curl python3.12-venv -y
# RUN bash -c 'mkdir mi_entorno && cd mi_entorno && python3 -m venv mi_entorno && source mi_entorno/bin/activate'

#RUN mkdir mi_entorno && cd mi_entorno && python3 -m venv mi_entorno && source mi_entorno/bin/activate
#RUN pip install -U openai-whisper 
# RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs
#| sh 
# RUN pip install --no-input setuptools-rust

# curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp
# chmod a+rx /usr/local/bin/yt-dlp
# yt-dlp --extract-audio --audio-format mp3 https://youtu.be/4HR3p5SP9xY?si=vD_9Z_dr8WHQNSgI

