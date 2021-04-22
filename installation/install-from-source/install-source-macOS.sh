# 1) Clone Hummingbot repo
#git clone https://github.com/CoinAlpha/hummingbot.git
# Install code from Idex repo temporarily, while we wait for our PR#3199 to be merged into CoinAlpha's repo
git clone -b idex/developmentAkTech-coinalpha-rebase https://github.com/idexio/hummingbot.git
# 2) Navigate into the hummingbot folder
cd hummingbot
# 3) Run install script
./install
# 4) Activate environment
conda activate hummingbot
# 5) Compile
./compile
# 6) Run Hummingbot
bin/hummingbot.py