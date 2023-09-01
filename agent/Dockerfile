# Base image
FROM ubuntu:20.04

# Labels and Credits
LABEL name="reNgine-agent"
# Environment Variables
ENV DEBIAN_FRONTEND="noninteractive"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install essentials
RUN apt update -y && apt install -y  --no-install-recommends \
    gcc \
    libpq-dev \
    libpcap-dev \
    python3 \
    python3-pip \
    wget


# Download and install go 1.20
RUN wget https://golang.org/dl/go1.20.linux-amd64.tar.gz
RUN tar -xvf go1.20.linux-amd64.tar.gz
RUN rm go1.20.linux-amd64.tar.gz
RUN mv go /usr/local


# ENV for Go
ENV GOROOT="/usr/local/go"
ENV PATH="${PATH}:${GOROOT}/bin"
ENV PATH="${PATH}:${GOPATH}/bin"

ENV GOPATH=$HOME/go
ENV PATH="${PATH}:${GOROOT}/bin:${GOPATH}/bin"

# Make directory for app
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Download Go packages
# RUN go install -v github.com/hakluke/hakrawler@latest
#
# RUN GO111MODULE=on go install -v -v github.com/bp0lr/gauplus@latest
#
# RUN GO111MODULE=on go install -v github.com/jaeles-project/gospider@latest
#
# RUN go install -v github.com/owasp-amass/amass/v3/...@latest
#
# RUN go install -v github.com/ffuf/ffuf@latest
#
# RUN go install -v github.com/tomnomnom/assetfinder@latest
# RUN GO111MODULE=on go install -v github.com/tomnomnom/gf@latest
# RUN GO111MODULE=on go install -v github.com/tomnomnom/unfurl@latest
# RUN GO111MODULE=on go install -v github.com/tomnomnom/waybackurls@latest
#
# RUN GO111MODULE=on go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
# RUN GO111MODULE=on go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
# RUN GO111MODULE=on go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest
RUN GO111MODULE=on go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest


# # Update Nuclei and Nuclei-Templates
# RUN nuclei -update
# RUN nuclei -update-templates

# Copy requirements
COPY ./requirements.txt /tmp/requirements.txt
RUN pip3 install --upgrade setuptools pip && \
    pip3 install -r /tmp/requirements.txt

# # install eyewitness
#
# RUN python3 -m pip install fuzzywuzzy \
#     selenium \
#     python-Levenshtein \
#     pyvirtualdisplay \
#     netaddr

# Copy source code
COPY . /usr/src/app/
