cd ~
export CONDAPATH="$(pwd)/miniconda3"
export PYTHON="$(pwd)/miniconda3/envs/hummingbot/python3"
# Clone Hummingbot
#git clone https://github.com/CoinAlpha/hummingbot.git
# Install code from Idex repo temporarily, while we wait for our PR#3199 to be merged into CoinAlpha's repo
git clone -b idex/developmentAkTech-coinalpha-rebase https://github.com/idexio/hummingbot.git
# Install Hummingbot
export hummingbotPath="$(pwd)/hummingbot" && cd $hummingbotPath && ./install
# Activate environment and compile code
conda activate hummingbot && ./compile
# Start Hummingbot 
winpty python bin/hummingbot.py