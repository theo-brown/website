systemctl --user stop website
git reset --hard
git submodule init
git pull --recurse-submodules
systemctl --user start website
