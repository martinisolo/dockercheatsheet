FROM ubuntu:latest
#WORKDIR /
# Install OS-level dependencies
RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive \
    apt-get install --no-install-recommends --assume-yes \
    python3 python3-pip ffmpeg curl python3.12-venv
RUN curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp \
&& chmod a+rx /usr/local/bin/yt-dlp

COPY ./app /app/

WORKDIR /app

RUN chmod +x ./entrypoint.sh

ENTRYPOINT [ "/app/entrypoint.sh" ]

CMD [ "echo", "Default argument from CMD instruction" ]

# yt-dlp --extract-audio --audio-format mp3 https://youtu.be/4HR3p5SP9xY?si=vD_9Z_dr8WHQNSgI

# Create the virtual environment
#RUN python3 -m venv /venv
#ENV PATH=/venv/bin:$PATH

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

